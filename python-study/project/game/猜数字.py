import random
guess_num = random.randint(0,100)
gusee_count = 0

while True:
    user_num = int(input("请输入一个数字\n"))

    gusee_count+=1

    if user_num == 10086:
        print(guess_num)
        continue
    
    if user_num < guess_num:
        print("小了")
    elif user_num > guess_num:
        print("大了")
    else:
        print(f"猜对了,你一共猜了{gusee_count}次")
        break