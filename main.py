
class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecture, course, grade):
        if isinstance(lecture, Lecturer) and course in self.courses_in_progress and course in lecture.courses_attached:
            if course in lecture.grades:
                lecture.grades[course] += [grade]
            else:
                lecture.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grate(self):
        grades_amount = 0
        grades_sum = 0
        average = 0
        for grades in self.grades.values():
            grades_sum += sum(grades)
            grades_amount += len(grades)
        if grades_amount != 0:
            average = grades_sum / grades_amount
        return average

    def __str__(self):
        res = []
        res.append(f'Имя: {self.name}')
        res.append(f'Фамилия: {self.surname}')
        res.append(f'Средняя оценка за домашние задания: {self.average_grate():.2}')
        res.append(f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}')
        res.append(f'Завершенные курсы: {", ".join(self.finished_courses)}')

        return '\n'.join(res)

    def __lt__(self, other):
        return self.average_grate() < other.average_grate()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grate(self):
        grades_amount = 0
        grades_sum = 0
        average = 0
        for grades in self.grades.values():
            grades_sum += sum(grades)
            grades_amount += len(grades)
        if grades_amount != 0:
            average = grades_sum / grades_amount
        return average

    def __str__(self):
       return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grate():.2}'

    def __lt__(self, other):
        return self.average_grate() < other.average_grate()

class Reviewer(Mentor):

    def rate_student(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

def students_average_rate(students, course):
    grades_amount = 0
    grades_sum = 0
    average = 0
    for student in students:
        if course in student.grades:
            grades_sum += sum(student.grades[course])
            grades_amount += len(student.grades[course])
    if grades_amount != 0:
        average = grades_sum / grades_amount
    return average

def lecturers_average_rate(lecturers, course):
    grades_amount = 0
    grades_sum = 0
    average = 0
    for lecturer in lecturers:
        if course in lecturer.grades:
            grades_sum += sum(lecturer.grades[course])
            grades_amount += len(lecturer.grades[course])
    if grades_amount != 0:
        average = grades_sum / grades_amount
    return average

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    student_1 = Student('Student', 'First')
    student_1.courses_in_progress += ['Python']
    student_1.courses_in_progress += ['JAVA']
    student_1.finished_courses += ['C++']

    student_2 = Student('Student', 'Second')
    student_2.courses_in_progress += ['Python']
    student_2.courses_in_progress += ['JAVA']

    # reviewer_1
    reviewer_1 = Reviewer('Reviewer', 'First')
    reviewer_1.courses_attached += ['Python']
    reviewer_1.courses_attached += ['JAVA']
    reviewer_1.courses_attached += ['C++']

    reviewer_1.rate_student(student_1, 'Python', 10)
    reviewer_1.rate_student(student_1, 'JAVA', 8)
    reviewer_1.rate_student(student_1, 'C++', 5)

    reviewer_1.rate_student(student_2, 'Python', 7)
    reviewer_1.rate_student(student_2, 'JAVA', 7)

    # reviewer_2
    reviewer_2 = Reviewer('Reviewer', 'Second')
    reviewer_2.courses_attached += ['JAVA']

    reviewer_2.rate_student(student_1, 'JAVA', 6)
    reviewer_2.rate_student(student_2, 'JAVA', 6)

    # lecturer_1
    lecturer_1 = Lecturer('Lecturer', 'First')
    lecturer_1.courses_attached += ['Python']
    lecturer_1.courses_attached += ['JAVA']

    student_1.rate_lecture(lecturer_1, 'Python', 8)
    student_1.rate_lecture(lecturer_1, 'JAVA', 10)
    student_2.rate_lecture(lecturer_1, 'Python', 10)

    # lecturer_2
    lecturer_2 = Lecturer('Lecturer', 'Second')
    lecturer_2.courses_attached += ['Python']
    lecturer_2.courses_attached += ['JAVA']

    student_1.rate_lecture(lecturer_2, 'Python', 8)
    student_2.rate_lecture(lecturer_2, 'Python', 10)
    student_2.rate_lecture(lecturer_2, 'JAVA', 6)

    # print
    print('\nStudents:')
    print(f'\n{student_1}')
    print(f'\n{student_2}')

    print('\nReviewers:')
    print(f'\n{reviewer_1}')
    print(f'\n{reviewer_2}')

    print('\nLecturers:')
    print(f'\n{lecturer_1}')
    print(f'\n{lecturer_2}')

    # __lt__
    print('\n__lt__:\n')
    print(f'student_1 less than student_2: {student_1 < student_2}')
    print(f'lecturer_1 less than lecturer_2: {lecturer_1 < lecturer_1}')

    print()
    students = [student_1, student_2]
    print(f'Python (students): {students_average_rate(students, "Python")}')

    lecturers = [lecturer_1, lecturer_2]
    print(f'Python (lecturers): {lecturers_average_rate(lecturers, "Python")}')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
