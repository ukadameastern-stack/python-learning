class Student:
  def __init__(self, id, name, title):
    self.id = id
    self.name = name
    self.title = title
  
  def myfunc(self):
    print(f"Hi {self.name}({self.title}) : {self.id}")

  @staticmethod
  def default():
    print("Default")      
    
s = Student(12, "Uday", "TL")

s.myfunc()
s.default()