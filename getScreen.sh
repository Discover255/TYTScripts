adb shell screencap -p | sed 's/\r$//' > screen.png
#执行adb shell 将\n转换\r\n, 因此需要用sed删除多余的\r