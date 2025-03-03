
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print( f"Привіт, мене звуть {self.name}")

class Student(Person):
    def is_student(self):
        return True

student = Student("Юля")
student.greet()
print(f"{student.name} студент: {student.is_student()}")