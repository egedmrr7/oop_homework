
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
            print("Grade must be between 0 and 100.")

   
    def get_grade(self):
        return self.__grade

   
    def info(self):
        return f"{self.code} - {self.name} ({self.credit} credits)"


c1 = Course("Mathematics", "MATH101", 6)
print(c1.info())  
c1.set_grade(85)
print("Grade:", c1.get_grade())



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


online = OnlineCourse("Chemistry", "CHEM102", 5, "Zoom")
campus = CampusCourse("Physics", "PHYS103", 5, "A-204")


print(online.info())
print(campus.info())


from abc import ABC, abstractmethod

class AbstractStudent(ABC):
    @abstractmethod
    def register_course(self):
        pass

    @abstractmethod
    def show_courses(self):
        pass


class Student(AbstractStudent):
    def __init__(self, name):
        self.name = name
        self.courses = []

    def register_course(self, course):
        self.courses.append(course)
        print(f"{self.name} registered to {course.name}")

    def show_courses(self):
        print(f"{self.name}'s Courses:")
        for c in self.courses:
            print("-", c.name)


s1 = Student("Ahmet")
s1.register_course(c1)
s1.register_course(campus)
s1.show_courses()
