class Mobile:
    processor="SnapDragon"
    camera=13
Redmi=Mobile()
print(type(Redmi))
print("The processor of Redmi is : ",Redmi.processor)
print("The processor of Redmi is : ",Redmi.camera)
Redmi.processor="Quad Core"
Redmi.camera=45
print("The processor of Redmi is : ",Redmi.processor)
print("The processor of Redmi is : ",Redmi.camera)
Samsumg=Mobile()
Samsumg.processor="S1"
Samsumg.camera=25
print("The processor of Samsung is : ",Samsumg.processor)
print("The processor of Samsung is : ",Samsumg.camera)