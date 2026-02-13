my_str = "万过薪月，员序程马黑来，nohtyP学"
neo_my_str = my_str[::-1]

neo_my_str_2 = neo_my_str.split("，")
neo_my_str_3 = neo_my_str_2[1].replace("来","")
print(neo_my_str_3)