# VSCode 配置 C / C++ 环境

1. 创建好一个空项目，然后在 vscode 中打开，然后打开终端
2. 创建文件 `cpp.code-workspace`
3. 输入 `g++ --version` 查看 clang 版本
4. 输入 `xcode-select --install` 安装 Xcode。
5. 安装 C/C++ 扩展，之后 reload xcode
6. 尝试在右上角点开运行，后面选择 g++ 来编译
7. 尝试在菜单栏选择 调试，然后还是选择 g++