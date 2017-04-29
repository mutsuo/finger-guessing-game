# -*- coding:utf-8 -*-
# file: HelloGTK++.py
#
import pygtk           # 导入pygtk模块
pygtk.require('2.0')         # 设置pygtk所需的gtk版本
import gtk            # 导入gtk模块
class MyWindow():          # 定义窗口类
 def __init__(self, title, width, height):   # 定义初始化方法
  self.window = gtk.Window()      # 生成窗口对象
  self.window.set_title(title)     # 设置窗口标题
  self.window.set_default_size(width, height) # 设置窗口大小
  self.window.show()        # 显示窗口
 def main(self):          # 定义main方法
  gtk.main()          # 调用gtk.main方法
window = MyWindow('PyGTK', 300, 200)     # 创建窗口对象
window.main()           # 进入消息循环
