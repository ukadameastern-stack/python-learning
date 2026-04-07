class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age # Private property

  def get_age(self):
    return self.__age

  def set_age(self, age):
    if age > 0:
      self.__age = age
    else:
      print("Age must be positive")

p1 = Person("Uday", 25)
print(p1.name) # Uday
print(p1.get_age()) # Age (Private property)
p1.set_age(-50) # Age must be positive
p1.set_age(50) # 50
print(p1.get_age()) # Age (Private property)
#print(p1.__age) # This will cause an error
