from audioop import reverse


l =[[1, 2], [3, 4], [5, 6, 7]]
l_flat=[]
def get_flat(x):
    for i in x:
        if isinstance(i,list):
            get_flat(i)
        else:
            l_flat.append(i)
get_flat(l)
l_flat.reverse()
print(l_flat)