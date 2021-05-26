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
#issubclass(sub,sup)
print(issubclass(Derived,Calculation1))
print(issubclass(Calculation1,Calculation2))
print(issubclass(Derived,Calculation2))

#isInstance(obj,class)
d=Derived()
c=Calculation1()
print(isinstance(d,Derived))
print(isinstance(c,Derived))
print(isinstance(d,Calculation2))
