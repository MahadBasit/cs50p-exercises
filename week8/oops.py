'''
class Book:
    def __init__(self, title, pages, pages_read = 0):
        self.title = title
        self.pages = pages
        self.pages_read = pages_read

    def read(self, n):
        self.pages_read += n
        return self.pages_read
    
    def progress(self):
        return f'{(self.pages_read/self.pages)*100:.2f}%'
    
s1 = Book('Quad', 500)


s1.read(45)
s1.read(56)

print(s1.progress())
'''

class Student:
    schol_name = 'HITEC'
    def __init__(self, name, age, major, ):
        self.name = name
        self.age = age
        self.major = major

    def __str__(self):
        return f"{self.name} is {self.age} years old and his major is {self.major}."
    
class GraduateStudent(Student):
    def __init__(self, name, age, major, thesis_title):
        super().__init__(name, age, major)
        self.thesis_title = thesis_title

    def __str__(self):
        return super().__str__() + f" His thesis title is {self.thesis_title}"
    
    def defend_thesis(self):
        return f"{self.name} is defending {self.thesis_title}."