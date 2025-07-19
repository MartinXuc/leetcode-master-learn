[toc]

# Git 基本命令

## 1 前置概念

### 三大工程区域

Git  版本控制下的工程区域有 3 种：

1. **版本库（Repository）**

在工作区中有一个隐藏目录 `.git` 就是 Git 的版本库，里面存放了 Git  用来管理该工程的所有版本数据，也可以叫本地仓库。

2. **工作区（Working Directory）**

日常工作的代码文件或者文档所在的文件夹。

3. **暂存区（stage）**

一般存放在工程根目录 `.git/index` 文件中，所以我们也可以把暂存区叫做索引（Index）

### 三种文件状态

1. **已提交（committed）**

该文件已经被安全地保存在本地数据集中了

2. **已修改（modified）**

修改了某个文件，但是还没有提交保存

3. **已暂存（staged）**

把已修改的文件放在下次提交时要保存的清单中。

## 2 常用命令总览 (cheet-sheet)

### 工程准备

- 工程克隆—— `git clone`

### 查看工作区

- 查看工作区的修改内容—— `git diff`
- 查看工作区的文件状态—— `git status`

### 文件修改后提交推送

- 新增、删除、移动文件到暂存区—— `git add / git rm / git mv`
- 提交更改的文件—— `git commit`
- 推送远端仓库—— `git push`

### 查看日志

- 查看当前分支上的日志—— `git log`

### 分支管理

- 列出本地分支—— `git branch`
- 新建分支—— `git branch branch_name / git checkout -b branch_name`
- 删除分支—— `git branch -d`
- 切换分支—— `git checkout`
- 更新分支—— `git pull`
- 合并分支—— `git merge`

### 撤销操作

- 强制回退到历史节点——`git reset`
- 回退本地所有修改而未提交的—— `git checkout`

### 分支合并

- 合并目标分支内容到当前分支—— `git merge/git rebase`

## 3 命令讲解

### 3.1 工程准备 - git init & git clone

创建新仓库：

```sh
git init <project_name>
```

会在这里创建一个仓库，里面包含了 `.git` 文件夹，这个文件夹是 Git 用来管理该工程的所有版本数据，也可以叫本地仓库。

克隆远程仓库：

```sh
git clone <repository_url>
git lfs clone <repository_url>
```

有时候 `git clone` 会失败，因为 Git 默认会克隆所有文件，包括大文件，这时候可以使用 `git lfs clone` 来克隆。其中原因主要是 git lfs 对二进制文件进行了区别管理，与原来默认的 git 逻辑是不兼容的。

### 3.2 新增、删除、移动文件到暂存区 - git add / git rm / git mv

#### git add

对于新创建的，尚未被 git 跟踪的，需要先执行 `git add` 命令，将文件添加到暂存区，再执行提交。

如果文件已经被 git 追踪，即曾经提交过的，在早期版本的 git 中，需要 `git add` 再提交，现在可以直接提交。

#### git rm

`git rm` 将指定文件彻底从当前分支的暂存区删除，因此它从当前分支的下一个提交快照中被删除。如果一个文件被执行 `git rm` 后进行了提交，它将脱离 git 追踪，这个文件在之后的节点也不再受 git 工程的管理。

若将文件直接删除，然后再执行 `git commit`，命令，在后续版本该文件也会消失，实际效果与 `git rm` 一致。

#### git mv

`git mv` 命令用于移动或重命名一个文件。这是一个直接在暂存区和工作区同步操作的快捷命令。

### 3.3 查看工作区 - git diff / git status

#### git diff

`git diff` 用于比较项目中任意两个版本（分支）的差异，也可以用来比较当前索引和上次提交之间的差异。

```sh
# 比较两个节点间的差异
git diff <commit_id1> <commit_id2>

# 比较两个分支之间的差异
git diff <branch1> <branch2>

# 比较当前索引和上次提交之间的差异
git diff --cached

# git diff 后面可以加上 --name-status 参数，只显示文件名和状态
git diff <xxx> <xxx> --name-status
```

#### git status

`git status` 用于显示工作区、暂存区的文件状态。使用此命令可以看到修改的 git 文件是否被保存了，新增的文件是否纳入了 git 版本库的管理。

### 3.4 提交更改的文件 - git commit

`git commit` 主要是将暂存区里的文件改动提交到本地的版本库。这个动作是本地的动作，是往本地版本库中记录改动，不影响远端服务器。git commit 命令后可以加上 -m 参数，用来指定提交的注释：

```sh
git commit -m "commit message"
```

提交成功后，git 的日志可以查到此次提交的 id 和提交描述信息。

如果要一次性提交所有:

1. 在暂存区改动的文件
2. 所有已经跟踪却还未添加到暂存区的文件

到版本库，可以执行：

```sh
git commit -am "commit message"
```

修改最近一次提交的注释：`git commit --amend -m "new commit message"`

### 3.5 查看日志 - git log

git log 命令用于查看 git 的日志，可以查看提交的 id 和提交描述信息。

git log 配合不同的参数具有相当灵活强大的功能，例如：

```sh
# 查看提交历史
git log

# 查看最近 n 条提交记录
git log -n <number>

# 单行显示提交记录
git log --oneline

# 图形化显示分支合并历史
git log --graph --oneline --all

# 显示每次提交的详细修改内容
git log -p

# 显示每次提交的统计信息
git log --stat

# 按作者筛选提交记录
git log --author="author_name"

# 按日期范围筛选提交记录
git log --since="2023-01-01" --until="2023-12-31"

# 查看特定文件的提交历史
git log -- <file_path>

# 显示提交的简短哈希值和提交信息
git log --pretty=format:"%h - %an, %ar : %s"
```

常用的格式化选项：
- `%h`：提交的简短哈希值
- `%H`：提交的完整哈希值
- `%an`：作者姓名
- `%ae`：作者邮箱
- `%ad`：作者修订日期
- `%ar`：作者修订日期，按多久以前的方式显示
- `%s`：提交说明
- `%n`：换行符

初学者这里可以酌情跳过。

### 3.6 推送远端仓库 - git push

`git push` 用于将本地仓库的提交推送到远程仓库。

成功推送远端仓库后，其他开发人员可以获取到你新提交的内容，常用的推送命令格式：

```sh
git push origin branch_name
```

branch_name 决定了你的本地分支推送成功后，在远端服务器上的分支名，但本地分支名可以和远端分支名不一致，可以用下面的命令来实现：

```sh
git push origin branch_name:remote_branch_name
```

### 3.7 分支管理 - git branch & git checkout & git branch -d & git pull & git fetch

#### git branch

- `git branch` 用于查看本地工程的所有 git 分支名称。星号表示当前工作区所在分支。
- `git branch -r(emote)` 用于查看远端仓库所有 git 分支名称
- `git branch -a(ll)` 可以查看所有的分支，本地和远端都包含
- `git branch <branch_name>` 用于创建新分支。
- `git checkout -b <branch_name>` 用于创建并切换到新分支。
- `git branch -d <branch_name>` 用于删除本地分支。`-d` 换成 `-D` 可以强制删除，添加 `-r` 可以删除远端分支，删除完毕后需要 `git push origin :<branch_name>`
- `git branch -m <new_branch_name>` 用于重命名当前分支。
- `git branch -m <old_branch_name> <new_branch_name>` 用于重命名本地分支。

#### git checkout

- `git checkout <branch_name>` 可以用于切换分支。官方叫法为“检出”。
- `git checkout -b <branch_name>` 可以用于创建并切换到新分支。
- `git checkout -f` 可以用于强制切换分支。

#### git pull

`git pull` 用于从远端仓库拉取最新代码并合并到本地。

- `git pull` 拉取操作，使用默认仓库的默认分支
- `git pull <remote_name>` 拉取操作，指定远端仓库
- `git pull <remote_name> <branch_name>` 用于从远端仓库拉取最新代码并合并到本地，指定分支
- `git pull <remote_name> <remote_branch_name>:<local_branch_name>` 用于从远端仓库拉取最新代码并合并到本地，并指定远端分支和本地分支。

#### git fetch

`git fetch` 用于从远端仓库拉取最新代码，但不会合并到本地。

- `git fetch <remote_name>` 拉取远端仓库到本地。
- `git fetch <remote_name> <branch_name>` 拉取远端仓库到本地，并指定远端分支。
- `git fetch <remote_name> <remote_branch_name>:<local_branch_name>` 拉取远端仓库到本地，并指定远端分支和本地分支。

### 3.8 分支合并 - git merge & git rebase

#### git merge

`git merge` 用于将指定分支合并到当前分支。会将指定分支与当前分支比较，找出二者最近的一个共同节点 base，之后将指定分支在 base 之后，分离的节点合并到当前的分支上。分支合并，实际上就是分支间差异提交节点的合并。如果涉及新的节点，则会产生新的提交节点。

- `git merge <branch_name>` 合并指定分支到当前分支。

#### git rebase

`git rebase` 用于将当前分支的提交节点，移动到指定分支的最新节点之后。与 merge 不同，rebase 会重写提交历史，使提交历史更加线性。

- `git rebase <branch_name>` 将当前分支的提交节点，移动到指定分支的最新节点之后。
- `git rebase --abort` 取消 rebase 操作，回到 rebase 前的状态
- `git rebase --continue` 解决冲突后继续 rebase 操作

### 3.9 撤销操作 - git reset & git checkout .

#### git reset

`git reset` 用于将当前分支的指针移动到指定节点，可以用这个命令来实现撤销修改的操作。

- `git reset <commit_id>`：仅移动分支指针到指定提交，保留暂存区和工作区的更改（等同于 `--mixed`，默认模式）。
- `git reset --hard <commit_id>`：移动分支指针，并清空暂存区和工作区的所有更改（不可恢复，谨慎使用）。
- `git reset --soft <commit_id>`：移动分支指针，保留暂存区和工作区的所有更改，所有修改会被标记为已暂存。
- `git reset --mixed <commit_id>`：移动分支指针，重置暂存区但保留工作区的更改（未暂存的修改会保留）。

#### git checkout .

`git checkout .` 用于撤销所有未提交的修改，将工作区恢复到最近一次提交的状态。相当于 `git reset --mixed HEAD`。
`git checkout <file_path>` 用于撤销指定文件的修改，将工作区恢复到最近一次提交的状态。