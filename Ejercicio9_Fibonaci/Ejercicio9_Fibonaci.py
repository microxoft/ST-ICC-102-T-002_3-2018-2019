num1 = 0
num2 = 1
num3 = num1 + num2
sumaPares = 0

while num3 < 4000000:
    sumaPares += num3 if (num3 % 2 == 0) else 0
    num1 = num2
    num2 = num3
    num3 = num1 + num2
    
print(sumaPares) # 4613732
