from random import randint
list = []
n = 10**6
for i in range(n):
    a = randint(1,10**10)
    
    list.append(a)

print(max(list))
