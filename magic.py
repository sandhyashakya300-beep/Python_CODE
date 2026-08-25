# Python Magic Method

class Employee:
    def __init__(self,name):
        self.name = name 
    def __len__(self):
        i = 0
        for c in self.name:
            i += 1 
        return i
    

e1 = Employee("Amit Kumar")

print(e1.name)

#print(len(e1))
def __str__(self):
    return f"Employee name is {self.name}"
print(e1)