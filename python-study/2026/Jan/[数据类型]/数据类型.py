# 用print直接输出
print(type("代理人"))
print(type(123))
print(type(12.3))
# 存储在变量里,再输出
int_type = type(123)
float_type = type(12.3)
str_type = type("代理人")

print(int_type)
print(float_type)
print(str_type)

# 查看变量中存储的数据类型
name = "代理人"
name_type = type(name)
print(name_type)