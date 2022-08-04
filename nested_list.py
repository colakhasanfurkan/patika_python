arr = []
n = int(input())
for i in range(n):
    name = input()
    score = float(input())
    arr.append([])
    arr[i].append(score)
    arr[i].append(name)  
temp =[]
arr.sort()
list = arr
list.sort()
m = min(list)
c = 0
for i in range(n):
    if m[0] == list[i][0]:
        c+=1
for i in range(c):
    m = min(list)
    list.remove(m)
m = min(list)

for i in range(len(list)):
    if m[0] == list[i][0]:
        print(list[i][1])