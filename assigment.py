
from abc import ABC, abstractmethod
from functools import singledispatchmethod
from dataclasses import dataclass


class Course:
    def __init__(self, name, code, credit):
        self.name = name
        self.code = code
        self.credit = credit
        self.__grade = None

    def set_grade(self, grade):
        if 0 <= grade <= 100:
            self.__grade = grade
        else:
            raise InvalidGradeError("Grade must be between 0 and 100.")

    def get_grade(self):
        return self.__grade

    def info(self):
        return f"{self.code} - {self.name} ({self.credit} credits)"

    def __add__(self, other):
        if not isinstance(other, Course):
            return NotImplemented
        total_credit = self.credit + other.credit
        return Course("Combined", f"{self.code}+{other.code}", total_credit)


class OnlineCourse(Course):
    def __init__(self, name, code, credit, platform):
        super().__init__(name, code, credit)
        self.platform = platform

    def info(self):
        base = super().info()
        return base + f" | Type: Online | Platform: {self.platform}"


class CampusCourse(Course):
    def __init__(self, name, code, credit, classroom):
        super().__init__(name, code, credit)
        self.classroom = classroom

    def info(self):
        base = super().info()
        return base + f" | Type: On Campus | Room: {self.classroom}"


class AbstractStudent(ABC):
    @abstractmethod
    def register_course(self, course):
        pass

    @abstractmethod
    def show_courses(self):
        pass


class Advisor:
    def __init__(self, name):
        self.name = name


class Student(AbstractStudent):
    def __init__(self, name, advisor=None):
        self.name = name
        self.courses = []
        self.advisor = advisor

    def register_course(self, course):
        self.courses.append(course)

    def show_courses(self):
        print(f"{self.name}'s Courses:")
        for c in self.courses:
            print("-", c.info())

    @property
    def gpa(self):
        valid_grades = [c.get_grade() for c in self.courses if c.get_grade() is not None]
        if not valid_grades:
            return 0
        return round(sum(valid_grades) / len(valid_grades), 2)


class InvalidGradeError(Exception):
    pass


class Department:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)


class CourseFactory:
    @staticmethod
    def create_course(course_type, name, code, credit, extra):
        if course_type == "online":
            return OnlineCourse(name, code, credit, extra)
        elif course_type == "campus":
            return CampusCourse(name, code, credit, extra)
        else:
            raise ValueError("Invalid course type")


class GradeCalculator:
    @singledispatchmethod
    def calculate(self, data):
        raise NotImplementedError

    @calculate.register
    def _(self, grade: int):
        return "Pass" if grade >= 50 else "Fail"

    @calculate.register
    def _(self, grades: list):
        if not grades:
            return "No grades"
        avg = sum(grades) / len(grades)
        return "Pass" if avg >= 50 else "Fail"


class Logger:
    @staticmethod
    def log(message):
        print(f"[LOG] {message}")


@dataclass(frozen=True)
class Point:
    x: float
    y: float

    def translate(self, dx: float, dy: float):
        return Point(self.x + dx, self.y + dy)


advisor = Advisor("Dr. Smith")
student = Student("Ahmet", advisor)
department = Department("Engineering")
department.add_student(student)

c1 = Course("Mathematics", "MATH101", 6)
c2 = Course("Physics", "PHYS103", 5)
c3 = CourseFactory.create_course("online", "Chemistry", "CHEM102", 5, "Zoom")

student.register_course(c1)
student.register_course(c2)
student.register_course(c3)

c1.set_grade(90)
c2.set_grade(75)
c3.set_grade(80)

print(f"GPA of {student.name}: {student.gpa}")
print((c1 + c2).info())

calc = GradeCalculator()
print("Single grade result:", calc.calculate(85))
print("List of grades result:", calc.calculate([85, 70, 90]))

Logger.log("All operations completed successfully.")

p1 = Point(0.0, 0.0)
p2 = p1.translate(2.5, 4.5)
print("New Point:", p2)
