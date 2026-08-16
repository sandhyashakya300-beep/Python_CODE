#Static method

class math:
    def __init__(self,num):
        self.num = num

    @staticmethod
    def add(x, y):
        return x + y

    def addtonum(self, value):
        self.num += value

    

    
#a = math(5)
#ask the input from the user
user_val = int(input("Enter a number:"))
a = math(user_val)

print("current value of num:", a.num)

# ask the user for a number to add 
add_val = int(input("Enter a number to add:"))
a.addtonum(add_val)

#print(a.num)
#a.addtonum(10)
print(f"updated value of num:{a.num}")
