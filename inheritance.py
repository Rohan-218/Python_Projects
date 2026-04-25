class a:
    def sum(self,a,b):
        self.s=a+b
    def p(self):
        print(f"Result is {self.s}.")
class b(a):
    def sub(self,x,y):
        self.s=x-y
s=b()
s.sum(100,200)
s.p()
s.sub(10,20)
s.p()
 