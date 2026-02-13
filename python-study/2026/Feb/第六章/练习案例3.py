# 填充列表
myList = []
for i in range(1,11):
    myList.append(i)

print(myList)

evenList = []

for i in myList:
    if i % 2 == 0:
        evenList.append(i)
    else:
        continue
print(f"for循环:\t{evenList}")

while i < len(myList):
    if i % 2 == 0:
        evenList.append(i)
    else:
        continue

    i += 1

print(f"while循环:\t{evenList}")