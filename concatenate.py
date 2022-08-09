import numpy as np
arr=[[]]
n,m = map(int,input().split())
for i in range(n):
    arr.append( map(int,input().split()))
print(arr[0][0])