[TOC]

# 题目描述

**题目描述**

你的任务是计算若干整数的和。

**输入描述**

每行的第一个数N，表示本行后面有N个数。

如果N=0时，表示输入结束，且这一行不要计算。

**输出描述**

对于每一行数据需要在相应的行输出和。

**输入示例**

```
4 1 2 3 4
5 1 2 3 4 5
0 
```

**输出示例**

```
10
15
```

# 编程小课

## 前言

本节课你会学习到下列内容：

- 累加操作
- `sum()`求和
- 算术运算符
- 赋值运算符
- `map()`函数
- 常用的数学运算

## 题目分析

在本题中，你需要计算若干个整数的和，每行第一个数 n 表示后面有 n 个数，后面的几个数是输入的整数，如果 n 为 0 时，结束输入。

根据之前学习的内容，我们可以写出初步的代码。

```python
while True:
      # 将输入的每行数据分割成列表
    input_line = input().split()  
```

n 应当是列表的第一位元素，我们将之转换为整数, 如果 n 为 0，表示输入结束，应当退出程序

```python
# input_line[0]表示是第一个整数，通过int()将之转换成整数
n = int(input_line[0])
# 如果 n == 0, 退出循环
if n == 0:
    break
```

```python
while True:
    input_line = input().split()
    n = int(input_line[0])
    if n == 0:
        break  # 退出循环
```

那么剩下的问题就是对后边的这几位数字进行累加了，方法也很简单，后面共有 n 位数字，我们可以事先定义一个变量 `total` , 用于计算最后的结果，之后进行 n 次循环，把列表中的每一个元素累加到 `total` 上即可，代码如下：

```python
total = 0 # 提前定义一个变量total, 用于计算后面 n 个数字的总和
# 执行 n 次循环
for i in range(n):
      # 累加操作
```

进行累加时，i 从 0 遍历到 n - 1, 共执行 n 次，不过我们需要累加的是第 1 个元素到第 n 个元素（第0个元素是 n), 所以需要对 i 进 + 1 操作

```python
# 将 total 和 input_line[i + 1]进行累加（转为int类型后），重新赋值给 total 
total = total + int(input_line[i + 1])
```

最后将结果打印输出即可, 完整的代码如下：

```python
while True:
    input_line = input().split()
    n = int(input_line[0])
    if n == 0:
        break
    total = 0
    for i in range(n):
        total = total + int(input_line[i + 1])
    print(total)
```

将上面的代码复制到题目中，就可以完成提交了，不过我们还可以对代码进行一些小小的改进。

## 1 算术运算符

算术运算符主要是进行运算，比如最开始的`a + b`, 常用的算术运算符有`+、-、*、/、**、//`，含义分别是加法、减法、乘法、除法、取模、幂运算和整除。

> ⚠️ 在Python3中，除法总是返回浮点数

```python
a = 10 - 5  # 减法运算，将10减去5，结果为5
a = 10 + 5	# 加法运算，将10和5相加，结果为15
a = 5 * 5		# 乘法运算，将5和5相乘，结果为25
a = 10 / 5	# 除法运算，将10除以5，结果为2.0，Python3中，除法总是返回浮点数，即便结果是整数
a = 5 // 2 	# 整数除法运算，将5除以2，结果为2（只保留整数部分）
a = 2 ** 2	# 幂运算，2的2次方，即2^2，结果为4
a = 10 % 4  # 取余数运算，将10除以4，返回余数，即2
```

## 2 赋值运算符

实际上，我们从一开始就在使用赋值运算符了，比如最常用的 `i = 0`, 赋值运算符的作用是将右侧表达式的值赋值给左侧的变量。

> ⚠️ 千万不要混淆相等运算符 `==` 和赋值运算符 `=`, 比如写成 `if i = j` 的形式

除了 `=` 这种赋值运算符之外，我们经常会对某个值进行运算后，再把计算的结果赋给这个值，比如 `total = total + a`， 将 total 的值和 a 进行运算后，再赋值给 total ， 此时我们可以使用复合赋值运算符`+=`

```python
total = 0
for i in range(1, 11):
    total += i  # 与 total = total + i 等价
```

我们通常都使用`sum += i`的形式来书写代码，而且这种形式也常常用于其他算数运算符，比如 `-=、*=、/=、%=`

```python
a += 5  # 相当于 a = a + 5 
a -= 5 	# 相当于 a = a - 5 
a *= 5 	# 相当于 a = a * 5 
a **= 5 # 相当于 a = a ** 5 
a /= 5 	# 相当于 a = a / 5 
a //= 5 # 相当于 a = a // 5 
a %= 5 	# 相当于 a = a % 5 
```

## 3 内置sum函数

> 如果你在代码中重新定义了 `sum` 变量，它将覆盖内置的 `sum` 函数, 所以变量命名要小心。

上面我们完成了累加操作，但其实 Python 列表内置的有 `sum()`函数，可以遍历列表中的所有元素，并将它们相加计算列表中元素的总和。

其基本语法如下：

```python
sum(列表，初始值)
```

初始值是总和的初始值，然后将列表中的元素依次相加，比如下面的示例：

```python
numbers = [1, 2, 3, 4, 5]
total = sum(numbers)
print(total)  # 输出 15，因为 1 + 2 + 3 + 4 + 5 = 15
```

但是还有一个问题仍存在，就是列表中的所有元素仍然是字符串，我们需要用一种快捷操作将列表中的所有元素转换成整数，这可以使用内置的`map()`函数，它也常用于Python中的列表操作，可以将一个函数应用到序列的每个元素，并返回一个包含结果的新序列。`map()` 的一般语法如下：

```python
map(function, list)
```

- `function` 是一个要应用到列表中每个元素的函数。
- `list` 是要处理的列表。

比如下面的示例：

```python
string_numbers = ["1", "2", "3", "4", "5"]

# 使用 map(int, list) 将列表中的所有字符串元素全都转换成整数
# 再在外面加一层list(), 使用list()方法将map的返回结果转为列表
int_numbers = list(map(int, string_numbers))

print(int_numbers)
```

```python
numbers = map(int, input_line[1:])
```

这里的`input_line[1:]`是一个切片操作，表示从列表中获取从指定索引（包括该索引）到序列末尾的所有元素, 然后对这些元素都执行`int`函数转换，将之转换成整数，并最终返回一个新的列表。

完整的代码如下：

```python
while True:
    input_line = input().split()
    n = int(input_line[0])
    if n == 0:
        break
    # input_line[1:]是一个切片操作，表示从列表中获取从指定索引（包括该索引）到序列末尾的所有元素
    # [1:]表示的为获取从索引1到末尾的所有元素，即列表的第二个元素开始，直到最后
    numbers = list(map(int, input_line[1:]))
    total = sum(numbers)
    print(total)
```

## 4 常用的数学运算

Python中内置了一些常用的数学函数，你可以使用这些函数进行一些常见的数学运算。

- `abs(x)`: 返回数字的绝对值
- `max(x, y, z, ...)`: 返回一组数据中的最大值
- `min(x, y, z, ...)`: 返回一组数据中的最小值
- `pow(x, y)`: 返回 x 的 y 次方，参数为整数
- `round(x)`:返回浮点数 x 的四舍五入值

```python
print(abs(-10)) # 返回 -10的绝对值 10
print(max(1,2,3)) # 返回 3 
print(min(1,2,3)) # 返回 1
print(pow(10, 2)) # 100
```

但是更多的数学运算，需要导入`math`模块才能使用

- `math.ceil(x)`: 返回一个大于或等于 x 的最小整数。
- `math.floor(x)`: 向下取整，返回一个比 x 小的最大整数。
- `math.pow(x, y)`: 返回 x 的 y 次方, math模块会把参数转换成浮点数。
- `math.sqrt(x)`: 返回 x 的平方根

```python
import math
print(math.ceil(3.14))   # 4
print(math.floor(-9.99)) #  -10
print(math.pow(10, 2)) # 100.0
print(math.sqrt(100)) # 10.0
```

想要生成一个随机数，可以导入`random`模块

```python
import random
# 生成一个随机数，位于 区间 [0, 1) 之间
random.random() 
```

## 总结

本节课我们用了累加的例子学习了算术运算符和赋值运算符，这些基础运算在以后的编程练习中将无处不在，大家一定要多加练习。

# 代码

```python
while True:
    input_line = list(map(int,input().split()))
    n = input_line[0]
    if n == 0:
        break
    total = sum(input_line[1:])
    print(total)
```

