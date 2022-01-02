n = 'my name'
i = 1

for j in n:
  t = n[:i]
  
  if t[len(t)-1:] ==' ':
    pass
  else:
    print(t)
    
  i = i + 1

i = len(n)*(-1) - 1
for j in n :
    t = n[:-i]

    if t[len(t)-1:] == " ":
      pass
    else:
        print(t)
    i = i + 1
