# 1. 走进HTML世界

## 1.1. HTML简介

>参考百度百科

## 1.2. 如何创建HTML文件

鼠标右键->新建文本文件->更改后缀名.html 

**创建文件所需要注意事项**

- 可以以中文命名，但是不允许使用中文（我）。
- 不允许使用特殊字符。
- HTML文件名推荐使用小写。
- 如果是多个单词创建的文件名，推荐使用驼峰命名法，每个单词首字母大写  HelloWorld
- 创建完HTML文件后依然是文本文件格式，那么需要将系统中隐藏已知文件类型扩展名勾选掉。

## 1.3. HTML标签相关

### 1.3.1 HTML标签

 标签是HTML的最基本的单位，也是最重要的组成部分，通常用两个角括号括起来得：”<" 和 “>”。

- 标签有两种形式：

  1. 成对标签(双标签)

     ```html
     <p>内容</p>
     ```

  2. 不成对标签(单标签)

     ```html
     <hr />
     ```

单标签中的`/`是标准语法，推荐加上。

### 1.3.2 HTML标签的大小写问题

标签是大小写无关的，与表示意思一样，推荐使用小写。

### 1.3.3 HTML标签属性

1. HTML属性一般都出现在HTML标签中，是HTML标签的一部分。
2. 标签可以有属性，包含了额外的信息，属性的值一定要在双引号中。而且标签还可以存在多个属性。
3. 一般属性由属性名和属性值成对出现，对于属性名只可能有1个属性值的情况，属性值可以省略不写。

- 语法：

```html
 <标签名 属性名1=“属性值” 属性名2=“属性值”></标签名>
```

### 1.3.4 HTML颜色值的设置

1. 浏览器都支持颜色名称集合，颜色值是一个关键字或者是一个RGB格式的数字，在网页中都用的很多。
2. 使用英文单词作为颜色值：
   - red 红色 | green 绿色 | blue 蓝色 | pink 粉色 | purple 紫色等。
3. 六位的十六进制颜色值：
   - `\#ff0000`  简写：`#f00`
   - 前两位表示红色，中间两位表示绿色，最后两位表示蓝色。

### 1.3.5 HTML注释

> 注释的内容不会被浏览器解释出来

注释的好处：

- 方便查找、比对、方便其他程序员快手了解你得代码、方便以后自己对自己代码理解和修改。
- 注释的内容不会被浏览器解析出来。
- 格式：

```html
<!--书写输入的内容-->
```

### 1.3.6 HTML的代码格式

- 任何回车或者空格在源代码中都不起作用，所以在编写HTML代码时，都可以使用回车或者空格进行代码排版，这样可以使代码清晰便于团队合作，必须保持严格的缩进规则，缩进以tab键为准。
- 任何的回车或者空格或者tab键在内容当中只会被解析为一个小空格。

### 1.3.7 HTML实体字符

```html
&nbsp; 空格
&gt; <
&lt; >
&copy; 版权符号©
```

在网页中显示这些字符的时候，必须使用实体字符。

## 1.4. HTML主体结构

```html
<!DOCTYPE html> <!--声明头-->
<html>
  <!--头标签-->
  <head>
  </head>
  <!--体标签-->
  <body>
  </body>
</html>
```

1. 最顶部声明

   ```
   <!DOCTYPE html>
   ```

   - 声明是文档的第一成份，位于文档的最顶部。
   - 该标签就是告诉浏览器所使用的HTML规范。

2. 以开始，以结束，中间包含头部标签及主体标签

## 1.5. `<head>`标签中常用的标签

```html
<head lang="en">
  <!--
    lang是language的意思,lang="en" 属性对页面声明主要语言，en表示英文，zh-cn表示中文。
    搜索引擎不会判断该站点是中文还是英文，它让搜索引擎知道你得站点是中文站，这些都是HTML规范，越规范，越容易被收录
    -->
<title></title>设置页面字符串
<meta charset="utf-8" /> 设置页面字符集
<meta http-equiv="content-type" content="text/html;charset=utf-8" />设置页面字符集（HTML4）
<!--
    .html text/html  指的是文件mime类型
    .css  text/css
    .jpg  image/jpeg
    .jpeg  image/jpeg
    .png   image/png
    .gif   image/gif
    www.baidu.com  文件mime类型
-->
<!--http-equiv 告知浏览器的行为-->
<meta http-equiv="refresh" content="5;url=https://www.lmonkey.com" /> 设置5秒后自动跳转到学习猿地
<meta http-equiv="refresh" content="5" />设置浏览器5秒刷新一次
<!--name 告知浏览器的内容-->
<meta name="keywords" content="关键字1,关键字2"/> 设置网站关键字，多个关键字之间用英文状态下的逗号分割
<meta name="description" content="描述的内容" />设置网站的描述
<link />定义两个文档之间连接的关系
<!--
    rel = "表示文档与被连接文档之间的关系"
    type = "被连接文档的类型"
    href = "被连接文档的地址"
-->
<link rel="icon" type="" href=""/>加载标题icon图标
<!--了解级别-->
<link rel="stylesheet" type="text/css" href="" />加载CSS样式
<style></style> 加载CSS样式
<script></script> 加载JS脚本
<!--阻止移动浏览器自动调整页面大小-->
<meta name="viewport" content="initial-scale=2.0,width=device-width" />
<!--
    name = "viewport" 说明此meta标签定义视口的属性
    initial-scale = 2.0 意思是将页面放大两倍
    width = device-width 告诉浏览器页面的宽度的能与设备的宽度
-->
<meta name="viewport" content="width=device-width,maximun-scale=3,minimum-scale=0.5" />
<!--允许用户将页面最大放大至设备宽度3倍，最小压缩至设备宽度的一半-->
<meta name="viewport" content="initial-scale=1.0,user-scalable=no" />
<!--禁止用户缩放，可以在混合APP时，为了使html页面更逼真，使页面无法缩放。user-scalable=no是禁止缩放-->
```
