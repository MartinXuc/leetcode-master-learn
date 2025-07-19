# 第 1 课 a + b 问题 I

1. Python 的输入函数是 `input()`
2. 用 `int()` 将输入的字符串转成数字，还可以类比使用其他方式。
3. `input()` 常用的一个操作是 `list = input().split()`
4. 常用 `try` 和 `except` 来处理异常，常用于次数未知的输入行为
5. 非常规的赋值方式：`a = b = c = 42`，`x, y, z = 1, 2, 3`，`a, b = [1, 2]`
6. 主模块调用 `if __name__ =='__main__'`

# 第 2 课 a + b 问题 II

1. `for i in range(n):`
2. `range(start, stop, step)`，左闭右开；step 为 -1 则是从右往左的方向
3. `for line in sys.stdin:` 对每行数据进行处理

# 第 3 课 a + b 问题 III

1. 三元运算符 `语句1 if condition else 语句2`

# 第 4 课 a + b 问题 IV

1. sum 函数求和 `sum(列表，初始值=0)`
2. 快捷操作序列 `map(func, list)`
3. 切片 `list[start:end:step]` ，左闭右开
4. `abs(-1) is 1` 绝对值
5. `max(1,2,3) is 3` 最大值
6. `min(1,2,3) is 1` 最小值
7. `pow(10,2) is 100` 乘方（整数）
8. `round(4.5) is 5` 四舍五入
9. `math.ceil(x)` 顶
10. `math.floor(x)` 底
11. `math.pow(x,y)` 乘方（浮点数）
12. `math.sqrt(x)` 开方
13. `random.random()` 随机数

# 第 5 课 a + b 问题 VIII

pass

# 第 6 课 数组的倒序与隔位输出

1. 可以将其他类型序列转成列表 `list(seq)`
2. 求列表长度 `len(list)`
3. 添加元素到列表末尾 `list.append(x)`
4. 指定位置插入元素 `list.insert(index, x)`
5. 移除值为 x 的元素 `list.remove(x)`，只删除第一个
6. 移除址为 index 的元素 `list.pop(index)`，且带出移除的值
7. 查找 x 的下标 `list.index(x)`
8. 升序排序列表 `list.sort()`
9. 反转列表顺序 `list.reverse()`
10. 列表下标 -1, -2 表示倒数第 1, 2 个数
11. 列表、字典、集合 是可变值；整数、浮点数、字符串、元组 是不可变值

# 第 7 课 摆平积木

pass

# 第 8 课 奇怪的信

pass

# 第 9 课 打印正方形

pass

# 第 10 课 平均绩点

1. 获取字符串长度 `len(str)`
2. 字符串分割 `str.split()`
3. 字符串替换 `str.replace("old", "new")`
4. 字符串连接 `"连接符号".join(list)`，其中 list 是一个字符串列表
5. 保留 2 位小数：`formatted_num = f"{num:.2f}"`
6. 转换成 2 位小数：`formatted_num = float(f"{num:.2f}")`
7. 多用 f 字符串

# 第 11 课 句子缩写

1. 将字符转换成 unicode 编码：`ord(c)`
2. 将 unicode 编码转换成字符：`chr(i)`
3. 字符串转小写：`str.lower()`
4. 字符串转大写：`str.upper()`
5. 字符串是否全大写：`str.isupper()`
6. 字符串是否全小写：`str.islower()`
7. 字符串是否全字母：`str.isalpha()`
8. 字符串是否全数字：`str.isdigit()`
9. 字符串是否全字母或数字：`str.isalnum()`
10. 函数传参：Python 中所有参数都是**对象引用传递**，但对于不可变对象（如数字、字符串、元组），函数内无法修改原对象；对于可变对象（如列表、字典），函数内可以修改原对象的内容

# 第 12 课 位置互换

1. `a, b = b, a` 交换两个变量的值

# 第 13 课 链表的基础操作 I

1. Python 中类的定义使用大驼峰命名方式。

# 第 14 课 链表的基础操作 II

pass

# 第 15 课 链表的基础操作 III

pass

# 第 16 课 出现频率最高的字母

pass

# 第 17 课 判断集合成员

1. 列表转换成集合 `set(list)`
2. 集合用来判断元素是否存在，或者用来去重
3. 集合的操作：`set1 | set2` 并集，`set1 & set2` 交集，`set1 - set2` 差集
4. 添加元素：`set.add(x)`
5. 删除元素：`set.remove(x)` 或者 `set.discard(x)`，后者不关心是否存在，不存在社不报错
6. 集合长度：`len(set)`
7. 清空集合：`set.clear()`
8. 遍历集合：`for x in set:`

# 第 18 课 开房门

1. Python 使用字典实现 C++ 的 map，而 Python 的 map 另有作用，不要搞混
2. 字典的定义：`dict = {key1: value1, key2: value2, ...}`
3. 添加元素：`dict[key] = value`
4. 更新元素：`dict[key] = value`
5. 删除元素：`del dict[key]`
6. 清空字典：`dict.clear()`
7. 删除字典：`del dict`
8. 判断元素是否存在：`key in dict`
9. 字典键列表：`dict.keys()`
10. 字典值列表：`dict.values()`
11. 字典键值对列表：`dict.items()`
12. 遍历字典：`for key, value in dict.items():`
13. 上述 `dict.keys()` 和 `dict.values()` 返回的是迭代器，需要用 `list()` 转换成列表

# 第 19 课 洗盘子

1. Python 栈可以直接使用 list 模拟：`stack = []`
2. 栈的常用操作：`stack.append(x)` 入栈，`stack.pop()` 出栈，`stack[-1]` 获取栈顶元素

# 第 20 课 排队取奶茶

1. Python 队列可以直接使用 list 模拟：`queue = []`
2. 队列的常用操作：`queue.append(x)` 入队，`queue.pop(0)` 出队，`queue[0]` 获取队首元素

# 第 21 课 图形的面积

1. 使用 `__name` 表示隐藏属性
2. 使用 `class Circle(Shape):` 表示继承
3. 使用 `super().__init__(x, y)` 表示调用父类构造函数