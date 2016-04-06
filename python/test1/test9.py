#-*- coding:utf-8 -*-
#导入包
from sys import argv
#从命令行接收参数
script, filename = argv
#打开命令行输入的制定的文本文件，该文件要和该.py文件在同一路径下
txt = open(filename)
#打印输入 这是你的文件： 文件名
print "Here's your file %r:" % filename
#打印读取的文件内容
print txt.read()
#打印文字显示
print "Type the filename again : "
#重新输入文件名
file_again = raw_input("> ")
#打开输入的文件
txt_again = open(file_again)
#打印输入的文件的文件内容
print txt_again.read()
