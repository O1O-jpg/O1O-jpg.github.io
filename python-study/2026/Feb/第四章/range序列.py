# range序列
# 语法一
print("range(5) 输出:")
for i in range(5):
    print(i,end=",")

print()  # 换行

# 语法二
print("range(1,5) 输出:")
for i in range(1,5):
    print(i,end=",")

print()  # 换行

# 语法三
print("range(1,10,2) 输出:")
for i in range(1,10,2):
    print(i,end=",")

print()  # 换行

# 练习案例
num = 56
count = 0

for i in range(1,num):
    if i % 2 == 0:
        count += 1

print(f"1到{num}(不含{num}本身)之间偶数的个数为：{count}")