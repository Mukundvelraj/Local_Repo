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

a = 35
b = 25
var = calc(a,b)
value = "add"
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
