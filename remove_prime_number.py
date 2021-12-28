list1 = [7,5,7,0,8,-5,-88,53,79,-2]
list2 = []
for num in list1:
    for i in range(2, num):
        if(num % i == 0) :
            break
        list2.append(num)
for num in list2 :
    while num in list1:
        list1.remove(num)
print(list1)



