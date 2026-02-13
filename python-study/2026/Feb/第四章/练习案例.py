import random

money = 10000

for i in range(1,20+1):

    if money <= 0:
        print("工资发完了")
        break
    
    print(f"员工{i}",end=",")

    num = random.randint(1,10)
    print(f"绩效分{num}",end=",")

    if num < 5:
        print("低于5,不发工资,下一位.")
        continue
    else:
        money -= 1000
        print(f"高于5,发工资1000元,账户余额还剩余{money}元")
