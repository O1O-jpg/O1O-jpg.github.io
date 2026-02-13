# continue example
area = int(input("输入一个范围:"))
i = 0
count = 0

while i<area:
    i += 1
    if i % 2 == 0:
        print(f"{i}是偶数")
        count += 1
    else:
        continue

print(f"在{i}到{area}的范围内,有{count}个偶数")

# break example
for num in range(0,area+1):
    num += 1
    if num < area+1:
        print(num)
    else:
        break
    

# break in nested loops
for num1 in range(1,area+1):
    if num1 % 2 == 0:
        print(f"{num1}是偶数")

        for num2 in range(1,area+1):
            print(num2)
            break
    else:
        continue

