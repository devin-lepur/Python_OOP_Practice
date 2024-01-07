"""
    Author: Devin Lepur
    Student management system to further practice python OOP
    1/6/24
    ***Work in Progress***
"""
class School:
    #List of courses in the school
    courseList = []

    def __init__(self, schoolName):
        self.name = schoolName

    def addCourse(self, course):
        self.courseList.append(course)
        print(f"Course Added: {course.name}")

    def removeCourse(self, course):
        for otherCourse in self.courseList:
            if course == otherCourse:
                self.courseList.remove(otherCourse)
        print(f"Course Removed: {course.name}")

    def getCourseList(self):
        tempList = []
        for course in self.courseList:
            tempList.append(course.name)
        #This feels like poor syntax but I'm not sure how else to have a preceding newline
        print()
        print(tempList)
        print()




class Course:
    studentList = []

    def __init__(self, Coursename, requiredGrade, teacher = "Jane Doe"):
        self.name = Coursename
        self.requiredGrade = requiredGrade
        self.teacher = teacher

    def addStudent(self, student):
        self.studentList.append(student)

    #TODO: Ensure works properly
    def removeStudent(self, student):
        self.studentList.remove(student)

    def __eq__(self, other):
        return(
            self.name == other.name and
            self.requiredGrade == other.requiredGrade and
            self.teacher == other.teacher)

class Student:
    #Constructor
    def __init__(self, gpa, gradeLevel, homeroom, school, name = "John Doe"):
        self.gpa = gpa
        self.gradeLevel = gradeLevel
        self.homeroom = homeroom
        self.name = name
    
    #TODO: Ensure works properly
    def __eq__(self, other):
        return(self.name == other.name)


mySchool = School("Rio Seco")
myMathClass = Course("Math", 0)
mySchool.addCourse(myMathClass)
myEnglishClass = Course("English", 3, "Mr Shrin")
mySchool.addCourse(myEnglishClass)
phonyMathClass = Course("superHardMath", 0)
mySchool.addCourse(phonyMathClass)

mySchool.getCourseList()
mySchool.removeCourse(myMathClass)
mySchool.getCourseList()