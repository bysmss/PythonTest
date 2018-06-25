# -*- coding: utf-8 -*-
"""
IDE:               PyCharm Community Edition
-------------------------------------------------
   Project Name:   PythonTest
   File Name：     1
   Description :
   Author :       Admin
   date:          2018-6-11
-------------------------------------------------
   Change Activity:
                   2018-6-11:
-------------------------------------------------
"""
##############################################运算符
'''
counter = 100          # 一个整型数
miles   = 999.99       # 一个浮点数
name    = "Maxsu"       # 一个字符串
print (counter)
print (miles)
print (name)
#多重赋值
a=b=c=1
a,b,c=1,"haha",23
#可以使用del语句删除单个对象或多个对象。
del a
#三种不同的数值类型 -
int(有符号整数)#10,-100,2×2
float(浮点实值)#1.16
complex(复数)#复数是由x + yj表示的有序对的实数浮点数组成，其中x和y是实数，j是虚数单位。45.j，3.14j
'''
#运算符
'''
1.算术运算符
2.比较(关系)运算符
3.赋值运算符
4.逻辑运算符
5.按位运算符
6.成员运算符
7.身份运算符
'''
#假设a与b为
a,b=10,4
##############################################1.算数运算符

print(a+b)#加法运算
print(a-b)#减法运算
print(a*b)#乘法运算
print(a/b)#除法运算
print(a%b)#取余数
print(a**b)#幂，表示a的b次方
print(4//3)#去除小数点后的数，但-11.0//3 = -4.0
##############################################2.比较(关系)运算符
if a==b:
    print("false")#是否相等
if a!=b:
    print("true")#是否不相等
if a>b:
    print("true")#a是否大于b
if a<b:
    print("false")#a是否小于b
if a>=b:
    print("true")#a是否大于等于b
if a<=b:
    print("false")#a是否小于等于b
##############################################3.赋值运算符
c=a+b#右侧分配给左侧c
c+=a#右侧数相加左侧数并分配给左侧等于c=c+a
c-=a#左侧数减去右侧数并分配给左侧等于c=c-a
c*=a#右侧数×左侧数并分配给左侧等于c=c*a
c/=a#左侧数/右侧数并分配给左侧等于c=c/a
c%=a#左侧数/右侧数的模数（余）并分配给左侧等于c=c%a
c**=a#执行指数(幂)计算，并将值分配给左操作数c=c**a
c//=a#运算符执行地板除运算，并将值分配给左操作数c=c//a
##############################################4.逻辑运算符
#布尔运算and or not
if (a+1>1) and  (b+1>2):
    print("条件1且条件二")
if (a+1>5) or (b+1>6):
    print("满足任何一个条件即可")
if not(8>a+1):
    print("相反条件，a+1不小于8的")
##############################################5.按位运算符
#内置函数bin()可用于获取整数的二进制表示形式。
#假设变量
a = 60            # 60 = 0011 1100
b = 13            # 13 = 0000 1101
print ('a=',a,':',bin(a),'b=',b,':',bin(b))
c = 0

c = a & b;        # 12 = 0000 1100
print ("result of AND is ", c,':',bin(c))#按位与

c = a | b;        # 61 = 0011 1101
print ("result of OR is ", c,':',bin(c))#按位并

c = a ^ b;        # 49 = 0011 0001
print ("result of EXOR is ", c,':',bin(c))#按位异或

c = ~a;           # -61 = 1100 0011
print ("result of COMPLEMENT is ", c,':',bin(c))#按位翻转

c = a << 2;       # 240 = 1111 0000
print ("result of LEFT SHIFT is ", c,':',bin(c))#左移运算符

c = a >> 2;       # 15 = 0000 1111
print ("result of RIGHT SHIFT is ", c,':',bin(c))#右移运算符
##############################################6.成员运算符 in not in
a6 = 10
b6 = 20
list = [1, 2, 3, 4, 5 ]
if(a6 in list):
    print("他在list中")#如果在list中找到a6返回True
else:
    print("他不在List中")#找不到返回false
if (b6 not in list):
    print("没在里面返回true")
else:
    print("在里面返回false")
##############################################7.身份运算符 is not is
a7=10
b7=10
if(a is b):#a，b指向的对象相同吗？
    print("true")#相同返回true，不同返回false
if(a not is b):#a，b指向的对象是否不相同？
    print("true")#不相同返回true，相同返回false
##############################################8.运算符优先级
'''
序号	  运算符     	描述
1	       **	   指数(次幂)运算
2       ~ + -	   补码，一元加减(最后两个的方法名称是+@和-@)
3    	* / % //	乘法，除法，模数和地板除
4	      + -	
5	       >> <<	  向右和向左位移
6        	&	      按位与
7	       ^ 	     按位异或和常规的“OR”
8      	<= < > >=	比较运算符
9	     <> == !=	等于运算符
10	 = %= /= //= -= += *= **=	赋值运算符
11	      is is not	身份运算符
12	     in not in	成员运算符
13    	not or and	逻辑运算符
'''
