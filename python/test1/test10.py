#-*- coding:utf-8 -*-
#导入包
from sys import argv
#从命令行接受参数
script,filename = argv
#打印文字
print "We're going to erase %r. " % filename
print "If you don't want that, hit CTRL-C (^C) ."
print "If you do want that, hit RETURN."
#接收键盘参数
raw_input ("?")

print "Opening the file........."
#目标文件打开。以写方式（W）
target = open(filename,'w')

print "Truncating the file. GoodBye! "
#将文件清空
target.truncate()

print "Now I'm going to ask you for three lines."
#页面输入3条语句
line_1 = raw_input("line 1 :")
line_2 = raw_input("line 2 :")
line_3 = raw_input("line 3 :")

print "I'm going to write these to the file.."

#将页面输入的3条语句内容写入目标文件。格式化
#target.write(line_1)
#target.write("\n")
#target.write(line_2)
#target.write("\n")
#target.write(line_3)
#target.write("\n")

target.write(line_1 + "\n" + line_2 + "\n" + line_3)

print "And finally, we close it."
#关闭文件
target.close()



