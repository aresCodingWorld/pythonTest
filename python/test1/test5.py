#-*- coding:utf-8 -*-
age = raw_input("年龄 ? ")
height = raw_input("身高 ? ")
weight = raw_input("体重 ? ")

char = "我要转码！"
print char.decode("UTF-8")

print "所以，您现在的年龄是 %r 岁,身高是 %r cm，体重为 %r KG. " % (
	age,height,weight
	)