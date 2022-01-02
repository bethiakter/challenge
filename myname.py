n = "myname"
i = 1
for j in n:
    print(n[:i])
    i += 1

i = len(n)*(-1) - 1
for j in n:
    print(n[:-i])
    i +=1