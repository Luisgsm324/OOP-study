"""
A criação de múltiplas classes é uma prática comum e essas classes ainda podem relacionar entre si,
servindo como uma forma de facilitar o trabalho. Pegaremos a classe Student construída anteriormente.
"""
class Student():
    def __init__(self, name, grade):
        # O nome não precisa ser igual, então você poderia colocar outra coisa em vez de repetir. 
        self.name = name
        self.grade = grade
    
class Course():
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []
    
    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def get_average_grade(self):
        i = 0 
        for student in self.students: 
            if i < student.grade:
                i = student.grade
        return i

student1 = Student("Luis", 15)
student2 = Student("Clara", 18)
student3 = Student("Lucas", 20)

course1 = Course("Bar", 3)
course1.add_student(student1)
course1.add_student(student2)
course1.add_student(student3)
print(course1.get_average_grade())
