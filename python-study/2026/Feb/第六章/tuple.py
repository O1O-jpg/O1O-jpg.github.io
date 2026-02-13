t1 = (1,"2",'3',1,1.1)

print(f"{type(t1)}:\t{t1}")

# t2是字符串,不是tuple
t2 = ("m")
print(f"{type(t2)}\t\t{t2}")

# t3是元组
t3 = ("m",)
print(f"{type(t3)}:\t{t3}")

# tuple嵌套
t4 = ((1,2,3),(4,5,6))
print(f"{type(t4)}:\t{t4}")

# tuple下标
print(t4[0][0])

# index
print(t1.index(1))

# count
print(t1.count(1))

# len
print(len(t1))

# 遍历
print("========For========")
# for
for element in t1:
    print(element)

# while
print("========While========")
element = 0 

while element < len(t1):
    print(t1[element])

    element += 1

# 