import operator
def employee_lister(f):
    def inner(employee):
        return map(f,sorted(employee,key=lambda x: x[2]))
    return inner

@employee_lister
def name_format(worker):
    return ("Mr. " if worker[3]== 'M' else 'Ms. ') + worker[0] + ' ' + worker[1]



employee  =[input().split() for i in range(int(input()))]
print(*name_format(employee),sep='\n')