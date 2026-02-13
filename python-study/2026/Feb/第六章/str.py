str1 = "东方不败"

print(str1[0])
print(str1[-1])

# index
print(str1.index('东'))

# replace
print(str1.replace("东","西"))

# split
str2 = "But I love you so"
neoStr2 = str2.split(" ")
print(neoStr2)

# strip
str3 = "                    Some    body                 "
strNeo3 = str3.strip()
print(strNeo3)

str3 = "1213Somebody1231"
strNeo3 = str3.strip("123")
# 上面传入的不是123这个字符串,而是1,2,3这几个字符
print(strNeo3)

# walk throuhgh
# for
for element in str1:
    print(element)
# python 没有块作用域我服了
del(element)

# while
index = 0

while index < len(str1):
    print(str1[index])
    index+=1