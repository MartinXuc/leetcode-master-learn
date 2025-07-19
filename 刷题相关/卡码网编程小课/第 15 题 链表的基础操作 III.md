[TOC]

# 题目描述

**题目描述**

请编写一个程序，实现以下链表操作：构建一个单向链表，链表中包含一组整数数据。

1. 实现在链表的第 n 个位置插入一个元素，输出整个链表的所有元素。
2. 实现删除链表的第 m 个位置的元素，输出整个链表的所有元素。

要求：

1. 使用自定义的链表数据结构。
2. 提供一个 linkedList 类来管理链表，包含构建链表、插入元素、删除元素和输出链表元素的方法。
3. 在 main 函数中，创建一个包含一组整数数据的链表，然后根据输入的 n 和 m，调用链表的方法插入和删除元素，并输出整个链表的所有元素。

**输入描述**

每次输出只有一组测试数据。

每组的第一行包含一个整数 k，表示需要构建的链表的长度。

第二行包含 k 个整数，表示链表中的元素。

第三行包含一个整数 S，表示后续会有 S 行输入，每行两个整数，第一个整数为 n，第二个整数为 x ，代表在链表的第 n 个位置插入 x。

S 行输入...

在 S 行输入后，后续会输入一个整数 L，表示后续会有 L 行输入，每行一个整数 m，代表删除链表中的第 m 个元素。

L 行输入...

**输出描述**

包含多组输出。

每组第一行输出构建的链表，链表元素中用空格隔开，最后一个元素后没有空格。

然后是 S 行输出，每次插入一个元素之后都将链表输出一次，元素之间用空格隔开，最后一个元素后没有空格；

如果插入位置不合法，则输出“Insertion position is invalid.”。

然后是 L 行输出，每次删除一个元素之后都将链表输出一次，元素之间用空格隔开，最后一个元素后没有空格；如果删除元素后链表的长度为0，则不打印链表。

如果删除位置不合法，则输出“Deletion position is invalid.”。

如果链表已经为空，执行删除操作时不需要打印任何数据。

**输入示例**

```
5
1 2 3 4 5
3
4 3
3 4
9 8
2
1
0
```

**输出示例**

```
1 2 3 3 4 5
1 2 4 3 3 4 5
Insertion position is invalid.
2 4 3 3 4 5
Deletion position is invalid.
```

**提示信息**

链表为空的时候，不打印

# 我的代码（有 bug， 还不能 ac，暂时无法解决）

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkList:
    def __init__(self):
        self.length = 0
        self.head_node = None

    # 获取下标为 n 的节点
    def get(self, n):
        current_node = self.head_node
        for _ in range(n):
            current_node = current_node.next
        return current_node

    # 在下标 n 处插入
    def insert(self, n, data):
        if n > self.length or n < 0:
            print("Insertion position is invalid.")
            return False
        new_node = Node(data)
        if self.length == 0:
            self.head_node = new_node
        elif n == 0:
            new_node.next = self.head_node.next
            self.head_node = new_node
        else:
            pre_node = self.get(n - 1)
            new_node.next = pre_node.next
            pre_node.next = new_node
        self.length += 1
        return True

    # 在第 n 个位置插入
    def insert_p(self, n, data):
        return self.insert(n - 1, data)
    
    # 删除下标为 n 的元素
    def delete(self, n):
        if n >= self.length or n < 0:
            print("Deletion position is invalid.")
            return False
        if n == 0:
            self.head_node = self.head_node.next
        else:
            pre_node = self.get(n - 1)
            if pre_node.next is None:
                return False
            pre_node.next = pre_node.next.next
        self.length -= 1
        return True

    # 删除第 n 个元素
    def delete_p(self, n):
        return self.delete(n - 1)
    
    # 输出链表
    def print_list(self):
        if self.length == 0:
            return
        current_node = self.head_node
        while current_node.next is not None:
            print(current_node.data, end=' ')
            current_node = current_node.next
        print(current_node.data)

# 创建初始链表
k = int(input())
elements = list(map(int, input().split()))
link_list = LinkList()
for data in elements:
    link_list.insert(link_list.length, data)

# 插入操作
S = int(input())
for _ in range(S):
    n, x = map(int, input().split())
    if link_list.insert_p(n, x):
        link_list.print_list()

# 删除操作
L = int(input())
for _ in range(L):
    m = int(input())
    if link_list.delete_p(m):
        link_list.print_list()
            
```

# 编程小课

## 前言

在前两个章节中，我们学习了如何往链表的尾部添加节点以及打印链表的第 m 个节点，如果只是往链表的尾部添加节点，那链表和数组也没有什么差异了，之前我们也提到过，往数组的中间插入一个元素，后续所有元素都需要往后挪动一位，而链表则不必这么麻烦，那往链表的中间添加或者删除一个节点具体应该怎么做呢？

## 插入链表的过程

![](assets/第%2015%20题%20链表的基础操作%20III/image-20231106144313232.png)

我们可以假设这样一个场景：在传递情报过程中，A 的下线是 B , 也就是 `A.next = B` , 现在我们要引入一个 C 充当 A 和 B 之间的中间人，新的关系是 A 的下线是 C , C 的下线是 B，我们可以直接将 C 的 `next` 指向 B，但是 B 无法直接表示，之前是用 `A.next` 来表示 B 的，即 `C.next = A.next` , 然后再将 A 的 `next` 指向 C , 即 `A.next = C`，这样就将新的关系构建完成了。

在链表中，具体插入的过程如下：

- 如果要在头节点处插入新的节点 (新的节点成为头节点)：
  - 新节点的 `next` 指针指向原来的头节点： `new_node.next = head_node`
  - 新节点成为新的头节点 `head_node = new_node`
  - 链表长度 + 1
- 如果要在非头节点处插入新的节点
  - 找到要插入的位置的前一个节点，将之命名为 `pre_node`
  - 将新节点的 `next` 指针指向 `pre_node` 的 `next` 指针，即 `new_node.next = pre_node.next`
  - 将 `pre_node` 的 `next` 指针指向新节点，即 `pre_node.next = new_node`
  - 链表长度 + 1

这样就完成了链表节点的插入过程。转换成代码如下：

```python
# 在第 n 个位置插入元素
def insert_at(self, n, data):
    new_node = Node(data)
    if n == 1:  # 头节点的情况
        new_node.next = self.head_node # 新节点的 next 指向原来的头节点
        self.headNode = new_node #  新节点成为新的头节点
        self.length += 1 # 链表长度 + 1
        return new_node
    else:  # 不是头节点的情况
        pre_node = self.get(n - 1) # 使用 get 方法获取要插入位置的前一个节点，命名 pre_node
        if pre_node is not None:
            new_node.next = pre_node.next # 将新节点的 next 指针指向 pre_node 的 next 指针
            pre_node.next = new_node # 将 pre_node 的 next 指针指向新节点
            self.length += 1 # 链表长度 + 1
            return new_node
    return None
```

## 删除链表的过程

删除链表的过程同样要区分是否有头节点

- 如果链表不存在头节点：表示链表为空，返回 `None`
- 如果链表存在头节点 (链表不为空)，要删除头节点
  - 新的头节点指向当前头节点的 `next` 节点
  - 链表长度 - 1

![](assets/第%2015%20题%20链表的基础操作%20III/image-20231106145339998.png)

- 如果链表存在头节点，要删除非头节点
  - 找到删除节点的前一个节点`pre_node`
  - 并将其`next` 指针设置为指向下下个节点，从而跳过了下一个节点，实现了节点的删除操作。
  - 链表长度 - 1

![](assets/第%2015%20题%20链表的基础操作%20III/image-20231106145711342.png)

```python
def delete(self, n):
    if self.headNode is None:  # 判断头节点是否还存在, 即链表是否为空链表
        return None
    if n == 1:  # 如果要删除头节点
        deleted_node = self.headNode
        self.headNode = self.headNode.next # 当前头节点的下一个节点成为新的头节点
        self.length -= 1
        return deleted_node
    else: # 如果要删除的不是头节点
        pre_node = self.get(n - 1) # 找到要删除的前一个节点
        if pre_node is not None and pre_node.next is not None:
            deleted_node = pre_node.next 
            pre_node.next = pre_node.next.next # 跳过要删除的节点
            self.length -= 1 # 链表长度 -1
            return deleted_node # 返回要删除的节点
    return None
```

## 代码编写

首先，需要接收整数 k , 表示需要构建链表的长度，然后我们获取输入的 k 个数字，将其插入到新构建的链表中。

```python
k = int(input()) # k 表示构建链表的长度
link_list = LinkList() # 新建一个链表
elements = list(map(int, input().split())) # 获取链表各位元素
for data in elements:
    link_list.insert(data) # 将输入插入到链表中
```

之后，需要接收一个整数 `s` 表示 `s` 行输入，每行两个整数，第一个整数为 n，第二个整数为 x，代表在链表的第 n 个位置插入 x。

```python
s = int(input()) #  整数 s 表示后续会有 s 行输入
for i in range(s):
    n, x = map(int, input().split()) # 在链表的第 n 个位置插入 x
    node = link_list.insert_at(n, x) # 插入链表时，成功插入返回对应的节点，否则返回 None
    if node is not None: # 成功插入后，打印链表
        link_list.print_link_list()
    else: # 插入位置不合法
        print("Insertion position is invalid.")
```

链表节点删除的前置步骤类型，需要接收一个整数 l，表示后续会有 l 行输入，每行一个整数 m，代表删除链表中的第 m 个元素。

```python
l = int(input()) # 整数 l 表示后续会有 l 行输入
for j in range(l):
    m = int(input()) # 在链表的第 m 个位置删除
    if link_list.delete(m) is not None: # 删除链表节点时，成功删除返回对应的节点，否则返回 None
        link_list.print_link_list() # 成功删除时，打印链表
    else: # 删除位置不合法
        print("Deletion position is invalid.")
```

完整的代码如下：

```python
# 定义链表节点
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
# 定义链表
class LinkedList:
    def __init__(self):
        self.head_node = None
        self.length = 0
    # 尾部插入方法
    def insert(self, data):
        self.length += 1
        new_node = Node(data)
        if self.head_node is None:
            self.head_node = new_node
            return self.head_node
        else:
            current_node = self.head_node
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node
            return new_node
    # 获取 第 n 个节点
    def get(self, n):
        if n < 1 or n > self.length:
            return None
        i = 1
        current_node = self.head_node
        while current_node is not None:
            if i == n:
                return current_node
            i += 1
            current_node = current_node.next
        return None
    # 在 提供的位置插入节点
    def insert_at(self, n, data):
        new_node = Node(data)
        if n == 1:
            new_node.next = self.head_node
            self.head_node = new_node
            self.length += 1
            return new_node
        else:
            pre_node = self.get(n - 1)
            if pre_node is not None:
                new_node.next = pre_node.next
                pre_node.next = new_node
                self.length += 1
                return new_node
        return None
    # 删除节点
    def delete(self, n):
        if self.head_node is None:
            return None
        if n == 1:
            deleted_node = self.head_node
            self.head_node = self.head_node.next
            self.length -= 1
            return deleted_node
        else:
            pre_node = self.get(n - 1)
            if pre_node is not None and pre_node.next is not None:
                deleted_node = pre_node.next
                pre_node.next = pre_node.next.next
                self.length -= 1
                return deleted_node
        return None
    # 打印链表节点
    def print_link_list(self):
        current_node = self.head_node
        while current_node is not None:
            if current_node.next is not None:
                print(current_node.data, end=' ')
            else:
                print(current_node.data)
            current_node = current_node.next

k = int(input())
# 新建链表
link_list = LinkedList()
elements = list(map(int, input().split()))
# 将元素插入到链表中
for data in elements:
    link_list.insert(data)

s = int(input())
for _ in range(s):
    n, x = map(int, input().split())
    # 在索引 n 处插入链表节点
    node = link_list.insert_at(n, x)
    if node is not None:
        link_list.print_link_list()
    else:
        print("Insertion position is invalid.")

l = int(input())
for _ in range(l):
    m = int(input())
    # 在索引 m 处删除链表节点
    deleted_node = link_list.delete(m)
    if deleted_node is not None:
        link_list.print_link_list()
    else:
        print("Deletion position is invalid.")
```

## 结语

本节课我们学习了在链表的中间插入和删除节点的过程，虽然代码有点多，但是只要理解了插入和删除过程，就很容易写出代码，这些操作在链表相关的题目中也是十分重要，大家一定要掌握好哦。