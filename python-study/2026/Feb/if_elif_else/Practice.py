num = 49

if int(input("输入第一次猜想的数:")) == num:
    print("恭喜你，猜对了！")
elif int(input("不对,再猜一次:")) == num:
    print("恭喜你，猜对了！")
elif int(input("不对,再猜最后一次:")) == num:
    print("恭喜你，猜对了！")
else:
    print(f"Sorry,全部猜错啦,我想的是:{num}")
