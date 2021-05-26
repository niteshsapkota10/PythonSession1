#Multiple Inheritance
class Calculation1:
    """
    This class 
    calculates add value
    and returns the value
    after adding
    """
    def add(self,a,b):
        return a+b

class Calculation2:
    def Multipy(self,a,b):
        return a*b

class Derived(Calculation1,Calculation2):
    def divide(self,a,b):
        return a/b

d=Derived()
print(d.add(10,20))
print(d.Multipy(10,20))
print(d.divide(10,20))
print(type(d))

