#coding:utf-8
l=5
import random
from time import sleep
print("欢迎使用加减法自定义生成器")
sleep(0.3)
q=0
m=100
print("---------------------------------------------------")
print("预备区块")
z=int(input("输入欲生成的题目数量:"))
l=int(input("请输入每题的时间:"))
g=int(input("请输入可能出现的最大值:"))
q=m/z
print("---------------------------------------------------")
print("开始生成！")

i=0
#加法模块
while i<z:
    x=str(random.randint(1,g/2))
    y=str(random.randint(1,g/2))
    print(x+"+"+y+"=")
    f=int(x)+int(y)
    qwq=("输入答案:")
    
    sleep(l)
    if qwq==f:
        print("哎呀，粗问题啦，请重试")
    else:
        print("时间到")
        print("本题答案是"+str(f)) 
        
        i=i+1
    sleep(0.2)
#减法模块
    x=str(random.randint(1,g/2))
    y=str(random.randint(1,g/2))
    while x<y:
        x=int(x)+random.randint(1,4)  
        #防止出现负数
        x=str(x)      
    print(x+"-"+y+"=")
    f=int(x)-int(y)
    qwq=("输入答案:")
    sleep(l)
    if qwq==f:
        print("哎呀，粗问题啦，请重试")
    else:
        print("时间到")
        
    print("本题答案是"+str(f)) 
    sleep(0.2)
    i=i+1
print("---------------------------------------------------")
print("程序自检")
print("已经生成"+str(z)+"道题目")
print("每题可得"+str(q)+"分")
time=int(input("请输入分数:"))
jiyi=100-time
print("今天推荐做"+str(jiyi)+"道题目")
print("---------------------------------------------------")
