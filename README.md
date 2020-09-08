# Fuck_Campus-Network（中大南方）
>一键进行校园网认证，解放你的双手:grimacing:
<br>

## CHANGELOG:new:  
V1.1  
打包成exe文件，使用前无需配置python环境
<br><br>

## 下载  
[地址1](https://wwa.lanzous.com/iOErFgg95ne)  
[地址2](https://github.com/bqliang/Fuck_Campus-Network/releases/download/V1.1/Fuck_Campus-Network.-.V1.1.zip)  
<br>

## 使用方法
1. 下载压缩包，解压
2. 运行文件夹内的 ```点我配置信息.bat``` ，输入校园网账号密码，这时会在桌面生成一个快捷方式。
3. 同时按住 Win + R 键，输入 regedit ，点按确定，逐次找到  
   ```计算机\HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\NlaSvc\Parameters\Internet```  
   （你也可以按住 Ctrl + F 键，输入 EnableActiveProbing 进行搜索，搜索较慢，需耐心等待）  
   如图所示，双击右边窗口里的 EnableActiveProbing ，在数值数据中，输入0，默认值是1，确定。
   
   ![Image text](https://img-blog.csdn.net/20160511100609551)
   
4. 连接到校园网时，点击桌面的快捷方式 ```Wfif Con``` 自动进行认证
<br>

## 实现连接到 WiFi 自动执行认证操作
1. 右键“我的电脑”，点击```管理```
2. 在左栏选择```任务计划程序```
3. 点击右栏```创建任务```
4. 名称随便填
5. 切换到```触发器”```，点击```新建```，开始任务选择```发生事件时```
6. 点按```自定义``` -> ```新建事件筛选器```
7. 事件日志选择```应用程序与服务日志``` -> ```Microsoft``` -> ```Windows``` -> ```WLAN``` -> ```AutoConfig``` -> ```Operational```
8. 事件来源选择```WLAN-AutoConfig```
9. 所有事件id里输入数字```8001```
10. 切换到```XML```标签，勾选```手动编辑查询``` -> 在</Select>前增加代码```[EventData[Data[@Name='SSID']='NFU_Student']]```，点击确定返回上一层
11. 切换到```操作```标签栏，```新建``` -> ```浏览```,选择解压后文件夹内的```WifiAutoCon.exe```

![Image text](https://pic2.zhimg.com/80/v2-ab3248fc843aaa4a6a0e2f922794525a_720w.jpg?source=1940ef5c)
