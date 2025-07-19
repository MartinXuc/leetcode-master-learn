## 2 STL初识

### 2.1 STL的诞生

* 长久以来，软件界一直希望建立一种可重复利用的东西。
* C++ 的**面向对象**和**泛型编程**思想，目的就是**复用性的提升**。
* 大多情况下，数据结构和算法都未能有一套标准，导致被迫从事大量重复工作。
* 为了建立数据结构和算法的一套标准,诞生了**STL。**

### 2.2 STL基本概念

* STL (Standard Template Library，**标准模板库**)
* STL 从广义上分为: **容器(container)  算法(algorithm)  迭代器(iterator)**
* **容器** 和 **算法** 之间通过 **迭代器** 进行无缝连接。
* STL 几乎所有的代码都采用了 模板类 或者 模板函数。

### 2.3 STL六大组件

STL大体分为六大组件，分别是: **容器、算法、迭代器、仿函数、适配器（配接器）、空间配置器**

1. 容器：各种数据结构，如 `vector、list、deque、set、map` 等，用来存放数据。
2. 算法：各种常用的算法，如`sort、find、copy、for_each`等。
3. 迭代器：扮演了容器与算法之间的胶合剂。
4. 仿函数：行为类似函数，可作为算法的某种策略。
5. 适配器：一种用来修饰容器或者仿函数或迭代器接口的东西。
6. 空间配置器：负责空间的配置与管理。

### 2.4  STL中容器、算法、迭代器

#### 2.4.1 容器：置物之所

STL容器将运用**最广泛的一些数据结构**实现了出来。

常用的数据结构：数组、链表、树、栈、队列、集合、映射表 等。

这些容器分为**序列式容器**和**关联式容器**两种：

-   **序列式容器**：强调值的排序，序列式容器中的每个元素均有固定的位置。
-   **关联式容器**：二叉树结构，各元素之间没有严格的物理上的顺序关系。

#### 2.4.2 算法：问题之解

有限的步骤，解决逻辑或数学上的问题，这一门学科我们叫做算法 (Algorithms)。

算法分为：**质变算法**和**非质变算法**。

-   **质变算法**：是指运算过程中会更改区间内的元素的内容。例如拷贝，替换，删除等等。
-   **非质变算法**：是指运算过程中不会更改区间内的元素内容，例如查找、计数、遍历、寻找极值等等。

#### 2.4.3 迭代器：容器和算法之间粘合剂

提供一种方法，使之能够依序寻访某个容器所含的各个元素，而又无需暴露该容器的内部表示方式。

每个容器都有自己专属的迭代器。

迭代器使用非常类似于指针，初学阶段我们可以先理解迭代器为指针。

迭代器种类：

| 种类      | 功能                           | 支持运算                        |
| ------- | ---------------------------- | --------------------------- |
| 输入迭代器   | 对数据的只读访问                     | 只读，支持++、==、！=               |
| 输出迭代器   | 对数据的只写访问                     | 只写，支持++                     |
| 前向迭代器   | 读写操作，并能向前推进迭代器               | 读写，支持++、==、！=               |
| 双向迭代器   | 读写操作，并能向前和向后操作               | 读写，支持++、--，                 |
| 随机访问迭代器 | 读写操作，可以以跳跃的方式访问任意数据，功能最强的迭代器 | 读写，支持++、--、[n]、-n、<、<=、>、>= |

常用的容器中迭代器种类为双向迭代器，和随机访问迭代器，前面3种迭代器功能有些太少了，所以一般开发不使用。

### 2.5 容器算法迭代器初识

了解 STL 中容器、算法、迭代器概念之后，我们利用代码感受 STL 的魅力。

STL中最常用的容器为 Vector，可以理解为数组，下面我们将学习如何向这个容器中插入数据、并遍历这个容器。

#### 2.5.1 vector存放内置数据类型

- 容器：     `vector`
- 算法：     `for_each`
- 迭代器：  `vector<int>::iterator`

**示例：**

```C++
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
//vector 容器存放内置数据类型

void print(int x) {
    cout << x << endl;
}
void test01() {
    //创建了一个 vector 容器，数组
    vector<int> v;
    //向容器中插入数据
    v.push_back(10);
    v.push_back(20);
    v.push_back(30);
    v.push_back(40);
    //通过迭代起访问容器中的数据
    //起始迭代器  指向容器中第一个元素
    vector<int>::iterator itBegin = v.begin();
    //终止迭代器  指向容器中最后一个元素的下一个位置
    vector<int>::iterator itEnd = v.end();
    //第一种遍历方式(比较复杂)
    while (itBegin != itEnd) {
        cout << *itBegin << endl;
        ++itBegin;
    }
    //第二种遍历方式(比较常用)
    for (vector<int>::iterator it = v.begin(); it!=v.end(); ++it) {
        cout << *it << endl;
    }
    //第三种遍历方式（利用 STL 提供的算法 for_each）
    for_each(v.begin(), v.end(), print);
}

int main() {
    test01();
    return 0;
}
```



#### 2.5.2 Vector存放自定义数据类型

学习目标：vector中存放自定义数据类型，并打印输出

**示例：**

```c++
#include <iostream>
#include <string>
#include <vector>
using namespace std;
//vector容器中存放自定义数据类型
class Person{
public:
    Person(string name, int age){
        this->m_Name = name;
        this->m_Age = age;
    }
    string m_Name;
    int m_Age;
};
```

```cpp
void test01() {
    vector<Person> v;
    Person p1("aaa", 10);
    Person p2("bbb", 11);
    Person p3("ccc", 12);
    Person p4("ddd", 13);
    Person p5("eee", 14);
    v.push_back(p1);
    v.push_back(p2);
    v.push_back(p3);
    v.push_back(p4);
    v.push_back(p5);
    //遍历容器中的数据
    for (vector<Person>::iterator it = v.begin(); it != v.end(); ++it) {
        //cout << "姓名：" << it->m_Name << endl;
        //cout << "年龄：" << it->m_Age << endl;
        cout << "姓名：" << (*it).m_Name << endl;
        cout << "年龄：" << (*it).m_Age << endl;
    }
}
```

```cpp
//存放自定义数据类型的指针
void test02() {
    vector<Person*> v;
    Person p1("aaa", 10);
    Person p2("bbb", 11);
    Person p3("ccc", 12);
    Person p4("ddd", 13);
    Person p5("eee", 14);
    v.push_back(&p1);
    v.push_back(&p2);
    v.push_back(&p3);
    v.push_back(&p4);
    v.push_back(&p5);
    //遍历容器
    for (vector<Person*>:: iterator it = v.begin(); it != v.end(); ++it) {
        cout << "姓名" << (*it)->m_Name << endl;
        cout << "年龄" << (*it)->m_Age << endl;
    }
}
```

```cpp
int main() {
    test01();
    test02();
    return 0;
}
```



#### 2.5.3 Vector容器嵌套容器

学习目标：容器中嵌套容器，我们将所有数据进行遍历输出

**示例：**

```C++
#include <iostream>
#include <vector>
using namespace std;
//容器嵌套容器
```

```cpp
void test01() {
    vector<vector<int>> v;
    //创建小容器
    vector<int> v1;
    vector<int> v2;
    vector<int> v3;
    vector<int> v4;
    //向小容器中添加数据
    for (int i = 0; i < 4; i++) {
        v1.push_back(i+1);
        v2.push_back(i+2);
        v3.push_back(i+3);
        v4.push_back(i+4);
    }
    //将小容器插入到大容器中
    v.push_back(v1);
    v.push_back(v2);
    v.push_back(v3);
    v.push_back(v4);
    //通过大容器把所有数据遍历一遍
    for (vector<vector<int>>::iterator it = v.begin(); it != v.end(); ++it) {
        //(*it)是一个 vector<int> 容器
        for (vector<int>::iterator vit = (*it).begin(); vit != (*it).end(); ++vit) {
            cout << (*vit) << " ";
        }
        cout << endl;
    }
}
```

```cpp
int main() {
    test01();
    return 0;
}
```

