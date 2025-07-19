## git install

### Linux 

```bash
# Debian-based distribution
sudo apt install git

# Fedora
sudo yum install git

# Arch
sudo pacman -S git
```

### MacOS

```zsh
# MacPorts
sudo port install git

# Homebrew
brew install git
```

### Windows

Download installer.exe for Windows.

## git 传输协议

### https

### ssh

免密，推荐。

1. 生成 ssh 密钥对：

```sh
ssh-keygen -t rsa
```

2. 将 `id_rsa.pub` 公钥传入到 github / gitee
3. 验证 ssh 是否已经正确添加

```sh
ssh -T git@github.com
# or
ssh -t git@gitee.com
```

## help documents

### tldr(更简短)

```sh
# get common usage on git diff
tldr git-diff
```

### man

```sh
# get all available information on 'git status'
git status --help # same as 'man git-status'
# get a quick help on 'git checkout'
git checkout -h
```

## start git

```sh
mkdir {my-project}
cd {my-project}
git init
```

```sh
git config user.name "sadads"
git config user.email "xxxx@xxx"
cat .git/config
```

```sh
# 查看当前项目工作状态
git status
```

```sh
touch README.md
vim README.md
git add README.md
git commit -m "added README.md"
```

## push to origin

在 github / gitee 上创建一个新仓库。

```sh
git remote add origin {remote_url}

# if you want to change
git remote set-url origin {remote_url}

# show a list of existing remotes
git remote -v
```

```sh
git push {remote_name:origin} {local_branch_name}
git push --upstream origin master
```

