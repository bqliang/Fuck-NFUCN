# Fuck NFU Campus Network :globe_with_meridians:
# 中大南方校园网自动登录
>一键进行校园网认证，解放你的双手:grimacing:  [实现效果](https://wx1.sinaimg.cn/large/006aTw3Zgy1gijla8yn6qg31e00qd4qr.gif)
<br>

## :new: CHANGELOG  
V1.3  
添加登录结果通知
使用线程
一些难以描述的优化

V1.2  
解决自动化无效的bug  
  
V1.1  
打包成exe文件，使用前无需配置python环境
<br><br>

## :arrow_down: 下载  
[地址1（推荐）](https://wwa.lanzous.com/iXcmJgt5vmd)  
[备用地址](https://github.com/bqliang/Fuck_Campus-Network/releases/download/V1.2/Fuck_Campus-Network-V1.2.zip)  
<br>

## :u7981: 使用方法  
1. 下载压缩包，解压
2. 运行文件夹内的 ```点我配置信息.bat``` ，输入校园网账号密码，这时会在桌面生成一个快捷方式。
3. 同时按住 Win + R 键，输入 regedit ，点按确定，逐次找到  
   ```计算机\HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\NlaSvc\Parameters\Internet```  
   （你也可以按住 Ctrl + F 键，输入 EnableActiveProbing 进行搜索，搜索较慢，需耐心等待）  
   如图所示，双击右边窗口里的 EnableActiveProbing ，在数值数据中，输入0，默认值是1，确定。
   
   ![Image text](https://img-blog.csdn.net/20160511100609551)
   
4. 到目前为止，程序已可用，连接到校园网时，点击桌面的快捷方式 ```Wfif Con``` 即可自动进行认证。如果你想要全自动化，你可能需要再花费一点时间阅读以下内容。
<br>

## :arrows_counterclockwise: 实现连接到 WiFi 自动执行认证操作  
1. 右键“我的电脑”，点击```管理```
2. 在左栏选择```任务计划程序```；点击右栏```创建任务```
3. 名称随便填
4. 切换到```触发器```选项卡，点击```新建```，开始任务选择```发生事件时```
5. 点按```自定义``` -> ```新建事件筛选器```
6. 事件日志选择```应用程序与服务日志``` -> ```Microsoft``` -> ```Windows``` -> ```WLAN``` -> ```AutoConfig``` -> ```Operational```；事件来源选择```WLAN-AutoConfig```；所有事件id里输入数字```8001```
7. 切换到```XML```选项卡，勾选```手动编辑查询``` -> 在```</Select>```前面增加代码```[EventData[Data[@Name='SSID']='NFU_Student']]```，点击确定返回上一层
8. 切换到```操作```选项卡，```新建``` -> ```浏览```,选择解压后文件夹内的```自动化选我.exe```，最后一路确认。

![Image text](https://pic2.zhimg.com/80/v2-ab3248fc843aaa4a6a0e2f922794525a_720w.jpg?source=1940ef5c)  
<br>

## :love_letter: 联系方式  
:four_leaf_clover: 微信：```iwaslbq``` （请不要为了咨询怎么使用而给我发送消息，师妹除外）  
:mailbox_with_mail: 电子邮箱：```bqliang@outlook.com```<br><br>

## :interrobang: Android版什么时候会有？  
你看这个鸽子，它又大又白...咕咕咕 🕊️
<br><br>

## :interrobang: iOS版什么时候会有？  
不可能会有的，除非你送我一台最新的iPhone

