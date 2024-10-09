# Problem 1
def swap_first_last(lst):
    lst[0], lst[-1] = lst[-1], lst[0]

lst = [1, 2, 3, 4]
swap_first_last(lst)
print(lst)  

# Problem 2
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def circumference(self):
        return 2 * math.pi * self.radius


# Problem 3
class Fraction:
    def __init__(self, num, denom):
        self.num = num
        self.denom = denom
    
    def __add__(self, other):
        new_num = self.num * other.denom + other.num * self.denom
        new_denom = self.denom * other.denom
        return Fraction(new_num, new_denom)
    
    def __str__(self):
        return f"{self.num}/{self.denom}"



# Problem 4
class Student:
    def __init__(self, name, grade, credits):
        assert 0 <= grade and grade <= 100, "Invalid grade"
        assert credits >= 0, "Invalid credits"
        self.name = name
        self.grade = grade
        self.credits = credits
    
    def add_credits(self, credits):
        self.credits += credits



# Problem 5
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def show_employees(self):
        for employee in self.employees:
            print(f"{employee.name}, Salary: {employee.salary}")



# Problem 6
class Manager(Employee):
    def __init__(self, name, salary, bonus):
        Employee.__init__(name, salary)
        self.bonus = bonus

    def show_info(self):
        print(f"{self.name}, Salary: {self.salary}, Bonus: {self.bonus}")


# Problem 7
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Teacher(Person):
    def __init__(self, name, age, subject):
        Person.__init__(name, age)
        self.subject = subject

class MathTeacher(Teacher):
    def __init__(self, name, age, subject, math_degree):
        Teacher.__init__(name, age, subject)
        self.math_degree = math_degree



# Problem 8
class OddNumbersIterator:
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


class OddNumbers:
    def __init__(self, n):
        assert n >= 1, "n must be greater than or equal to 1"
        self.n = n

    def __iter__(self):
        return OddNumbersIterator(self.n)

# Problem 9
class Account:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        self.__balance -= amount

    def get_balance(self):
        return self.__balance



# Problem 10

class Course:
    def __init__(self, name, credits):
        self.name = name
        self.credits = credits

class Student:
    def __init__(self, name):
        self.name = name
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)

    def drop_course(self, course_name):
        for course in self.courses:
            if course.name == course_name:
                self.courses.remove(course)
                break

    def total_credits(self):
        total = 0
        for course in self.courses:
            total += course.credits
        return total



# Problem 11
class Animal:
    def __init__(self, species, sound):
        self.species = species
        self.sound = sound

class Bird(Animal):
    def __init__(self, species, sound, can_fly=True):
        Animal.__init__(species, sound)
        self.can_fly = can_fly

class Penguin(Bird):
    def __init__(self, species, sound):
        Bird.__init__(species, sound, can_fly=False)

p = Penguin("Penguin", "Squawk")
print(p.species, p.sound, p.can_fly) 
