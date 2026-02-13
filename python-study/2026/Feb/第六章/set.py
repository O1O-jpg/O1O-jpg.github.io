my_set = {1,2,3,2,1}

print(my_set)

empty_set = set()
print(f"{type(empty_set)}:{empty_set}")

empty_set_1 = {}
print(f"{type(empty_set_1)}:{empty_set_1}")

# add()
empty_set.add(1)
print(empty_set)

my_set.add(4)
print(my_set)

# remove()
empty_set.remove(1)
my_set.remove(4)
print(my_set)
print(empty_set)

# pop()
element = my_set.pop()
print(my_set)
print(element)

# clear()
my_set.clear()
print(my_set)

# .difference()

set_1 = {1,2,3,4,5}
set_2 = {1,3,5}

set_1_2 = set_1.difference(set_2)
print(set_1_2)

# .difference_undate
set_1 = {1,2,3,5,6,7,9}
set_2 = {1,2,5,9}

set_1.difference_update(set_2)
print(set_1)
print(set_2)

# union()
neo_set = set_1.union(set_2)
print(neo_set)
neo_set = set_2.union(set_1)
print(neo_set)

# len()
print(len(neo_set))

# walk through
for element in neo_set:
    print(element)
