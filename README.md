# 跳一跳脚本
这是一个初级的跳一跳脚本，需要使用者手动选择落地的位置。
## 使用
要使用这个脚本需要
* python3
* flask
* PATH中有ADB

步骤
1. 将上面的依赖解决之后
2. 将Android设备连接上电脑，并开启调试模式
3. 打开跳一跳小游戏
4. 运行"WebPage.py"（需要指定监听的IP地址和端口），并用浏览器打开该IP地址和端口
5. 此时应该能看到游戏内的界面，用鼠标单击当前位置，再单击目标落地的位置，点击提交即可

## 原理
* 用flask与用户交互
* 获得用户两次点击的位置之后，计算出2D距离
* 代入之前获得的距离-按压时间的关系中，计算出需要按压的时间
* 用ADB模拟点按的操作