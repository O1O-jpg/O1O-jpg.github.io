my_list = [1,2,3,4,5,6,7,8,9,10]

neo_my_list = my_list[0:5]
print(neo_my_list)

neo_my_list = my_list[0:5:2]
print(neo_my_list)

my_str = "12345"
neo_my_str = my_str[::2]
print(neo_my_str)

# 步长为负数相当于反转
neo_my_str = my_str[::-1]
print(neo_my_str)

neo_my_str = my_str[::-2]
print(neo_my_str)

neo_my_str = my_str[4:2:-1]
print(neo_my_str)
