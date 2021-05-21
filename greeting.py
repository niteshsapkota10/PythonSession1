import my_module
print(my_module.greeting("Nitesh"))
from my_module import greeting
print(greeting("Nitesh"))
from my_module import greeting,age
print(greeting("Nitesh")," Age = ",age)
# Ctrl+k+c
