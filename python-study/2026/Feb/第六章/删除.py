myList = ["A","B","C"]

# 语法1
del myList[1]

print(myList)

# 重新插入,reset
myList.insert(1,"B")
print(myList)

# 语法2
myList.pop(1)
print(myList)
