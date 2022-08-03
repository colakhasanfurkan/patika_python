
n = int(input())

def numbers(n):
    sum = 0
    m=n-1
    for i in range(1,n+1):
        sum=i*(10**m)+sum
        m-=1
    return sum
print(numbers(n))