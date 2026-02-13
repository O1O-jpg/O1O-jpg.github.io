myList = [21,25,21,23,22,20]

# append 附加;贴上
myList.append(31)

# extend 伸展,扩充
myList.extend([29,33,30])

# 取出第一个元素
print(myList[0])

# 去除最后一个元素
# 因为是0开始的,所以要-1
print(myList[len(myList)-1])

print(myList.index(31))