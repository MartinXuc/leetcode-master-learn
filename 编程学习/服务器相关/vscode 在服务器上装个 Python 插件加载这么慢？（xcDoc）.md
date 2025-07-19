## 前言

不知道大家开发过程中有没有遇到服务器死活装不上插件的问题，反正我是遇到很多次了，参加 wiki 已有的方法去点击一个小图标将本地插件复制到远程服务器，发现还是解决不了这个问题。但是遇到问题不能就这么算了，研究了一会儿还是搞定了，现在将我的方法分享出来：

最近开发过程中经常遇到在服务器上装不了 Python 插件的问题，网上一查发现和我一样的人不在少数，主要还是网络配置问题。不过我不打算去搞网络，而是用另一个方法规避问题，那就是离线安装！

## 步骤

### 1 找到对应安装包的 vsix 资源

微软政策最近在收紧，所有的插件都没办法从官方网站或者 vscode 里直接导出 vsix 格式的安装包了，只能用点“旁门左道”来**搞到插件安装包**。

这里找到了一个微软**官方直链下载**的方式，替换其中的包名和版本号就可以直接下载，可以保证下载的是**安全**的文件。暂时还不知道多久之后会被 ban 掉。如果想要指定版本请**自行替换**。

#### Python 插件链接

```
https://marketplace.visualstudio.com/_apis/public/gallery/publishers/ms-python/vsextensions/python/2024.2.1/vspackage
```

#### Pylance 插件链接

```
https://marketplace.visualstudio.com/_apis/public/gallery/publishers/ms-python/vsextensions/vscode-pylance/2024.3.2/vspackage
```

#### Python Debugger 插件链接

```
https://marketplace.visualstudio.com/_apis/public/gallery/publishers/ms-python/vsextensions/debugpy/2024.0.0/vspackage?targetPlatform=linux-x64
```

### 2 将 vsix 包复制到服务器里

具体方式就不说了，注意传文件的合规要求，别被系统掐掉了。（已知 scp 方式传到 90 绿区服务器会被掐掉）

### 3 vscode 上安装插件

1. 连接到服务器，先找到 `.vscode-server/extensions` 路径，把里面原来的东西全删掉，防止以前的旧插件弄冲突了。
2. 左侧打开插件栏目，右上角三个点，选择 `Install from VSIX...`
3. 找到对应的包进行安装