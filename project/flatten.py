l = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
l_flat=[]
def get_flat(x):
    for i in x:
        if isinstance(i,list):
            get_flat(i)
        else:
            l_flat.append(i)
get_flat(l)
print(l_flat)