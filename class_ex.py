l = []
class Employee:
    num_emp = 0
    def __init__(self,name,last,age,pay):
        self.name = name
        self.last = last
        self.age = age
        self.pay = pay
        
    def full_name(self):
        return self.name + " " + self.last
    
    
for i in range(int(input())):
    e = input().split()
    emp = Employee(e[0],e[1],int(e[2]),int(e[3]))
    l.append(emp)
    Employee.num_emp +=1

def print_list(l):
    for i in range(len(l)):
        print(Employee.full_name(l[i]),l[i].age,l[i].pay)

def avg_pay(l):
    c = 0
    for i in range(len(l)):
        c += l[i].pay
    return c/len(l)
def avg_age(l):
    c=0
    for i in range(len(l)):
        c+=l[i].age
    return c/len(l)
print("\n")
print_list(l)
print("\nAverage pay: ",avg_pay(l))
print("\nAverage Age: ",avg_age(l))
print("\n\n",l[0].__dict__)

