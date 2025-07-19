首先讲一个推荐的文件结构：根目录下只需要一个入口文件即可，如果是开发一些包或者后端，这个入口文件都可以不要。而所有的核心代码都应该放在一个文件夹里。在根目录下放一个 tests 文件夹，这里面专门放测试，测试文件夹也写成一个 package，也就是放一个 `__init__.py` 文件，这个文件夹里的所有其他文件就都是我们的测试文件。

这里使用 `unitest` ，Python 的标准库自带的测试框架。若按照上方文件的组织方式，可以直接命令行 `python -m unitest`，python 就会自动地执行测试流程。

## 测试怎么写

测试是检查程序运行结果是不是预期结果，所以首先要知道代码应该做什么。

测试文件命名需要以 `test_` 开头，例如 `test_vector.py` 。测试文件中首先 `import unitest`，然后将要测试的内容 import 进来。

然后写测试类：

- 继承 unitest.TestCase 类
- 类名以 `Test` 开头或结尾
- 每一个测试类里面可以有若干个 test method，命名需要 `test_` 开头
- 测试类可以使用 self.assert... 方法来检验，具体说明见 unitest 文档

  - 尽量使用 assertEqual 而不是 assertTrue，用来获得更多的错误信息
  - assertRaises：对一个会 raise 的方法进行测试：

```
with self.assertRaises(ValueError):
    	v = Vectot("1", "2")
```

## 常用的 unitest feature

- 如果想要在 test method 前后做一些动作，可以在测试类定义 `setUp` 函数和 `tearDown` 函数。这样会对每一个 test method 前后都运行。
- 如果想要在 test class 前后做一些动作，可以使用 `setUpClass` 和 `tearDownClass` 函数，需要使用 `classmethod` 装饰器装饰。
- 如果希望测试在某些情况下不运行，可以使用装饰器：`@unitest.skipIf(条件语句, message)` 将 test method 装饰起来

## 运行指定的测试

现在测试被分成了 3 级：

- test module - `test_vector.py`
- test class - `class TestVector`
- test method = `test_init()`

执行 `python -m unitest {module}.{class}.{method}` 方式执行测试，如果不填 method 级那就执行 class 下所有 module，如果不填 class 级那就执行 module 下的所有 class 的 method。