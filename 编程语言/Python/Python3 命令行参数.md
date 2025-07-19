## Python3 命令行参数

Python 提供了 **getopt** 模块来获取命令行参数。

```Plaintext
$ python test.py arg1 arg2 arg3
```

Python 中也可以所用 **sys** 的 **sys.argv** 来获取命令行参数：

- **sys.argv** 是命令行参数列表。
    
- **len(sys.argv)** 计算命令行参数个数。
    

**注：sys.argv[0]** 表示脚本名。

**实例：**

test.py 文件代码如下：

```Plaintext
#!/usr/bin/python3

import sys

print ('参数个数为:', len(sys.argv), '个参数。')
print ('参数列表:', str(sys.argv))
print ('脚本名:', str(sys.argv[0]))
```

执行以上代码，输出结果为：

```Plaintext
$ python3 test.py arg1 arg2 arg3
参数个数为: 4 个参数。
参数列表: ['test.py', 'arg1', 'arg2', 'arg3']
脚本名: test.py
```

### getopt 模块

getopt 模块是专门处理命令行参数的模块，用于获取命令行选项和参数，也就是 **sys.argv**。命令行选项使得程序的参数更加灵活。支持短选项模式 **-** 和长选项模式 **--**。

该模块提供了两个方法及一个异常处理来解析命令行参数。

#### getopt.getopt 方法

getopt.getopt 方法用于解析命令行参数列表，语法格式如下：

```Plaintext
getopt.getopt(args, options[, long_options])
```

方法参数说明：

- **args**: 要解析的命令行参数列表，通常是 `sys.argv[1:]`，这里 `sys.argv` 是一个列表，包含了命令行中所有的参数，`argv[0]` 是脚本名称，`argv[1:]` 是除了脚本名称之外的参数。
    
- **options**: 定义了可接受的短选项，例如 `"n:u:"` 表示 `-n` 和 `-u` 是有效的选项，后面的冒号 `:` 表示该选项需要一个附加的参数。
    
- **long_options**: 定义了可接受的长选项，例如 `["name=", "url="]`，等号 `=` 表示该长选项需要一个附加的参数。
    

该方法返回值由两个元素组成：

1. 一个由 `(option, value)` 元组组成的列表，其中 `option` 是选项字符（短选项或长选项），`value` 是与该选项关联的参数值。
2. 一个参数列表，包含了所有没有前缀 `-` 或 `--` 的参数。

接下来我们定义一个 site() 函数，然后通过命令行输入站点名称 **name** 和网址 **url**，可以用缩写 **n** 和 **u**:

```Python
import sys 
import getopt 
  
  
def site(): 
    name = None
    url = None
  
    argv = sys.argv[1:] 
  
    try: 
        opts, args = getopt.getopt(argv, "n:u:")  # 短选项模式
      
    except: 
        print("Error") 
  
    for opt, arg in opts: 
        if opt in ['-n']: 
            name = arg 
        elif opt in ['-u']: 
            url = arg 
      
  
    print( name +" " + url) 
  
site()
```

测试以上代码，命令行中输入：

```Plaintext
python3 test.py -n RUNOOB -u www.runoob.com
```

输出结果为：

```Plaintext
RUNOOB www.runoob.com
```

以下实例演示长选项模式的使用：

```Python
import sys 
import getopt 
  
def site(): 
    name = None
    url = None
  
    argv = sys.argv[1:] 
  
    try: 
        opts, args = getopt.getopt(argv, "n:u:",  
                                   ["name=", 
                                    "url="])  # 长选项模式
      
    except: 
        print("Error") 
  
    for opt, arg in opts: 
        if opt in ['-n', '--name']: 
            name = arg 
        elif opt in ['-u', '--url']: 
            url = arg 
      
  
    print( name + " " + url) 
  
site()
```

测试以上代码，命令行中输入：

```Plaintext
python3 test.py -n RUNOOB -u www.runoob.com
```

输出结果为：

```Plaintext
RUNOOB www.runoob.com
```

另外一个方法是 `getopt.gnu_getopt`，用到的情况比较少，这里不多做介绍。

#### Exception getopt.GetoptError

在没有找到参数列表，或选项的需要的参数为空时会触发该异常。

异常的参数是一个字符串，表示错误的原因。属性 **msg** 和 **opt** 为相关选项的错误信息。

**实例：**

假定我们创建这样一个脚本，可以通过命令行向脚本文件传递两个文件名，同时我们通过另外一个选项`-h`查看脚本的使用。脚本使用方法如下：

```Plaintext
usage: test.py -i <inputfile> -o <outputfile>
```

test.py 文件代码如下所示：

```Python
#!/usr/bin/python3

import sys, getopt

def main(argv):
   inputfile = ''
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
   except getopt.GetoptError:
      print ('test.py -i <inputfile> -o <outputfile>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print ('test.py -i <inputfile> -o <outputfile>')
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg
   print ('输入的文件为：', inputfile)
   print ('输出的文件为：', outputfile)

if __name__ == "__main__":
   main(sys.argv[1:])
```

```Plaintext
$ python3 test.py -h
usage: test.py -i <inputfile> -o <outputfile>

$ python3 test.py -i inputfile -o outputfile
输入的文件为： inputfile
输出的文件为： outputfile
```