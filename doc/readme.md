# QuickCmd

## 1 下载安装miniconda3、vscode安装python插件

## 2 python -m pip install --upgrade pip

## 3 修改为国内源

### 3.1 永久修改方法1

在用户目录创建 ~/.pip/pip.conf

```conf
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
```

### 3.2 永久修改方法2

powershell或CMD中输入命令：

```shell
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

## 4 python工作区

- 创建工作区文件夹
- 创建虚拟环境
    python -m venv .venv
- 打开终端，若有提示，输入以下命令
    set-executionpolicy remotesigned
- 选择本文件夹中的虚拟环境

## 5 配置Python环境

```shell
pip install pyside2
pip install pyinstaller
```

## 6 打包程序

```shell
pyinstaller -F -w .\src\quickcmd.py
```
