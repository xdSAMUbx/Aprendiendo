n = 14
cont = 0
while n!=0:
    if n%2 == 0:
        n = n/2
        cont += 1 
    else:
        n -= 1
        cont += 1 
print(cont)