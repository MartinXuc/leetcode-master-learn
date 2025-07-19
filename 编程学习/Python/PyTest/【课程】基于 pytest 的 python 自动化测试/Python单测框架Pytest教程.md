# 1. What: 单测框架

## 1.1 什么是单测

单元测试是自动化测试的一种形式--这仅仅意味着测试计划是由一个脚本执行的，而不是由人手动执行的。

它们作为软件测试的第一层，通常以函数的形式编写，验证软件程序中各种功能的行为。

## 1.2 为什么要写单元测试

以下列举了一些我为什么使用单元测试的好处：

1. 减少bug：允许你对代码做出任何改变，因为你了解单元测试会在你的预期之中。单元测试可以有效地降低程序出现BUG的机率。
2. 重构：帮助你更深入地理解代码--因为在写单元测试的时候，你需要明确程序所有的执行流程及对应的执行结果等等; 允许在任何时候代码重构，而不必担心破坏现有的代码。这使得我们编写程序更灵活，确保你的代码的健壮性，因为所有的测试都是通过了的。
3. 文档记录：单元测试就是一种无价的文档，它是展示函数或类如何使用的最佳文档，这份文档是可编译、可运行的、并且它保持最新，永远与代码同步。
4. 回归性：自动化的单元测试避免了代码出现回归，编写完成之后，可以随时随地地快速运行测试，而不是将代码部署到设备之后，然后再手动地覆盖各种执行路径，这样的行为效率低下，浪费时间。

# 2. Why: 为什么是Pytest

官网上的 [pytest](https://docs.pytest.org/en/7.3.x/):
helps you write better programs.
The pytest framework makes it easy to write small, readable tests, and can scale to support complex functional testing for applications and libraries.

测试是如此重要，以至于Python带有自己的内置测试框架，称为unittest。但是，在unittest中编写测试可能很复杂，因此近年来，pytest框架已成为标准。

1. 非常容易开始，因为它的简单和容易的语法
2. 可以并行执行测试
3. 可以执行特定测试或测试子集
4. 自动检测测试
5. 跳过测试
6. 开源
7. 使用普通的断言语句而不是 unittest 的 assertSomething 方法（例如，assertEquals、assertTrue）
8. 简化了测试状态的设置和拆卸

# 3. How：Pytest教程

## 3.1 安装

```sh
pip install -U pytest
pip install -U pytest-html
pip install -U pytest-rerunfailures
```

## 3.2 一个简单的例子

```py
# content of test_sample.py
def inc(x):
    return x + 1

def test_answer():
    assert inc(3) == 5
```

执行测试：

```sh
$ pytest
=========================== test session starts ============================
platform linux -- Python 3.x.y, pytest-7.x.y, pluggy-1.x.y
rootdir: /home/sweet/project
collected 1 item

test_sample.py F                                                     [100%]

================================= FAILURES =================================
_______________________________ test_answer ________________________________

    def test_answer():
>       assert inc(3) == 5
E       assert 4 == 5
E        +  where 4 = inc(3)

test_sample.py:6: AssertionError
========================= short test summary info ==========================
FAILED test_sample.py::test_answer - assert 4 == 5
============================ 1 failed in 0.12s =============================

```

执行测试的时候，我们只需要在测试文件 test sample所在的目录下，运行 pytest 即可。
pytest 会在当前的目录下，寻找以 test 开头的文件（即测试文件），找到测试文件之后，进入到测试文件中寻找 test 开头的测试函数并执行。
通过上面的测试输出，我们可以看到该测试过程中，一个收集到了一个测试函数，测试结果是失败的（标记为 F），并且在FAILURES 部分输出了详细的错误信息，帮助我们分析测试原因。
我们可以看到 ”assert func(3) == 5” 这条语句出错了，错误的原因是 func(3)=4，然后我们断言 func(3) 等于 5。

## 3.3 如何编写pytest测试

### 3.3.1 规则

#### 3.3.1.1 编写规则

pytest 执行单测需要按照下面的规则：

1. 测试文件以 `test_` 开头（以 `_test` 结尾也可以）
2. 测试类以 `Test` 开头，并且不能带有 `__init__` 方法
3. 测试函数以 `test_` 开头
4. 断言使用基本的 assert 即可

#### 3.3.1.2 执行规则

执行测试：

```sh
pytest               # 在当前目录下执行所有测试用例
pytest test_mod.py   # 执行指定文件中的所有测试用例
pytest somepath      # 执行指定目录下的所有测试用例
pytest -k stringexpr # 执行匹配到字符串的测试用例
pytest test_mod.py::test_func # 执行指定文件中的指定测试用例
```

### 3.3.2 测试函数

```py
# content of test_sample.py
def func(x):
    return x+1

def test_func():
    assert func(3) == 5
```

### 3.3.3 测试类

```py
# content of test_class.py
class TestClass:
    def test_one(self):
        x = "this"
        assert 'h' in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, 'check')
```

执行测试：

```sh
$ pytest -q test_class.py
.F
================================= FAILURES =================================
____________________________ TestClass.test_two ____________________________
self = <test_class.TestClass object at 0x7fbf54cf5668>
def test_two(self):
x = "hello"
> assert hasattr(x, 'check')
E assert hasattr('hello', 'check')
test_class.py:8: AssertionError
1 failed, 1 passed in 0.01 seconds
```

`pytest -q` 可以不再输出版本信息。

该测试共执行了两个测试样例，一个失败一个成功。同样，我们也看到失败样例的详细信息，和执行过程中的中间结果。
pytest中用点号(.)表示一条用例被执行并通过，用F来标识一条用例被执行并失败。

如果想查看详情可以在pytest命令后面加上-v或者–verbose选项:

```sh
$ pytest -v test_class.py

collected 2 items

test_class.py::TestClass::test_one PASSED                                                                        [ 50%]
test_class.py::TestClass::test_two FAILED                                                                        [100%]

======================================================= FAILURES =======================================================
__________________________________________________ TestClass.test_two __________________________________________________

self = <test_class.TestClass object at 0x7fbcb0a15030>

    def test_two(self):
        x = "hello"
>       assert hasattr(x, 'check')
E       AssertionError: assert False
E        +  where False = hasattr('hello', 'check')

test_class.py:10: AssertionError
```

### 3.3.4 使用raises在单测中捕获异常

有时候我们在做测试的时候，预期就是抛出一个异常，但如果在正常情况下，抛出异常后 pytest 会停止该条测试用例的继续执行，所以我们需要一个期望抛出异常的方法，pytest.raises 就可以做到这一点，代码如下：

```py
# content of test_sysexit.py
import pytest

def f():
    raise SystemExit(1)

def test_mytest():
    # 此处必须抛出SystemExit的异常，用例才会通过
    with pytest.raises(SystemExit):
        f()

def test_add_raises():
    with pytest.raises(AssertionError):
        # 此处必须抛出AssertionError的异常，用例才会通过
        assert 1 + 1 == 3
```



