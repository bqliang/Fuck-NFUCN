# Fuck_Campus-Network（中大南方）

一键进行校园网认证，解放你的双手


#### 环境依赖

* Win 7+
* [python 3.6+](https://www.python.org/downloads/)
* python request库


#### 环境配置
>（出现问题请使用搜索引擎寻求解决办法）

1. 下载 python 安装

2. 使用 ```pip install requests``` 命令安装 request 模块


#### 使用方法

1. 下载压缩包，解压
2. 运行文件夹内的 ```点我配置信息.bat```
3. 同时按住 Win + R 键，输入 regedit ，点按确定，逐次找到 
   ```计算机\HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\NlaSvc\Parameters\Internet``` 
   如图所示，双击右边窗口里的 EnableActiveProbing ，在数值数据中，输入0，默认值是1，确定。
   ![Image text](https://img-blog.csdn.net/20160511100609551)
   
4. 连接到校园网时，点击桌面的快捷方式 ```Wfif Con```

