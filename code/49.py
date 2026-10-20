class Father:
    def show(self):
        print("this is father class")
class Son(Father):
    def display(self):
        print("this is son class")
s = Son()
s.show()
s.display()