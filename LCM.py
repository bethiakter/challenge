num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
num3 = int(input("Enter the third number:"))
i = 1
while True:
    if i%num1 == 0 and i%num2 == 0 and i%num3 == 0:
        print("LCM =",i)
        break
    else:
        i +=1