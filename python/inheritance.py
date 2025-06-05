class person:
   def __init__(self, name, age):
       self.firstname = name
       self.lastname = age

   def display(self):
       print("Name:",self.firstname, "Last Name:",self.lastname,'\n')

obj = person("John", 36)
obj.display()  # Output: Name: John Last Name: 36 


# Create a Child Class
class empdetail:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname

    def printname(self):
            print(self.firstname,self.lastname)


class student(empdetail):
  pass

obj1 = student('Akash',"Kumar")
obj1.printname()  # Output: Akash Kumar


# Add the __init__() Function
class empdetail1:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    def printname(self):
        print(self.firstname,self.lastname)
class student(empdetail1):
    def __init__(self,fname,lname):
        empdetail1.__init__(self,fname,lname)
obj2=student("Akash",'Biswas')
obj2.printname()                       


# Use the super() Function
class empdetail2:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    def printname(self):
        print(self.firstname,self.lastname)
class student(empdetail2):
    def __init__(self,fname,lname):
        super().__init__(fname,lname)
obj3=student("Akash","Aggarwal")
obj3.printname()                    

# Add Properties
class studetail:
  def __init__(self,fname,lname):
      self.firstname=fname
      self.lastname=lname

  def printname(self):
      print(self.firstname,self.lastname)
class student(studetail):
    def __init__(self,fname,lname):
        super().__init__(fname,lname)
        self.graduateon = "BCA"
obj4 = student("Akash","Biswas")
print(obj4.firstname,obj4.lastname,"","Graduated On : ",obj4.graduateon)      


