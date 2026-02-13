name = "David"
age = 20
weight = 60

name_age = "David -%s" % age
print(name_age)

name_age_weight = name + "-%s %s" % (age,weight)
print(name_age_weight)

#數據類型佔位示例
name = "Alex"
weight = 91.5
age = 160

alex = "%s --%f --%d" % (name,weight,age)
print(alex)