def checker(num):
    p = True
    for i in range(2, num):
        if num % i == 0:
            p = False
    if p:
        return True
    else:
        return False
sum = 0
for k in range(10, 251):
    numb = checker(k)
    if numb:
        sum += k
print(sum)

