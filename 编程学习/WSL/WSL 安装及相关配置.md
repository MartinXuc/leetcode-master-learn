## WSL 1 和 2 的区别

![](assets/WSL%20安装及相关配置/20250511113733.png)

WSL 1 实际上就是一个翻译层，WSL 2 基于 Hyper-v 虚拟化平台，Windows 和 Linux 处于平级关系，wsl 有自己独立的内核。

## 前置步骤

- 开启 CPU 虚拟化，可以打开任务管理器查看状态
  - 开启需要打开 BIOS：
    - Intel (VMX) Virtualization
    - AMD-v
- 开启 Windows 功能：
  - 适用于 Linux 的 Windows 子系统
  - 虚拟机平台

## 安装 WSL

### 默认方式

管理员身份运行 CMD。

- `wsl --update`
- `wsl --install [--web-download]`

之后进入 wsl 设置用户名和密码

- `wsl -d [name]`

### 自定义方式

可以查看所有的 wsl 发行版本，然后自定义安装（上面的安装就是默认的 Ubuntu）

- `wsl --list --online`
- `wsl --install <name> [--web-download]`

## 启动停止

- 查看已安装的 wsl 子系统列表：`wsl -- list -v`
- 切换默认的 wsl 子系统：`wsl --set-default <name>`
- 命令行方式启动 wsl：`wsl -d <name>`
  - Windows Terminal 可以使用图形化方式启动，只需要在上方标签页上操作即可-
- 停止运行 wsl：`$exit`

## 卸载与备份

- 卸载子系统命令：`wsl --unregister <name>`
- 备份子系统：`wsl --export <name> <tar—name>`
- 恢复子系统：`wsl --import <name> <os_path> <tar_name>`

## 文件共享

### 在 WSL 中查看 Windows 文件

- 查看系统的硬盘空间：`df -h`
  - Windows 里的硬盘目录会直接挂载在这里，但是实际 IO 性能一般，如果 IO 需求量大的话应当将整个项目迁移到 WSL 内部空间。

### 在 Windows 中查看 WSL 文件

- 在 资源管理器 中，左栏下方的 Linux 下方就有网络方式挂载的一些磁盘。

## 一些黑科技

### 命令混用

WSL 允许在 Linux 里直接运行 Windows 程序。

例子：

```sh
# 在 Linux 中调用 Windows 记事本编辑文件
notpad.exe <file_path>

# 在 Linux 中调用 Windows 资源管理器
explorer.exe <dir_path>
```

### WSLg1

允许 Linux 里带图形界面的应用程序直接以 Windows 窗口的形式打开，利用了 RDP 远程桌面协议。

## 显卡直通

可以使用 `nvidia-smi` 在 WSL 中查看显卡信息。

