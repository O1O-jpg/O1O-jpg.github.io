# 定义bool类型变量
isAlive = True
print(f"isAlive的值是{isAlive}")

# bool类型变量参与比较运算
result1 = 5 > 3  # True
result2 = "baka" == "baka"  # True
print(f"5 > 3的结果是{result1},类型是{type(result1)}")
print(f"2 == 4的结果是{result2},类型是{type(result2)}")

# 比较运算符的使用
a = 10
b = 20
c = -1
result3 = a > b  # False
result4 = a < c  # False
result5 = b > c  # True
result6 = a >= 10  # True
result7 = b <= 15  # False
result8 = a != c  # True

print(f"a > b的结果是{result3},类型是{type(result3)}")
print(f"a < c的结果是{result4},类型是{type(result4)}")
print(f"b > c的结果是{result5},类型是{type(result5)}")
print(f"a >= 10的结果是{result6},类型是{type(result6)}")
print(f"b <= 15的结果是{result7},类型是{type(result7)}")
print(f"a != c的结果是{result8},类型是{type(result8)}")