class Parent:
    def __init__(self,lastname,height,age,looks):
        self.lastname=lastname
        self.height=height
        self.age=age
        self.looks=looks

    def getLastname(self):
        return self.lastname
    
    def getheight(self):
        return self.height
    
    def getAge(self):
        return self.age
    
    def getlooks(self):
        return self.looks
        
class Child(Parent):
    def __init__(self, lastname, height, age, looks,weight,firstname):
        super().__init__(lastname,height,age,looks)
        self.weight=weight
        self.firstname=firstname

    def getfirstname(self):
        return self.firstname
    def getWeight(self):
        return self.weight

Riju=Child("Rai","5",21,"Hot",30," Riju")
# print("Last Name : ",Riju.getLastname())
# print("Height : ",Riju.getheight())
# print("Age : ",Riju.getAge())
Riju.looks=" Nice and beautiful "
# print("Looks : ",Riju.looks)
# print("Weight : ",Riju.getWeight())

print("Hello My name is {0} {1}. I am {2} years old. I am {3} ft in height.I am very {4}. I am {5} kg. My father name is Prabhat Rai ..".format(Riju.getfirstname(),Riju.getLastname(),Riju.getAge(),Riju.getheight(),Riju.getlooks(),Riju.getWeight()))