class myclass: # Define a class
    x = 5 
    print("x value using class:",x)
myclass()

p1 = myclass() # Create an object of myclass
print('x value using object:',p1.x)


'''
The __init__() Function
The examples above are classes and objects in their simplest form, and are not really useful in real life applications.
To understand the meaning of classes we have to understand the built-in __init__() function.
All classes have a function called __init__(), which is always executed when the class is being initiated.
'''
class person: 
    def __init__(self,name,age):
        self.name = name
        self.age = age
p2 = person('Akash',25)
print(p2.name)
print(p2.age)  


# Without The__str__() Function
class person2:
    def __init__(self1,name,age):
        self1.name = name
        self1.age = age
p3 = person2("John",30)        
print(p3)   # String Not Stored in the Address of p3


#With The_str_() Function
class person3:
    def __init__(self2,name1,age1):
        self2.name1 = name1
        self2.age1 = age1
    def __str__(self2):
      return f"{self2.name1}({self2.age1})"        
p4 = person3("Priya",30) #String Stored in the Address of p4
print(p4)         


'''
Object Methods
Objects can also contain methods. Methods in objects are functions that belong to the object.
'''
class person4:
    def __init__(self3,name2,age2):
        self3.name2 = name2
        self3.age2 = age2
    
    def myfunc(self3):
        print('Hello my name is',self3.name2)
p5 = person4("Ravi",28)
p5.myfunc()  # Call the method of the object p5        


'''
The self Parameter
The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.
'''
class person5:
    def __int__(self4,name3,age3):
        self4.name3 = name3
        self4.age3 = age3


'''
Modifying Object Properties
'''

class person6:
    def __init__(self5,name4,age4):
       self5.name4 = name4 
       self5.age4 = age4

    def myfun(self5):
        print('Hello my name is',self5.name4)

p6 = person6("Sita",22)

p6.age4 = 30
print(p6.name4,p6.age4)



