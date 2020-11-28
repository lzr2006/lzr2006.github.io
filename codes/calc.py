#Play section photoelectric/Toys World Science and Technology Department
class calc:
    class info:
        def andder():
            print("计算加法...")
        def subber():
            print("计算减法...")
        def muller():
            print("计算乘法...")
        def divver():
            print("计算除法...")
        def __init__(*args):
            print("感谢使用我的计算器")
        def __del__(*args):
            print("离开...")
        def error():
            print("请不要乱输入!")
   
    class do:
        def andder(num1,num2):
            print(str(int(num1) + int(num2)))
        def sub(num1,num2):
            print(str(int(num1) - int(num2)))
        def mul(num1,num2):
            print(str(int(num1) * int(num2)))
        def div(num1,num2):
            print(str(int(num1) / int(num2)))
        
while 1:
    num1 = input("输入第一个数:")
    num2 = input("输入第二个数:")
    user = input("输入运算类型(加/减/乘/除)")

    if user == "加":
        calc.info.andder()
        calc.do.andder(num1,num2)
    elif user == "减":
        calc.info.subber()
        calc.do.sub(num1,num2)
    elif user == "乘":
        calc.info.muller()
        calc.do.mul(num1,num2)
    elif user == "除":
       calc.info.divver()
       calc.do.div(num1,num2)
    else:
        calc.info.error()
        break
   
