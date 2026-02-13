# 示例一
if int(input("请输入您的身高:")) >= 120:
    print("您的身高大于120cm,需要付费游玩")
    print("但是如果您的等级大于6级的话,可以免费游玩")

    if int(input("请输入您的等级:")) >= 6:
        print("您的等级大于6级,可以免费游玩")
    else:
        print("Sorry,您需要付费游玩")

else:
    print("您的身高小于120cm,可以免费游玩")

# 示例二
age = int(input("请输入您的年龄:"))
time = int(input("输入你的入职时间:"))
level = int(input("请输入您的等级:"))

if age >= 18:
    print("OK,您是成年人,继续判断")

    if age < 30:
        print("您的年龄符合标准,继续判断")

        if time > 2:
            print("您的入职时间大于2年,您可以领取礼物")
        elif level >= 3:
            print("您的等级大于等于3级,您可以领取礼物")
        else:
            print("您的入职时间或等级不符合标准,不得领取礼物")
    else:
        print("您不符合标准,不得领取礼物")
else:
    print("您是未成年人,不得领取礼物")