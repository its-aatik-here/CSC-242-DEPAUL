import code

# exercise 1
def swap_first_last(lst):
    first = lst[0]
    last = lst[len(lst)-1]
    lst[0] = last
    lst[len(lst)-1] = first
    return lst
# exercise 2
class Circle():
    def __init__(self,radius):
        self.radius = radius
    
    def circumference(self):
        return 2*self.radius*(3.142)
    def area (self):
        return 3.142*(self.radius**2)
# exercise 3
class Fraction():
    def __init__(self, numerator, denomenator):
        self.numerator = numerator
        self.denomenator = denomenator

    def __add__(self, other):
        new_numerator = (self.numerator *other.denomenator) + (self.denomenator * other.numerator)
        new_denomenator = self.denomenator * other.denomenator
        return Fraction(new_numerator, new_denomenator)
    def __str__(self):
        return f"{self.numerator}/{self.denomenator}"
# exercise 4
class Student ():
    def __init__(self, name, grade, credits):
        self.name = name
        self.grade = grade
        self.credits = credits
        assert grade >-1 and grade <101, "Invalid grade"
        assert credits> -1 , "Invalid Credits"
    def add_Credits(self,credits):
        self.credits += credits
# exercise 5
class Employee ():
    def __init__ (self,name,salary):
        self.name = name
        self.salary = salary
class Department ():
    def __init__(self, name):
        self.name = name
        self.employees = []
    def add_employees(self):
        self.employees.append(Employee)
    def show_employees(self):
        for employee in self.employees:
            print (f"{employee.name}, salary: ${employee.salary}")

# exercise 6
class Manager (Employee):
    def __init__(self,name,salary,bonus):
        Employee.__init__(name,salary)
        self.bonus = bonus
    def show_info(self):
        print (f"{self.name}, Salary= {self.salary}, Bonus= {self.bonus}")

#exercise 7
class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
class Teacher (Person):
    def __init__(self, name, age, subject):
        Person.__init__(self, name,age)
        self.subject = subject
class MathTeacher (Teacher):
    def __init__(self, name, age, subject, math_degree):
        Teacher.__init__(self, name, age, subject)
        self.math_degree = math_degree

#exercise 8
class OddNumbersiterator():
    def __init__(self, n):
        self.n = n
        self.current = 1
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current > self.n:
            raise StopIteration
        odd = self.current
        self.current += 2
        return odd
class OddNumbers():
    def __init__(self,n):
        assert n>=1, "n must be greater than or equal to 1"
        self.n = n
    def __iter__ (self,n):
        return OddNumbersiterator(self.n)
    
# exercise 9
class Account():
    def __init__(self, balance):
        self.balance= balance
    def deposit(self,value):
        self.balance += value
    def withdraw(self,value):
        self.balance -=value
    def get_balance(self):
        return self.balance
#exercise 10
class Course():
    def __init__(self,name,credits):
        self.name = name
        self.credits = credits
class Student():
    def __init__(self):
        self.courses = []
    def add_course(self,name,credits):
        self.courses.append(Course(name,credits))
    def drop_course(self,name,credits):
        for course in self.courses:
            if course.name == name and course.credits == credits:
                self.courses.remove(course)
    def total_credits(self):
        for course in self.courses:
            self.total_credits += course.credits
        return self.total_credits
# exercise 11
class Animal ():
    def __init__(self,species,sound):
        self.species = species
        self.sound = sound
class Bird (Animal):
    def __init__(self,species,sound,can_fly):
        Animal().__init__(species,sound)
        self.can_fly = can_fly
class Penguin (Bird):
    def __init__(self,species,sound):
        Bird.__init__(species,sound,can_fly=False)

p = Penguin("Penguin", "Squawk")
print (p.species,p.sound,p.can_fly)



code.interact(local=dict(globals(), **locals()))