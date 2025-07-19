## 介绍

pytest 是 python 的一种单元测试框架，同时与自带的 unitest 测试框架类似，相比于 unitest 测试框架使用起来更加简洁，而且效率更高，功能更加强大

- pytest 特点
	- 非常容易上手，入门简单，文档丰富，文档中有很多实例可以进行参考
	- 支持参数化，一样的流程用例步骤使用不同的数据时进行参数化数据驱动测试
	- 执行测试用例过程中可以将某些用例跳过，或者对某些预期失败的用例进行标记
	- 支持重复执行失败的用例
	- 便捷管理用例，方便和持续集成工具进行结合使用，便于生成测试报告
	- 具有很多第三方插件，可以进行自定义扩展和使用
- 框架核心作用
	- 定位测试用例
	- 执行测试用例
	- 断言测试用例
	- 生成测试报告

## 一、pytest 详解及常用插件的安装

pytest 有很多强大的插件

- 生成 html 报告 ：pytest-html
- 多线程运行：pytest-xdist
- 控制用例的执行顺序：pytest-ordering
- 失败用例可以重跑：pytest-rerunfailures
- 生成企业级测试报告：ailure-pytest
- 管理基础路径：pytest-base-url
- 测试框架本身：pytest

使用 pip install 安装，以下是 requirements.txt 编写实例

```
pytest-html
pytest-xdist
pytest-ordering
pytest-rerunfailures
ailure-pytest
pytest-base-url
pytest
```

`pip install -r requirements.txt`

## 二、pytest 默认的测试用例规则

一般在项目当中会新建一个用例包

- testcases (包)
	- 创建很多的 py 文件（用例文件）

注意：

- 包名和模块名以及用例名必须以 test 开头或者 test 结尾
- 测试用例类必须以 Test 开头，而且不能有 `__init__` 方法
- 不管是函数的用例还是方法的用例都要以 test 开头或者结尾

演示：

```python
# pytest 用例风格一般使用函数或者方法进行调用

# 函数形式
def test_login01():
    print("现在去登录01")
    

# 方法形式

class TestLogin:
    
    def test_login02(self):
        print("现在去登录02")
```

## 三、pytest 用例执行的 2 种方式

1. 使用命令行方式执行用例

```sh
pytest
```

不加参数则会执行当前目录下所有符合命名要求的测试用例（testxxxx.py）。