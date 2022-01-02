n = int(input())
i = 1
l = []
while len(l)<n:
    t = ''
    for j in range(1, i+1):
        t += str(j)

    l.append(t)
    i += 1

