class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.lecturer_grades:
                lecturer.lecturer_grades[course] += [grade]
            else:
                lecturer.lecturer_grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.SGPA()}\nКурсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}'

    def SGPA(self):
        total_grades = 0
        count = 0
        for value in self.grades.values():
            if isinstance(value, list):
                for grades in value:
                    total_grades += grades
                    count += 1
            else:
                total_grades += value
                count += 1
        if count > 0:
            result = total_grades / count
            return result
        else:
            return 0

    def __lt__(self, other):
        if self.SGPA() < other.SGPA():
            return f'Первый студент имеет меньшую среднюю оценку за задания, чем второй'
        elif self.SGPA() > other.SGPA():
            return 'Второй студент имеет меньшую среднюю оценку за задания, чем первый'
        else:
            return 'Второй студент имеет такую же среднюю оценку за задания, что и первый'

    def subject_average(students, course_name):
        total_grades = 0
        count = 0
        for student in students:
            if course_name in student.grades:
                grades = student.grades[course_name]
                for grade in grades:
                    total_grades += grade
                    count += 1
        if count == 0:
            return 'Ошибка'
        else:
            return total_grades / count

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lecturer_grades = {}

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.GPA()}'

    def GPA(self):
        total_grades = 0
        count = 0
        for value in self.lecturer_grades.values():
            if isinstance(value, list):
                for grades in value:
                    total_grades += grades
                    count += 1
            else:
                total_grades += value
                count += 1
        if count > 0:
            result = total_grades / count
            return result
        else:
            return 0

    def __lt__(self, other):
        if self.GPA() < other.GPA():
            return 'Первый лектор имеет меньшую среднюю оценку за лекции, чем второй'
        elif self.GPA() > other.GPA():
            return 'Второй лектор имеет меньшую среднюю оценку за лекции, чем первый'
        else:
            return 'Второй лектор имеет такую же среднюю оценку за лекции, что и первый'

    def lectures_average(lecturers, course_name):
        total_grades = 0
        count = 0
        for lecturer in lecturers:
            if course_name in lecturer.lecturer_grades:
                grades = lecturer.lecturer_grades[course_name]
                for grade in grades:
                    total_grades += grade
                    count += 1
        if count == 0:
            return 'Ошибка'
        else:
            return total_grades / count


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

best_student = Student('Raul', 'Grime', 'Male')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['JS']
best_student.finished_courses += ['C++']

bad_student = Student('Gill', 'Edvard', 'Male')
bad_student.courses_in_progress += ['Python']
bad_student.courses_in_progress += ['JS']
bad_student.finished_courses += ['Java']


cool_mentor = Reviewer('Sam', 'Bale')
cool_mentor.courses_attached += ['Python']
cool_mentor.courses_attached += ['JS']

cool_men = Lecturer('Oleg', 'Bud')
cool_men.courses_attached += ['Python']
cool_men.courses_attached += ['JS']

bad_men = Lecturer('Nikita', 'Glo')
bad_men.courses_attached += ['Python']
bad_men.courses_attached += ['JS']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'JS', 10)
cool_mentor.rate_hw(best_student, 'JS', 7)

cool_mentor.rate_hw(bad_student, 'Python', 8)
cool_mentor.rate_hw(bad_student, 'Python', 8)
cool_mentor.rate_hw(bad_student, 'JS', 5)
cool_mentor.rate_hw(bad_student, 'JS', 3)

best_student.rate_lecture(cool_men, 'Python', 5)
bad_student.rate_lecture(cool_men, 'Python', 9)
best_student.rate_lecture(cool_men, 'JS', 4)
bad_student.rate_lecture(cool_men, 'JS', 6)

best_student.rate_lecture(bad_men, 'Python', 3)
bad_student.rate_lecture(bad_men, 'Python', 4)
best_student.rate_lecture(bad_men, 'JS', 7)
bad_student.rate_lecture(bad_men, 'JS', 1)

print(best_student.grades)
print(cool_men.lecturer_grades)

print(cool_mentor.__str__())

print(cool_men.GPA())
print(cool_men.__str__())
print(bad_men.GPA())
print(bad_men.__str__())

print(best_student.SGPA())
print(best_student.__str__())
print(bad_student.SGPA())
print(bad_student.__str__())

print(best_student.__lt__(bad_student))
print(bad_men.__lt__(cool_men))

print(Student.subject_average([best_student, bad_student], 'Python'))
print(Student.subject_average([best_student, bad_student], 'JS'))

print(Lecturer.lectures_average([cool_men, bad_men], 'Python'))
print(Lecturer.lectures_average([cool_men, bad_men], 'JS'))
