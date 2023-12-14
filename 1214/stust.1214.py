import json
import os

class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.courses = {}
 
    def add_course(self, course_code, course_name, semester):
        if semester not in self.courses:
            self.courses[semester] = []
        self.courses[semester].append({"code": course_code, "name": course_name})

    def delete_course(self, course_code, semester):
        if semester in self.courses and any(course["code"] == course_code for course in self.courses[semester]):
            self.courses[semester] = [course for course in self.courses[semester] if course["code"] != course_code]
            print(f"Course {course_code} deleted for {self.name} in semester {semester}.")
        else:
            print(f"Course {course_code} not found for {self.name} in semester {semester}.")

    def get_courses_by_semester(self, semester):
        return self.courses.get(semester, [])
 
    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            data = {
                "student_id": self.student_id,
                "name": self.name,
                "courses": self.courses
            }
            json.dump(data, file)        