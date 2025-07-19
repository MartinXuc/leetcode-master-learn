#### 1. 下载编辑器VScode

- 官网：https://code.visualstudio.com/

![](./assets/VScode%E4%B8%AD%E9%85%8D%E7%BD%AE%20C_C++%20%E7%8E%AF%E5%A2%83/VScode%E4%B8%AD%E9%85%8D%E7%BD%AE%20C_C++%20%E7%8E%AF%E5%A2%83.png)

- 安装VScode（建议附加任务全部勾选）

![](./assets/VScode%E4%B8%AD%E9%85%8D%E7%BD%AE%20C_C++%20%E7%8E%AF%E5%A2%83/VScode%E4%B8%AD%E9%85%8D%E7%BD%AE%20C_C++%20%E7%8E%AF%E5%A2%83.gif)

#### 2. 下载编译器MinGW并解压

- 官网页面：https://www.mingw-w64.org/
- 下载页面：https://sourceforge.net/projects/mingw-w64/files/
- 你可以进入官网自行寻找
- 你也可以直接点击为你找好的下载页面
- 下载页面中选择 `x86_64-win32-seh` 下载

![](./assets/VScode%E4%B8%AD%E9%85%8D%E7%BD%AE%20C_C++%20%E7%8E%AF%E5%A2%83/VScode%E4%B8%AD%E9%85%8D%E7%BD%AE%20C_C++%20%E7%8E%AF%E5%A2%83-1.png)

- 如果你因为网络环境限制无法下载
- 在C盘中解压文件

![](./assets/VScode%E4%B8%AD%E9%85%8D%E7%BD%AE%20C_C++%20%E7%8E%AF%E5%A2%83/VScode%E4%B8%AD%E9%85%8D%E7%BD%AE%20C_C++%20%E7%8E%AF%E5%A2%83-1.gif)

- 理论上你可以在任何地方解压，但注意路径不能包含中文，至于特殊字符请自行测试

#### 3. 将MinGW添加至环境变量

- 进入mingw64下的bin文件夹，复制当前路径，Win + i唤起系统设置，输入高级系统设置并进入，点击环境变量，选择path，编辑，新建，粘贴路径，按下三个确定

![](./assets/VScode%E4%B8%AD%E9%85%8D%E7%BD%AE%20C_C++%20%E7%8E%AF%E5%A2%83/VScode%E4%B8%AD%E9%85%8D%E7%BD%AE%20C_C++%20%E7%8E%AF%E5%A2%83-2.gif)

#### 4. 配置VScode插件

- 打开VScode安装插件 `Chinese` 和 `C/C++` ，等待安装完毕后重启VScode

![](./assets/VScode%E4%B8%AD%E9%85%8D%E7%BD%AE%20C_C++%20%E7%8E%AF%E5%A2%83/VScode%E4%B8%AD%E9%85%8D%E7%BD%AE%20C_C++%20%E7%8E%AF%E5%A2%83-3.gif)

#### 5. 运行代码

- 新建文件夹，修改为英文名称并进入，右键 `通过Code打开` 若在安装时未勾选相关选项，可能没有这个选项，请自行在VScode内操作打开文件夹
- 新建一个文件，英文命名且扩展名为 `.c`
- 编写相关代码

```Plaintext
#include <stdio.h> #include <stdlib.h> int main() { printf("Hello World!\n"); printf("你好世界！\n"); system("pause"); // 防止运行后自动退出，需头文件stdlib.h return 0; }
```

VScode菜单栏，点击运行，启动调试，稍等程序运行，输出结果在下方终端，上方调试面板，点击最右边的 `橙色方框` 停止程序运行。

#### 6. 调整和优化

点击右侧运行，会自动生成`task.json`文件（注意c使用gcc，c++使用g++），打开它，修改一下：

- “args”中的`"${file}$"`改成`*.c`或者`*.cpp`
- 下面`fileBasenameNoExtinsion....exe`修改成`a.exe`
- 打开调试，生成launch.json
- 点击右侧添加配置 (gdb)启动
- 修改程序名称为`"${filename}\\a.exe“`
- 修改MiDebuggerPath为mingw下gdb.exe

如下是我的示例（以C++为例）：

tasks.json

launch.json

#### 7. 提示

- 若源代码文件夹含有中文路径，将会无法编译程序。
- 若你的Windows用户名使用了中文，可能无法运行。