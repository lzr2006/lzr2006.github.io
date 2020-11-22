#双色球
import random
from time import sleep
try:
    print("开始抽奖:")
    print("红球:")
    red = [-1]   #防止重复
    for i in range(1,6):
        red_ball = random.randint(1,30)
        print(red_ball)
        red.append(red_ball)
        print(red)
        re = i
        sleep(3)
    print("-------")
    blue_ball = random.randint(1,10)
    print("蓝球:")
    sleep(5)    
    print(blue_ball)
except NameError:
    print("重复啦")
