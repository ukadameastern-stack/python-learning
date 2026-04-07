class Person:
  def __init__(self, fname, lname):
    self.firstname = fname + ' Suresh'
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)


class Student(Person):
  def __init__(self, fname, lname, age):
    #super().__init__(fname, lname) # This also work with 2 params
    Person.__init__(self, fname, lname) # This with 3 params
    self.age = age


x = Student("Uday", "Kadam", 25)
x.printname() # Uday Suresh Kadam
print(x.age) # 25