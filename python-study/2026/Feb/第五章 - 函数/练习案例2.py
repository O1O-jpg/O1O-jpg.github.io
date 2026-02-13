import os

balance = 5000000
name = None

def query_balance():
    print("--------------- Query Balance ---------------")
    print(f"{name},您好,您的余额剩余:{balance}元")

    os.system('pause')
    menu_reset()

def deposit():
    print("-------------- Deposit ---------------")
    money = int(input("请输入存款金额:"))
    print(f"{name},您好,您存款{money}元")

    global balance 
    balance += money

    print(f"{name},您好,您的余额剩余:{balance}元")

    os.system('pause')
    menu_reset()

def withdrawal():
    print("-------------- Withdrawal ---------------")
    money = int(input("请输入提款金额:"))
    print(f"{name},您好,您提款{money}元")

    global balance 
    balance -= money

    print(f"{name},您好,您的余额剩余:{balance}元")

    os.system('pause')
    menu_reset()

def exit():
    os.system('exit()')

def menu():
    print("--------------- Menu ---------------")
    print(f"{name},您好,欢迎来到黑人银行ATM,请选择操作")
    print("查询\t[1]")
    print("提款\t[2]")
    print("存款\t[3]")
    print("退出\t[4]")

    menu_choice(input())

def menu_choice(choice):
    if choice == '1':
        query_balance()
    elif choice == '2':
        withdrawal()
    elif choice == '3':
        deposit()
    elif choice == '4':
        exit()
    else:
        print("没有这个指令哟")
        print("o(╥﹏╥)o")

def menu_reset():
    os.system('cls')
    menu()

def ini_name():
    print("输入您的姓名:")
    global name
    name = input()

ini_name()

while 1:
    menu_reset()