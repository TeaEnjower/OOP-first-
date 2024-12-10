class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        
    def Lecturer_rating(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and (course in self.finished_courses or course in self.courses_in_progress) and course in lecturer.courses_attached:   
            if course in lecturer.grades:
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]
            return lecturer.grades    
        else:
            return 'Ошибка'
        
    def student_average_rating(self):
        total_grades = 0
        count = 0

        for course, grades in self.grades.items():
            total_grades += sum(grades)
            count += len(grades)

        return round(total_grades / count, 1) if count > 0 else 0

    def __eq__(self, other):
        return self.student_average_rating() == other.student_average_rating()
        
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.student_average_rating()}\nКурсы в процессе изучения: {self.finished_courses}\nЗавершённые курсы: {self.finished_courses}'
        

class Mentor:

    def __init__(self, name, surname, courses_attached=None):
        if courses_attached is None:
            courses_attached = []
        self.name = name
        self.surname = surname
        self.courses_attached = courses_attached
    
    def getName(self):
        return self.name +  ' ' + self.surname
        
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

class Lecturer(Mentor):

    def __init__(self, name, surname, courses_attached=None):
        super().__init__(name, surname, courses_attached)
        if courses_attached is None:
            courses_attached = {}
        self.grades = {}

    def Lecturer_average_rating(self):
        total_grades = 0
        count = 0

        for course, grades in self.grades.items():
            total_grades += sum(grades)
            count += len(grades)

        return round(total_grades / count, 1) if count > 0 else 0

    def __eq__(self, other):
        return self.Lecturer_average_rating == other.Lecturer_average_rating
    
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.Lecturer_average_rating()}'


class Reviewer(Mentor):

    def __init__(self, name, surname, courses_attached=None):
        super().__init__(name, surname, courses_attached)
    
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

lector_John = Lecturer("John", "Nort", ["Python", "C++", "Java"]) 

lector_Roman = Lecturer("Roman", "Ivanov", ["Python", "Probability Theory"])

student_Cole = Student("Cole", "Birminghem", "Male")
student_Cole.finished_courses += ["C++", "Python", "Java", "Probability Theory"]
student_Cole.courses_in_progress += ["Python", "C++", "Java"]
student_Cole.Lecturer_rating(lector_John, "Python", 10)
student_Cole.Lecturer_rating(lector_John, "C++", 9)
student_Cole.Lecturer_rating(lector_John, "Java", 10)

student_Jane = Student("Jane", "Miller", "Female")
student_Jane.finished_courses += ["C++", "Python", "Java", "Probability Theory"]
student_Jane.courses_in_progress += ["Python", "C++", "Java"]
student_Jane.Lecturer_rating(lector_John, "Python", 10)
student_Jane.Lecturer_rating(lector_John, "C++", 8)
student_Jane.Lecturer_rating(lector_John, "Java", 9)
 
cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python', 'Java', 'Probability Theory']
cool_mentor.rate_hw(student_Jane, 'Python', 10)
cool_mentor.rate_hw(student_Jane, 'Java', 7)
cool_mentor.rate_hw(student_Jane, 'Probability Theory', 8)
cool_mentor.rate_hw(student_Cole, 'Python', 10)
cool_mentor.rate_hw(student_Cole, 'Java', 10)

amazing_mentor = Mentor('Sergey', 'Balakirev')
amazing_mentor.courses_attached += ['Python', 'C++', 'Probability Theory']
amazing_mentor.rate_hw(student_Jane, 'Python', 10)
amazing_mentor.rate_hw(student_Jane, 'Java', 7)
amazing_mentor.rate_hw(student_Jane, 'Probability Theory', 8)
amazing_mentor.rate_hw(student_Cole, 'Python', 10)
amazing_mentor.rate_hw(student_Cole, 'Java', 10)
amazing_mentor.rate_hw(student_Cole, 'Probability Theory', 7)

print(lector_John, end="\n\n")
print(student_Jane, end="\n\n")
print(student_Cole, end="\n\n")
print(cool_mentor, end="\n\n")
print(student_Cole.__eq__(student_Jane))
print(lector_John.__eq__(lector_Roman), end="\n\n")

def Students_course(students_list, course):
    total_grades = 0
    count = 0

    for student in students_list:
        if course in student.grades:
            total_grades += sum(student.grades[course])
            count += len(student.grades[course])

    return round(total_grades / count, 1) if count > 0 else 0

def Lecturers_course(lecturers_list, course):
    total_grades = 0
    count = 0

    for lecturers in lecturers_list:
        if course in lecturers.grades:
            total_grades += sum(lecturers.grades[course])
            count += len(lecturers.grades[course])

    return round(total_grades / count, 1) if count > 0 else 0

print(Students_course([student_Cole, student_Jane], "Java"))
print(Lecturers_course([lector_John, lector_Roman], "Java"))