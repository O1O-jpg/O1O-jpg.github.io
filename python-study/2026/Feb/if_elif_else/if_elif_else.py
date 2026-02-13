print("欢迎来到Meow餐厅！")
high = int(input("请输入您的身高（厘米）："))
level = int(input("请输入您的会员等级（1-10）："))

if high <= 120:
    print("您的升高小于120cm,可以免费用餐！")
elif level >= 6:
    print("您的会员等级大于等于6级，可以免费用餐！")
else:
    print("很抱歉，您需要支付餐费。")

print("祝您用餐愉快！")

# 示例二
print("欢迎来到Meow餐厅！")
high = int(input("请输入您的身高（厘米）："))
level = int(input("请输入您的会员等级（1-10）："))
day = int(input("输入今天的日期:"))

if high <= 120:
    print("您的升高小于120cm,可以免费用餐！")
elif level >= 6:
    print("您的会员等级大于等于6级，可以免费用餐！")
elif day == 1:
    print("Meow恭喜,今天是每月的第一天，您可以免费用餐！")
else:
    print("很抱歉，您需要支付餐费。")

print("祝您用餐愉快！")

# 示例三
print("欢迎来到Meow餐厅！")

if int(input("请输入您的身高（厘米）：")) <= 120:
    print("您的升高小于120cm,可以免费用餐！")
elif int(input("请输入您的会员等级（1-10）：")) >= 6:
    print("您的会员等级大于等于6级，可以免费用餐！")
elif int(input("输入今天的日期:")):
    print("Meow恭喜,今天是每月的第一天，您可以免费用餐！")
else:
    print("很抱歉，您需要支付餐费。")