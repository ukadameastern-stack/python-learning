class Student:
  def __init__(self, name, salary):
    self.name = name
    self.__grade = 0 # Private property
    self._salary = salary # Protected property

  def set_grade(self, grade):
    if 0 <= grade <= 100:
      self.__grade = grade
    else:
      print("Grade must be between 0 and 100")

  def get_grade(self):
    return self.__grade

  def get_status(self):
    if self.__grade >= 60:
      return "Passed"
    else:
      return "Failed"

student = Student("Uday", 2500)
print(student._salary) # 2500

student.set_grade(85)
print(student.get_grade()) # 85
print(student.get_status()) # Passed

student.set_grade(25)
print(student.get_status()) # Failed