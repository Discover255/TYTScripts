import os, time
from sys import argv
import MyPythonTools

class Jump:

	current_OS = ''
	sizeX = 0
	sizeY = 0

	def getLastArgv(self):
		length = len(argv)
		return argv[length - 1]

	def jump(self,jump_time):
		jump_command = "adb shell input touchscreen swipe 0 0 0 0 " + str(jump_time)
		os.system(jump_command)
		sleep_time = (int(jump_time)/1000)+0.4
		time.sleep(sleep_time)
		self.screencap()

	def screencap(self):
		if self.current_OS == 'Windows':
			os.system('.\getScreen.bat')
		if self.current_OS == 'Unix-Like':
			os.system('sh getScreen.sh')

	def __init__(self):
		if MyPythonTools.isWindows:
			self.current_OS == 'Windows'
		if MyPythonTools.isPosix:
			self.current_OS == 'Unix-Like'
		sizeX, sizeY = MyPythonTools.getADBScreenSize()

	#不知道怎么去拟合，我觉得Logstic回归是个不错的曲线，用线性去拟合，最后发现整个s-t曲线是直线的。


if (__name__ == "__main__"):
	J = Jump()
	jump_time = J.getLastArgv()
	J.jump(jump_time)