import random
import time
def native_search(l,target):
    for i in range(len(l)):
        if l[i] == target:
            return i
        
        
def binary_search(l, target, low = None, high = None):
    if low == None:
        low = 0
    if high == None:
        high = len(l) -1
    if high<low:
        return -1
    midpoint = (low + high)//2
    if l[midpoint] == target:
        return midpoint
    elif l[midpoint] > target:
        return binary_search(l,target,low,midpoint-1)
    else:
        return binary_search(l,target,midpoint+1,high)
        
lenght = 1000
sorted_list = set()
while len(sorted_list) < lenght:
    sorted_list.add(random.randint(-3*lenght,3*lenght))
sorted_list = sorted(list(sorted_list))

start = time.time()
for target in sorted_list:
    native_search(sorted_list, target)
end = time.time()
print("Native time",(end-start)/lenght,"seconds")

start = time.time()
for target in sorted_list:
    binary_search(sorted_list, target)
end = time.time()
print("Binary time",(end-start)/lenght,"seconds")