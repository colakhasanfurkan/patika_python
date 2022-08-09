import numpy as np

n,m = map(int,input().split())
print(n,m)
arrA = np.array([input().split() for _ in range(n)],int)
arrB = np.min(arrA, axis = 1)
print (np.min(arrB))