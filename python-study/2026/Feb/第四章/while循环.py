# whle循环的基本语法
i = 1

while i <= 100 :
    print(f"小明,我第{i}次操你妈!")
    i += 1

# while练习
total = 0
value = 1

while value <= 100 :
    total += value
    value += 1

print(f"1-100的和是:{total}")

# 案例二
import random
num = random.randint(1,100)
choice = True

print("猜数字游戏开始了!数字在1-100之间")

while choice:
    guess = int(input("请输入你猜的数字:"))

    if guess > num :
        print("猜大了")
    elif guess < num :
        print("猜小了")
    else:
        print("恭喜你,猜对了!")
        choice = False

# while循环嵌套
i = 1

while i <= 10:
    print(f"今天是我向小红告白的第{i}天") 
    j = 1

    while j <= 5:
        print(f"我今天送了小红{j}朵玫瑰花")
        j += 1
    
    i += 1

# 打印99乘法表
a = 1
b = 1

while a <= 9:
    while b <= a: 
        print(f"{b}x{a}={a*b} ",end="\t")
        b += 1
    
    a += 1
    b = 1
    print()

# end=""
print("Hello",end="")
print("World",end="")

# \t使用
print("Name\tAge\tGender")
print("-----------------------")
print("Tom\t18\tMale")
print("Lily\t17\tFemale")
print("Jack\t19\tMale")