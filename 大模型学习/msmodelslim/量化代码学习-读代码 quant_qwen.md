# 读代码 quant_qwen

首先说明一下代码文件在 msit 仓库里的 `/msmodelslim/example/Qwen/quant_qwen.py`。

读代码的主要目的是加强对我们量化流程代码的熟悉程度，希望可以通过一遍详细的阅读代码达成以下目标：

1. 对基本的量化流程有了概念
2. 加强 Python 基础语法的学习
3. 对用到的 Python 工具模块熟悉

## 代码整体结构

### 1 核心模块组成

- 参数解析模块（`parse_arguments`）
- 量化器主类（`Quantifier`）
- 辅助函数集（数据处理 / 层选择等）
- 主执行流程（main）

### 2 关键功能组件

```python
# 参数解析部分（示例）
def parse_arguments():
    parser.add_argument('--model_path', type=str, help="模型路径")
    parser.add_argument('--w_bit', type=int, default=8, help="权重量化位数")
    parser.add_argument('--a_bit', type=int, default=8, help="激活值量化位数")
    # ...共30+个可配置参数

# 量化器类结构
class Quantifier:
    def __init__(self):  # 初始化模型和tokenizer
        self.model = SafeGenerator加载模型
        self.tokenizer = SafeGenerator加载分词器
        
    def create_quant_config():  # 创建量化配置
        # 根据模型类型自动生成disable_names
        # 支持qwen1/qwen2等不同架构
        
    def convert():  # 执行量化过程
        AntiOutlier异常值抑制 → Calibrator校准 → 保存量化模型
```

### 3 量化流程

主流程：
1. 加载原始模型和tokenizer
2. 准备校准数据集
3. 执行异常值抑制（AntiOutlier）
4. 创建量化配置（QuantConfig）
5. 运行校准器（Calibrator）
6. 保存量化后模型

## 读代码

### 1 顶层结构速览

先分析一下这个脚本的顶层结构：

```python
# 导入基础依赖库
import os
import json
import sys
import torch
import torch.nn.functional as F # PyTorch的神经网络函数库

# 获取当前脚本的绝对路径
current_directory = os.path.dirname(os.path.abspath(__file__))
# 构建父目录路径（向上跳两级目录）
parent_directory = os.path.abspath(os.path.join(current_directory, '..', ".."))
# 将父目录加入系统路径，以便导入自定义模块
sys.path.append(parent_directory)

# 从自定义模块导入所需组件
from ascend_utils.common.security.path import get_valid_write_path, get_valid_read_path
from example.common.utils import SafeGenerator, ArgumentParser, StringArgumentValidator, MAX_KEY_LENGTH, \
    MAX_JSON_LENGTH, cmd_bool
from msmodelslim.pytorch.llm_ptq.anti_outlier import AntiOutlier, AntiOutlierConfig # 抗异常值模块
from msmodelslim.pytorch.llm_ptq.llm_ptq_tools import Calibrator, QuantConfig # 量化核心工具
from msmodelslim.pytorch.llm_ptq.llm_ptq_tools.layer_select import LayerSelector # 层选择器

# 设备类型常量定义
CPU = "cpu"
NPU = "npu"

# 定义Qwen2/2.5架构的禁用层名称生成函数
def get_down_proj_disable_names(num_layers: int) -> list:
    ...

# 定义Qwen1/1.5架构的禁用层名称生成函数
def get_c_proj_disable_names(num_layers: int) -> list:
    ...

# 数据填充对齐函数
def get_padding_data(tokenizer, calib_list, device_type):
    ...

# 批量数据tokenize处理
def get_batch_tokenized_data(tokenizer, input_texts, device_type, batch_size=4):
    ...

# 自动层选择函数（基于阈值）
def auto_layer_select(model, disable_names, disable_threshold, select_layer_data):
	...

# 参数解析函数（包含30+个量化参数）
def parse_arguments():
    ...

# 量化器类定义
class Quantifier:
	...

# 主函数入口    
if __name__ == '__main__':
	...
```

接下来从主线逻辑 `__main__`处开始分析：

`args = parse_arguments()`：这行是调用 parse_arguments() 函数来获取用户命令行输入的参数配置，这个函数在当前脚本定义，包含了千问模型量化过程所需要的所有参数，大概有 30 多个。

### 2 脚本参数简要分析

阅读 parse_arguments() 的定义，并结合 README 的一些说明，可以对一些重要的参数进行理解学习：

#### 2.1 基础必选参数

1. model_path、save_directory

```python
parser.add_argument('--model_path', type=str, help="模型和tokenizer路径")
parser.add_argument('--save_directory', type=str)
```

这两个参数指明了模型的输入和输出路径，待量化的模型是 model_path，量化后模型的输出结果是 save_directory

2. model_type

这个参数指明了 Qwen 模型的版本， 是一个可选参数，在 `qwen1, qwen1.5, qwen2, qwen2.5` 中选择，之所以有这个参数是因为不同 Qwen 模型版本的结构不一样，然后这里没有最新的 qwen3 模型，说明暂时还没有适配。

```python
parser.add_argument('--model_type', default='qwen2', choices=['qwen1', 'qwen1.5', 'qwen2', 'qwen2.5'])
```

#### 2.2 量化精度控制相关

1. w_bit / a_bit：权重量化、激活值量化参数

```python
parser.add_argument('--w_bit', type=int, default=8)  # 权重量化bit
parser.add_argument('--a_bit', type=int, default=8)   # 激活值量化bit
```

可以有：

- W8A8：常规 8 bit 量化
- W8A16：激活值保持 16 bit
- W4A8：稀疏量化场景

这部分在 Wiki `大模型量化功能表以及介绍` 文档里有一个相对完整的介绍，可以跳转查看。

2. device_type

```python
parser.add_argument('--device_type', choices=['cpu', 'npu'], default='cpu')
```

可以选择使用 CPU 还是 NPU 来跑量化。

#### 2.3 校准数据相关

1. calib_file

```python
parser.add_argument('--calib_file', default='common/teacher_qualification.jsonl')
```

用于设置校准数据集文件路径，校准数据集通常包含一组具有代表性的输入数据，用于提高量化效率、保持量化后模型的性能和准确性。

2. calib_text

```python
parser.add_argument('--calib_text', nargs='+') 
```

用于直接传入校准文本，但是 README 里没有详细说明。

#### 2.4 异常值处理

1. anti_method

```python
parser.add_argument('--anti_method', type=str, default='')
```

这是离群值抑制的参数

可选算法：

- m1：SmoothQuant
- m2：SmoothQuant加强版
- m3：AWQ算法
- m4：smooth优化算法
- m5：CBQ量化算法
- m6：Flex smooth（需多卡环境）

2. co_sparse

```python
parser.add_argument('--co_sparse', type=cmd_bool, default=False)
```

是否开启稀疏量化

#### 2.5 高级功能参数

1. use_kvcache_quant

```python
parser.add_argument('--use_kvcache_quant', type=cmd_bool, default=False)
```

对使用 KVCache 机制的模型进行量化

2. disable_threshold

```python
parser.add_argument('--disable_threshold', type=float, default=0)
```

自动层回退阈值（>0时启用自动回退机制）

---

就先看这么多，如果后面还有需要的参数可以继续重点看，然后也可能专门找个时间把所有的参数都分析一遍。现在进行下一行代码：`checker = SafeGenerator()`

### 3 安全模型加载器简析

这是一个安全模型加载器，位于 `msmodelslim/example/common/utils.py`，接下来分析一下其中的代码。

第一眼关注 `@staticmethod` ，这是我第一次接触 Python 装饰器，由于这部分内容很多就先不完整学习了，不过这个装饰器的作用是将类成员方法声明成为静态的方法，可以不实例化对象就直接调用。

看到这里还以为和 C++ 的 static 一样，结果一问 AI 发现区别很大，关键区别：

| 特性           | Python @staticmethod | C++ static |
|----------------|---------------------|------------|
| 访问类成员     | 不能直接访问类/实例属性 | 可访问静态成员 |
| 内存存储       | 属于类命名空间       | 类级别全局存储 |
| 继承机制       | 可被子类重写         | 不能被子类重写 |
| 参数要求       | 无self/cls参数       | 无this指针 |

嗯，很复杂，暂时先记住这里的作用就是直接被类名调用即可。

后面简单看了一下这个工具类的实现，发现可以暂时先关注一下几个静态方法的声明，具体实现可以先忽略，这里就是相当又封装了一些异常处理逻辑。

---

### 4 RANK 值读取

下一行是：

```python
rank: int = int(os.getenv("RANK", "0"))
```

首先是语法上的解析：

- `rank: int` 是 Python 的类型注解，显式指明 rank 对象是整数类型。
- `os.getenv(str,val)` 表明从系统环境变量里寻找名为 str 的变量，然后如果有则返回，没有就返回默认值 val。这里就是看有没有 RANK 值，没有就返回 0，然后会被 `int()`  强制转换成整型。

接下来是一些量化场景下可能的作用：

进行多卡量化的时候（如 8 张），每张卡都有不同的 RANK 值（0~7），这个值用于区别不同卡的身份，从而可以分配不同的计算任务以及控制权重保存的位置，如果环境变量里没有 RANK 值，那么就会单卡运行。

### 5 获取参数

```python
model_path = args.model_path
save_directory = args.save_directory
```

读取输入输出路径。

```python
num_layers = checker.get_config_from_pretrained(
        model_path,
        trust_remote_code=args.trust_remote_code
    ).num_hidden_layers
```

读取模型的隐藏层层数，用于确定模型的结构，之后可以用来动态生成禁用层。

---

### 6 离群值抑制

```python
anti_outlier_config_val = None
```

这里是先声明一个变量，后面再赋值，也是 Python 的一个常用操作。这个应该是和异常值处理模块的配置有关。

```python
 if args.anti_method == 'm3':
        anti_outlier_config_val = AntiOutlierConfig(a_bit=args.a_bit, w_bit=args.w_bit,
                                                    anti_method=args.anti_method, w_sym=args.w_sym,
                                                    dev_type=args.device_type, dev_id=rank)
    elif args.anti_method == 'm6':
        keys = ['.o_proj']
        anti_disable_names = ["model.layers.{}.self_attn.o_proj".format(i) for i in range(num_layers)]
        anti_outlier_config_val = AntiOutlierConfig(anti_method=args.anti_method,
                                                    dev_type=args.device_type,
                                                    disable_anti_names=anti_disable_names, \
                                                    flex_config={'alpha': 0.6, 'beta': 0.3})
    elif args.anti_method:
        anti_outlier_config_val = AntiOutlierConfig(anti_method=args.anti_method,
                                                    dev_type=args.device_type)
```

这里对不同的离群值抑制算法进行了不同的参数配置，m3 对应的是 AWQ 算法，m6 对应的是 Flex smooth 算法，还有其他的离群值抑制算法。

对于 m3，需要的参数为：

- a_bit
- w_bit
- anti_method
- w_sym：权重量化是否为对称量化。
- dev_type
- dev_id = rank

对于 m6，需要的参数为：

- anti_method
- device_type
- anti_disable_names
- 里面还写死了柔性参数配置 flex_config

对于 其他的，就先使用：

- anti_method
- device_type

---

`tokenizer_args = json.loads(args.tokenizer_args)`：将 tokenizer 参数解析成字典对象，用于后续配置 tokenizer 参数。

```python
if tokenizer_args == {} and args.model_type == 'qwen1':
        tokenizer_args = {
            "padding_side":"left",
            "pad_token":"<|extra_0|>",
            "eos_token":"<|endoftext|>"
        }
```

当 tokenizer_args 为空 且 模型是 qwen1 的时候，那么会设置默认的 tokenizer 参数：

- `padding_side='left'`：左侧填充，确保模型关注最重要的右侧信息。
- `pad_token="<extra_0>"`：设置填充 token，这是 Qwen 模型特有的特殊 token。
- `eos_token="<|endoftext|>"`：设置结束 token。

可能是 qwen1 模型有特殊的 token，所以需要专门设置一下

---

```python
quantifier = Quantifier(
	model_path, args, anti_outlier_config_val,
	device_type=args.device_type,
    tokenizer_args=tokenizer_args,
	model_name=args.model_name,
)
```

创建了一个 quantifier 对象，用于执行 qwen 模型的量化过程。其中参数：

- model_path
- args
- anti_outlier_config_val - 离群值抑制配置，前面的部分有详细的参数
- device_type
- tokenizer_args
- model_name

---

```python
tokenized_calib_data = []
```

用于初始化一个空列表，用来存储经过 tokenizer 处理后的校准数据。可以跟踪一下这个变量，看看后面是怎么用的。

---

```python
calib_file = args.calib_file
if calib_file:
        calib_file = get_valid_read_path(calib_file)
        calib_texts = checker.load_jsonl(calib_file)
    else:
        calib_texts = args.calib_texts
```

从参数列表中获取 calib_file 的路径，然后如果获取成功，就使用安全验证函数过滤一下，之后将数据通过 load_jsonl 加载出来。如果没有的话， 那就检查 calib_texts 参数，用户可能直接使用 calib_texts 来传入校准数据。

---

```python
if calib_texts is not None:
    tokenized_calib_data = quantifier.get_tokenized_data(
        calib_texts,
        input_ids_name=args.input_ids_name,
        attention_mask_name=args.attention_mask_name
    )
```

如果存在 calib_texts，那么就调用 Quantifier 类的 get_tokenized_data 方法将原始文本数据转换为模型可处理的 tokenized 格式。这里有 3 个参数：

- calib_texts
- input_id_name：指定输入 ID 的键名
- attention_mask_name：指定注意力掩码的键名

---

```python
tokenized_ant_calib_data = tokenized_calib_data
```

将普通的校准数据复制一份专门用于异常值抑制处理。

---

```python
if args.anti_calib_file:
	args.anti_calib_file = get_valid_read_path(args.anti_calib_file)
	ant_calib_texts = checker.load_jsonl(args.anti_calib_file)
	if ant_calib_texts is not None:
		tokenized_ant_calib_data = quantifier.get_batch_tokenized_data(ant_calib_texts)
```

这段代码用于安全地获取离群值抑制的校准数据集。

---

```python
if isinstance(args.disable_threshold, float) and args.disable_threshold > 0:
        quantifier.create_quant_config(num_layers, tokenized_ant_calib_data)
    elif args.disable_threshold == 0:
        quantifier.create_quant_config(num_layers)
    else:
        raise ValueError("disable_threshold should be a float number >= 0")
```

- disable_threshold：自动回退阈值
  - 大于 0 时，使用校准数据（tokenized_ant_calib_data）自动选择需要回退的层，动态决定哪些层需要回退到高精度计算
  - 等于 0 时，使用预定义的层回退策略

---

```python
quantifier.convert(
    tokenized_calib_data,
    save_directory, 
    args.disable_level, 
    part_file_size=args.part_file_size,
    tokenized_ant_calib_data=tokenized_ant_calib_data
)
```

这里就是调用 quantifier 的 convert 方法，也就是 量化过程。导入一些参数：

- tokenized_calib_data  分词处理后的校准数据，用于在量化过程中收集模型的统计信息，以便确定合适的量化参数。
- save_directory 量化后的保存路径
- args.disable_level 用于控制量化过程中禁用层的一些信息
- part_file_size 用于分割文件
- tokenized_ant_calib_data 处理离群值的校准数据

---

## 量化后处理

```python
# 获取量化类型

quant_type = quantifier.quant_config.model_quant_type.lower()
```

```python
# 从预训练模型加载配置

auto_config = checker.get_config_from_pretrained(
    model_path,
    trust_remote_code=args.trust_remote_code
)
```

```python
# 修改模型配置

checker.modify_config(
    model_path,
    save_directory,
    auto_config.torch_dtype,
    quant_type,
    args
)
```

```python
# 复制分词器文件

checker.copy_tokenizer_files(
    model_path,
    save_directory
)
```

这部分代码主要目的是在完成模型量化构，更新模型的配置信息以及反映量化类型，并将相关的分词器文件复制到保存目录，确保量化后的模型可以正常使用。整个过程是模型量化流程的最后一步，为后续使用量化模型进行推理或训练做准备。
