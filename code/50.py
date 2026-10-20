class Student:
    college="ABC college"

    def __init__(self,name):
        self.name=name
    def display(self):
        print("name:",self.name)
        print("college:",Student.college)
s1 = Student("Dev")
s2 = Student("Rahul")
s1.display()
s2.display()