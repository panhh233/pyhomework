class MyClass(object):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def show(self):
        print(self.a, self.b, self.c)

    def add(self):
        print(self.a + self.b + self.c)

class MySecondClass(MyClass):
    def __init__(self, a, b, c, d):
        super(MySecondClass, self).__init__(a, b, c)
        self.d = d
    
    def add(self):
        print(self.a + self.b + self.c + self.d)

    def show(self):
        print(self.a, self.b, self.c, self.d)

class MyThirdClass(MySecondClass):
    def max(self):
        print(max(self.a, self.b, self.c, self.d))

obj1 = MyThirdClass(1, 2, 3, 4)
obj1.show()
obj1.add()
obj1.max()