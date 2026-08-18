class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_details(self):
        print( f"Name: {self.name}, Position: {self.position}")
  
Employee.get_details("Alice", "Developer")       