[toc]

# Git 安装与配置

## 1 Linux 安装 Git

### 1.1 包管理器方式安装

#### Ubuntu 10.10(maverick) 或更新版本，Debain(squeeze) 或更新版本

```sh
sudo aptitude install git
sudo aptitude install git-doc git-svn git-email gitk
```

#### RHEL、Fedora、CentOS

```sh
yum install git
yun install git-svn git-email gitk
```

其中 git 软件包包含了大部分 Git 命令，是必须安装的软件包。

软件包 git-svn、git-email、gitk 本来也是 Git 软件包的一部分，但是因为有着不一样的软件包依赖（如更多的 perl 模组，tk 等），所以单独作为软件包发布。

### 1.2 源码安装

1. 访问 Git 的官方网站 http://git-scm.com/ ，下载 Git 源代码，例如：git-2.10.0.tar.gz
2. 展开源码包，并进入到相应目录

```sh
tar -jxvf git-2.19.0.tar.gz
cd git-2.19.0
```

3. 参照 INSTALL 文件进行安装，参照其中的指示安装。如下示例将 Git 安装在 `/usr/local/bin` 中

```sh
make prefix=/usr/local all
sudo make prefix=/usr/local install
```

4. 安装 Git 文档（可选）

```sh
make prefix=/usr/local doc info
sudo make prefix=/usr/local install-doc install-html install-info
```

### 1.3 命令补全

bash 可以使用 bash-completion 工具包完成命令补全功能，实现使用 TAB 键进行自动补全的功能。如下操作是将 git 相关的命令补全逻辑添加到 bash 中，这样就可以让 bash 支持 git 的自动补全了。

1. 将 Git 源码包中的命令补齐脚本复制到 bash-completion 对应的目录中去

```sh
cp contrib/completion/git-completion.bash /etc/bash_completion.d
```

2. 重新加载自动补齐脚本，使其在当前 shell 开始生效

```sh
. /etc/bash_completion
```

3. 配置启动时自动加载 bash_completion 脚本

```sh
# ~/.bash_profile
# /etc/bashrc

if [ -f /etc/bash_completion]; then
. /etc/bash_completion
fi
```

## 2 Windows 安装 git & TortoiseGit

目前 Git 提供 Windows 安装包自带 MinGW (Mininalist GUN for Windows，最简 GUN 工具集)，在安装后提供了一个 bash 的 shell 环境（Git Bash）和其他工具软件，组成了一个最简系统（Minimal System），这样可以保证在 Git Bash 中使用 git 命令和 Linux 环境下完全一致。

### 2.1 安装方式

1. 去官网下载 Windows 安装包（*.exe）
2. 对于 git-lfs 可以关注是否勾选
3. 选择默认编辑器时可以关注
4. 环境变量建议选择 “Use Git Bash Only”，避免与 Windows 环境产生修改
5. 安装完成后右键 `Git Bash Here`，输入 `git version` 检查是否完成安装

### 2.2 安装 TortoiseGit（小乌龟）

Windows 下一个比较热门的 git GUI 工具。

访问网站 https://tortoisegit.org/ 下载安装即可。

安装时客户端选择建议缺省使用内置 TortoisePLink。

## 3 Git 基础配置

### 3.1 基本配置

#### 系统配置

配置文件存放在 git 的安装目录下：`%GIT%/etc/gitconfig`，使用 `git config --system` 命令读写的就是这个文件。

#### 用户配置

配置文件存放在用户目录下：`~/.gitconfig`，使用 `git config --global` 命令读写的就是这个文件。

#### 仓库配置

当前仓库的配置文件：`%WORKSPACE%/.git/config`，使用 `git config --local` 命令读写的就是这个文件。

总体来说，三种配置从上到下是逐级继承的关系，若同一变量出现在两个配置中，更下层的会优先生效。

### 3.2 配置个人身份

首次使用 git 一定会需要配置自己的个人身份。

```sh
git config --global user.name "xc"
git config --global user.email "xc@bytedance.com"
```

这个配置信息在 git 仓库提交修改时体现。和 git 服务器认证使用的密码或者公钥无关，与统计贡献与责任追踪有关。

### 3.3 文本换行符配置

由于 Windows 上换行使用 CRLF，Linux 和 macOS 上换行使用 LF，产生了不一致的现象，因此需要使用 autocrlf 工具对换行符进行自动转换。

在 Windows 上，需要设置

```sh
git config --global core.autocrlf true
```

作用：拉取代码自动替换成 CRLF，提交代码自动替换成 LF。

在 Linux 或 macOS 上，设置

```sh
git config --global core.autocrlf input
```

作用：拉取代码时不转换，提交代码时如果有误写的 CRLF 则替换成 LF。

纯 Windows 开发则可以设置：

```sh
git config --global core.autocrlf false
```

### 3.4 文本编码设置

建议配置如下，防止各种原因导致的中文乱码

```sh
# 中文编码支持
git config --global gui.encoding utf-8
git config --global il8n.commitencoding utf-8
git config --global il8n.logoutputcoding utf-8
# 显示路径中的中文
git config --global core.quotepath false
```

### 3.5 git 与服务器的认证配置

#### http(s) 协议认证

```sh
# 设置口令缓存
git config --global credential.helper store
# 添加 HTTPS 证书信任
git config http.sslverify false
```

#### ssh 协议认证

SSH 协议是一种非常常用的 Git 仓库访问协议，使用公钥认证、无需输入密码，加密传输，操作便利又保证安全性。

相关命令

```sh
# 生成公钥
ssh-keygen -t rsa -C email-address
# 之后一直回车就行
```

