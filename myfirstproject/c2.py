class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    @classmethod
    def from_string(cls, data):
        name, marks = data.split("-")
        return cls(name, int(marks))

s = Student.from_string("Uday-90")
print(type(s))    
print(s.name, s.marks)    