class Student:
    #def __init__(self) ->None:
    def __init__(self, school_name, department_name, director_name, student_name, id, school_address, points, GPA):
        self.school_name = school_name
        self.department_name = department_name
        self.director_name = director_name
        self.student_name = student_name
        self.id = id
        self.school_address = school_address
        self.points = points
        self.GPA = GPA

        school_name = "STUST"
    def getSchoolName(self):
        return self.school_name

    def setSchoolName(self, school):
        self.school_name = school

    def getDepartment(self):
        return self.department_name

    def setDepartment(self, department):
        self.department_name = department

    def getDirectorName(self):
        return self.director_name

    def setDirectorName(self, director):
        self.director_name = director

    def getStudentName(self):
        return self.student_name

    def setStudentName(self, student_name):
        self.student_name = student_name

    def getId(self):
        return self.id

    def setId(self, student_id):
        self.id = student_id

    def getSchoolAddress(self):
        return self.school_address

    def setSchoolAddress(self, address):
        self.school_address = address

    def getPoints(self):
        return self.points

    def setPoints(self, point):
        self.points = point

    def getGPA(self):
        return self.GPA

    def setGPA(self, gpa):
        self.GPA = gpa

student1 = Student("IE", "John", "Ace", "4B0G0140", "南台街1號", "10", "100")
print(student1.getSchoolName(),student1.getDepartment(),student1.getDirectorName(),student1.getId(),student1.getStudentName(),student1.getPoints(),student1.getGPA())
print(student1.setSchoolName(),student1.setDepartment(),student1.setDirectorName(),student1.setId(),student1.setStudentName(),student1.setPoints(),student1.setGPA())