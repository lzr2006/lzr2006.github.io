import random
import time
today = [0,0] #玩家出生位置
to = [5,5] #追逐目标位置
crazy = [random.randint(0,4),random.randint(0,4)] #怪物出生位置
end3 = []
end1 = [] #读取存档用数据·
end2 = []
game = 0
class move():
    def left(*args):
        if today[0] < 1:
            print(f'您已经到达最左侧，当前位置为({today[0]},{today[1]})')
        else:
            today[0] = today[0] - 1
            print(f'移动成功，当前位置为({today[0]},{today[1]})')
    def right(*args):
        if today[0] > 4:
            print(f'您已经到达最右侧，当前位置为({today[0]},{today[1]})')
        else:
            today[0] = today[0] + 1
            print(f'移动成功，当前位置为({today[0]},{today[1]})')
    def forward(*args):
        if today[1] > 4:
            print(f'您已经到达最前端，当前位置为({today[0]},{today[1]})')
        else:
            today[1] = today[1] + 1
            print(f'移动成功，当前位置为({today[0]},{today[1]})')
    def back(*args):
        if today[1] < 1:
            print(f'您已经到达最后端，当前位置为({today[0]},{today[1]})')
        else:
            today[1] = today[1] - 1
            print(f'移动成功，当前位置为({today[0]},{today[1]})')
            
class toer:
    def __init__(*args):
        print('实例：目标创建完毕.')
    def do(*args):
        global go
        go = random.randint(1,4)
        if go == 1:
            if to[0] < 1:
                to[0] = to[0] + random.randint(1,2)
            else:
                to[0] = to[0] - random.randint(1,2)
        elif go == 2:
            if to[0] > 4:
                to[0] = to[0] - random.randint(1,2)
            else:
                to[0] = to[0] + random.randint(1,2)
        elif go == 3:
            if to[1] < 1:
                to[1] = to[1] + random.randint(1,2)
            else:
                to[1] = to[1] - random.randint(1,2)
        elif go == 4:
            if to[1] > 4:
                to[1] = to[1] - random.randint(1,2)
            else:
                to[1] = to[1] + random.randint(1,2)

    def crazy_do(*args):
        global cg
        cg = random.randint(1,4)
        toer.no_out()
        if cg == 1:
            if crazy[0] < 1:
                crazy[0] = crazy[0] + 1
            else:
                crazy[0] = crazy[0] - 1
        elif cg == 2:
            if crazy[0] > 4:
                crazy[0] = crazy[0] - 1
            else:
                crazy[0] = crazy[0] + 1
        elif cg == 3:
            if crazy[1] < 1:
                crazy[1] = crazy[1] + 1
            else:
                crazy[1] = crazy[1] - 1
        elif cg == 4:
            if to[1] > 4:
                crazy[1] = crazy[1] - 1
            else:
                crazy[1] = crazy[1] + 1

    def no_out(*args):
        #防止越界,同时为怪物的移动加入不确定性.
        if crazy[0] > 4:
            crazy[0] = crazy[0] - random.randint(1,3)
        if crazy[0] < 0:
            crazy[0] = crazy[0] + random.randint(1,3)
        if crazy[1] > 4:
            crazy[1] = crazy[1] - random.randint(1,3)
        if crazy[0] < 0:
            crazy[1] = crazy[1] + random.randint(1,3)
            
class admin():
    global game
    def game_win(*args):
        if today[0] == to[0] and today[1] == to[1]:
            print('恭喜您，取得了游戏的胜利。')
            game = 1
    def game_lost(*args):
        if today[0] == crazy[0] and today[1] == crazy[1]:
            print('很不幸，您被怪兽撞到了，游戏结束。')
            game = 1




                
print('欢迎来到追逐游戏 -- ToysWold Studio Inc.')
print('游戏帮助：在一个5*5的平面直角坐标系内，有你的追逐目标。你每回合可以选择移动或查看目标位置。')
print(f'提示：您的位置在(0,0);目标位置在(5,5);怪兽位置在({crazy[0]},{crazy[1]})')
while game == 0:
    i = input('请选择(前/后/左/右/目标/怪兽/读取存档/保存/退出)：')
    if i == '前':
        move.forward()
        admin.game_win()
        admin.game_lost()
    elif i == '后':
        move.back()
        admin.game_win()
        admin.game_lost()
    elif i == '左':
        move.left()
        admin.game_win()
        admin.game_lost()
    elif i == '右':
        move.right()
        admin.game_win()
        admin.game_lost()
    elif i == '目标':
        print(f'目标的位置在({to[0]},{to[1]})')
    elif i == '怪兽':
        print(f'怪兽的位置在({crazy[0]},{crazy[1]})')
    elif i == '退出':
        print('感谢您的游玩.\n\nToysWold Studio Inc.')
        break
    elif i == '读取存档':
        input('注意:请将存档文件放置在桌面上,完成后请按Enter继续...')
        try:
            f = open('C:\\Users\\Administrator\\Desktop\\MyGameesult.zzg','r')
            fr = f.read()
            use = fr.split('|')
            use1 = use[0]
            use2 = use[1]
            use3 = use[2]
            myaddress = use1.split(':')
            thisaddress = use2.split(':')
            thataddress = use3.split(':')
            address1 = myaddress[1]
            address2 = thisaddress[1]
            address3 = thataddress[1]
            end1.append(int(address1[1]))
            end1.append(int(address1[3]))
            end2.append(int(address2[1]))
            end2.append(int(address2[3]))
            end3.append(int(address3[1]))
            end3.append(int(address3[3]))
            print(f'读取结果：您的位置为({end1[0]},{end1[1]});目标位置:读取成功;怪兽位置:读取成功.')
            today[0] = end1[0]
            today[1] = end1[1]
            to[0] = end2[0]
            to[1] = end2[1]
            crazy[0] = end3[0]
            crazy[1] = end3[1] #166-170行用于读取存档
            f.close()
        except:
            print('读取存档失败!')
            
    elif i == '保存':
          f = open('C:\\Users\\Administrator\\Desktop\\MyGameesult.zzg','w')
          f.write('Myaddress:' + '[' + str(today[0]) + ',' + str(today[1]) + ']|' + 'Thisaddress:[' + str(to[0]) + ',' + str(to[1]) + ']|Thataddress:[' + str(crazy[0]) + ',' + str(crazy[1]) + ']') 
          f.close()
          print('保存成功!')
    toer.do()
    toer.crazy_do()
    admin.game_win()
    admin.game_lost()
