#MethodOverriding
class Pravhat:
    def assignment(self):
        print("I am doing Assignment ")

class Tekendra(Pravhat):
    def assignment(self):
        super().assignment()
        print("Pravhat sab ko same xa tmle kasko sareko ")

teke=Tekendra()
teke.assignment()