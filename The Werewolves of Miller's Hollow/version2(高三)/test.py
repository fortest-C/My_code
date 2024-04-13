class C:
    def __init__(self, x):
        self.x = x

    def De(self):
        print(self.x)
try:
    c = C(5)
    c.De()
except:
    pass

class A:
    def __init__(self, x):
        self.x = x
        
    def dep(self):  #存款動作: amount代表存入金額
        print(self.x)
a = A(1)
a.dep()