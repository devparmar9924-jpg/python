class A:
    def show(self):
        print("class a")
class B(A):
    def display(self):
        print("class b")
class C(B):
    def result(self):
        print("class c")
obj=C()
obj.show()
obj.display()
obj.result()