myList = ["A","B","C","B","C","B"]

countB = myList.count("B")
count = 0

while count < countB:
    myList.remove("B")
    count += 1

print(myList)