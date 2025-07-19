## 学习目标

- 掌握 YAML 文件格式
- 掌握 YAML 文件操作

## 什么是 YAML 文件

“YAML Ain't a Markup Language”（YAML 不是一种标记语言）的递归缩写，它强调的是数据本身，而不是以标记为重点。

YAML 是一种可读性非常高，与程序语言数据结构非常接近。同事具备丰富的表达能力和可扩展性，并且易于使用的数据标记语言。

## 为什么要使用 YAML 文件

YAML 文件也是一种配置文件，但是相较于 ini, conf 配置文件来说，更加简洁，操作简单，还能存放不同类型的数据，而像 ini 存储的值就都是字符串类型，读取之后还要手动转换。

## YAML 的基本语法规则

- 大小写敏感
- 使用缩进表示层级关系
- 缩进时不允许使用 Tab 键，只允许使用空格键（可以是 4 个）
- 缩进的空格数目不重要，只要相同层级的元素左侧对齐即可
- `#` 表示注释

## YAML 的数据结构

- 对象：键值对的集合
- 数组
- 纯量（scalars）：单个的，不可再分的值。

### 对象类型

对象是一组键值对，使用冒号结构表示，会转换成 Python 中的字典。

**YAML：**

```yaml
animals: dog
```

**Python**：

```python
{'animals': 'dog'}
```

**YAML**:

```yaml
person: {name: Tom, age: 20, gender: male}
```

**Python**：

```python
{'person': {'name': 'Tom', 'age': 20, 'gender': 'male'}}
```

### 数组类型

数组类型使用 `-` 为前缀，与 markdown 中的无序列表语法一致，支持缩进表示层级关系

**YAML**：

```yaml
- one
- two
- three
- four
- five
```

**Python**：

```python
['one', 'two', 'three', 'four', 'five']
```

**YAML**：

```yaml
- 
    - 1
    - 2
    - 3
-
    - 4
    - 5
    - 6
```

**Python**：

```python
[[1, 2, 3], [4, 5, 6]]
```

### 纯量类型

纯量类型是最基本的、不可分割的值，类似于基本数据类型。

- 字符串：默认的数据类型，不需要引号包裹。
- 布尔值：true True false False
- 整数
- 浮点数
- 时间：ISO 8601 格式，时间和日期之间需要用 `T` 连接，最后使用 `+` 代表时区。
- 日期：ISO 8601 格式，即 yyyy-mm-dd
- Null：`~` 或 `null`

**YAML**：

```yaml
int: 12
float: 12.3
string: pets
bool: true
None: null
time: 2001-12-14T21:59:43.10-05:00
date: 2018-03-21
```

**Python**：

```python
{
    'int': 12,
    'float': 12.3,
    'string': 'pets',
    'bool': True,
    'None': None,
    'time': datetime.datetime(2001, 12, 14, 21, 59, 43, 100000, tzinfo=datetime.timezone(datetime.timedelta(hours=-5))),
    'date': datetime.date(2018, 3, 21)
}
```

### 复杂结构

**YAML**：

```yaml
cool_list:
  - 10
  - 15
  - 12

hard_list:
  - {key: value}
  - [1,2,3]
  - test:
      - 1
      - 2
      - 3

twice_list:
  -
    - {a: AA}
    - {b: BB}
    - {c: CC}
```

**Python**：

```python
{
    'cool_list': [10, 15, 12],
    'hard_list': [{'key', 'value'}, [1, 2, 3], {'test': [1, 2, 3]}]
    'twice_list':[[{'a':'AA'}, {'b': 'BB'}, {'c': 'CC'}]]
}
```

总结：有 `:` 后面的内容就解析成字典，有 `-` 后面的内容就解析成列表的元素。

## YAML 文件处理

Python 中，可以使用第三方模块 `pyyaml` 来处理 `YAML` 文件。

### 安装 pyyaml 模块

```sh
pip install pyyaml
```

### 读取 YAML 文件

`YAML` 模块使用 `safe_load()` 方法读取 `yaml` 文件，在读取文件之前，和普通文件一样，需要先将文件打开。

```python
import yaml

# 读取 YAML 文件, 以前面复杂结果数据为例
with open('data.yaml', 'r') as file:
    data = yaml.safe_load(file)

# 处理读取到的数据
print(data['cool_list'])
print(data['hard_list'][2]['test'])
```

### 写入 YAML 文件

`YAML` 模块使用 `safe_dump()` 方法向 `yaml` 文件中写入数据，在写入文件之前，也需要先将文件打开。

```python
import yaml

# 要写入的数据
data = {
    'key1': 'value1',
    'key2': 'value2',
    'key3': {
        'key4': 'value4'
    }
}

# 写入 YAML 文件
with open('output.yaml', 'w') as file:
    yaml.safe_dump(data, file)
```

