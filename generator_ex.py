l  = [1,2,3]
def square(l):
    for e in l:
        yield e*e
g = square(l)
print(g)