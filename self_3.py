class calc:
    def __init__(self,a,b):
        self.a = a
        self.b = b
        self.c = 0
    def add(self):
        self.c = self.a + self.b
    def sub(self):
        self.c = self.a - self.b
    def multi(self):
        self.c = self.a * self.b
    def div(self):
        self.c = self.a / self.b
    def display(self):
        print("The final value ",self.c)

a = int(input("Enter the a value = "))
b = int(input("Enter the b value = "))
var = calc(a,b)
value = input("Enter the operation add/sub/multi/div = ")
if(value == "add"):
    var.add()
    print("the operation is = ",value)
    var.display()
elif(value == "sub"):
    var.sub()
    print("the operation is = ",value)
    var.display()
elif(value == "multi"):
    var.multi()
    print("the operation is = ",value)
    var.display()
elif(value == "div"):
    var.div()
    print("the operation is = ",value)
    var.display()
else:
    print("Invalid")
    print("the operation is = ",value)