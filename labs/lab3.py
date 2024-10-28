class Course ():
    def  __init__(self, course_name):
        assert type(course_name) == str, "Course name must be a string"
        self.course_name =  course_name
        self.grades = []
    def add_grades(self,grades):
        assert type(grades) == int or float , "Grades must be a list"
        assert 0 <= grades <= 100, "Grade must be between 0 and 100"
        self.grades.append(grades)
    def calculate_average (self):
        assert self.grades , "No grades to calculate average"
        return sum (self.grades) / len(self.grades)
    def __str__(self):
        return f"Course Name: {self.course_name}, Average Grade: {self.calculate_average():.2f}"
    
    
# course = Course("CSC 242")
# course.add_grades(95)
# course.add_grades(87)
# course.add_grades(92.5)
# print(course.calculate_average())
# print (course)



class rectangle():
    def __init__(self,r_width,r_height):
        assert  type(r_width) == int or float , "Width must be a number"
        assert  type(r_height) == int or float , "Height must be a number"
        self.width = r_width
        self.height = r_height
    def __it__(self,other):
        return self.width * self.height < other.width * other.height
    def __gt__(self,other):
        return self.width * self.height > other.width * other.height
    def __eq__(self,other):
        return self.width * self.height == other.width * other.height
    def __str__(self):
        return f"Rectangle ({self.width}, {self.height})" 

# r1 = rectangle(4,5)
# r2 = rectangle(3,7)
# print (r1<r2)
# print (r1>r2)
# print (r1==r2)

class Person ():
    def  __init__(self, name, age):
        assert type(name) == str and len(name)>0, "Name must be a string"
        assert age>0 , "Age must be positive"
        self.name =  name
        self.age = age
    def __it__ (self,other):
        return  self.age < other.age
    def  __gt__ (self,other):
        return self.age > other.age
    def __add__ (self,other):
        return self.age + other.age
    def  __str__ (self):
        return f"Person: ({self.name},{self.age})"

# p1 = Person("Alice", 30)
# p2 = Person("Bob", 25)
# print (p1<p2)
# print (p1>p2)
# print (p1+p2)