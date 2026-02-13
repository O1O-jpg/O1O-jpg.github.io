# 示例一
name = "Droool" # 定义了一个字符串

for i in name:  # 遍历字符串
    print(i)    # 打印每个字符

# 练习案例
name_1 = "itheima is a brand of itcast"
count = 0

for i in name_1:  # 遍历字符串
    if i == 'a':
        count += 1  # 如果字符是a，计数器加1

print(count)