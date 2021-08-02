## ДЗ по занятию ООП
# class Person:

class Courses:
    def __init__(self):
        self.course_in_progress = []
        self.course_finished = []
        self.courses_attached = []
        self.grades = {}

    def list_courses(self, type='in progress'):
        if type == 'in progress':
            return ' '.join(x for x in self.course_in_progress)
        elif type == 'finished':
            return ' '.join(x for x in self.course_finished)
        else:
            print('Ошибка')

    def calc_av_grade(self):
        sum_grad = 0
        count_grad = 0
        for grade in self.grades:
            sum_grad += sum(x for x in grade[course])
            count_grad += len(grade[course])
        return 0 if count_grad == 0 else round(sum_grad / count_grad,2)


class Student(Courses):
    def __init__(self, name, surname, gender=None):
        #        Courses.__init__(self)
        self.name = name
        self.surname = surname
        self.gender = gender
        self.course_in_progress = []
        self.course_finished = []
        self.courses_attached = []
        self.grades = {}

    def list_courses(self, type='in progress'):
        if type == 'in progress':
            return ' '.join(x for x in self.course_in_progress)
        elif type == 'finished':
            return ' '.join(x for x in self.course_finished)
        else:
            print('Ошибка')

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.course_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    # def list_courses_in_progress(self):
    #  return ' '.join(x for x in self.course_in_progress)

    def __str__(self):
        st = 'Имя: ' + self.name + '\n'
        st += 'Фамилия: ' + self.surname + '\n'
        st += 'Средняя оценка за домашние задания: ' + str(self.calc_av_grade()) + '\n'
        st += 'Курсы в процессе обучения: ' + self.list_courses() + '\n'
        st += 'Законченные курсы : ' + self.list_courses('finished')
        return st

    def calc_av_grade(self):
        sum_grad = 0
        count_grad = 0
        for grade in self.grades.values():
            sum_grad += sum(x for x in grade)
            count_grad += len(grade)
        return 0 if count_grad == 0 else round(sum_grad / count_grad,2)

    def __gt__(self, other):
        if isinstance(other, Student):
            return self.calc_av_grade() > other.calc_av_grade()


class Mentor():
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Reviewer(Mentor):
    def __init__(self, name, surname):
        #        Mentor().__init__(self)
        super().__init__(name, surname)
        self.name = name
        self.surname = surname

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.course_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        st = 'Имя: ' + self.name + '\n'
        st += 'Фамилия: ' + self.surname
        return st


class Lecturer(Mentor, Courses):
    def __init__(self, name, surname):
        #        Courses.__init__(self)
        super().__init__(name, surname)
        self.name = name
        self.surname = surname
        self.grades = {}

    def __str__(self):
        st = 'Имя: ' + self.name + '\n'
        st += 'Фамилия: ' + self.surname + '\n'
        st += 'Средняя оценка за лекции: ' + str(self.calc_av_grade())
        return st

    def calc_av_grade(self):
        sum_grad = 0
        count_grad = 0
        for grade in self.grades.values():
            sum_grad += sum(x for x in grade)
            count_grad += len(grade)
        return 0 if count_grad == 0 else round(sum_grad / count_grad,2)

    def __gt__(self, other):
        if isinstance(other, Lecturer):
            return self.calc_av_grade() > other.calc_av_grade()


def calc_av_grade_stud(*args_stud, course=None):
    sum_grad = 0
    count_grad = 0
    if all(isinstance(x, Student) for x in args_stud):
        for st in args_stud:
            if course and course in st.grades.keys():
                sum_grad += sum(x for x in st.grades[course])
                count_grad += len(st.grades[course])
            else:
                print(f"Студент {st.name} {st.surname} не имеет оценок по курсу {course}")
        return 0 if count_grad == 0 else round(sum_grad / count_grad,2)
    else:
        print('Не все являются студентами')


def calc_av_grade_lect(*args_lect, course=None):
    sum_grad = 0
    count_grad = 0
    if all(isinstance(x, Lecturer) for x in args_lect):
        for st in args_lect:
            if course and course in st.grades.keys():
                sum_grad += sum(x for x in st.grades[course])
                count_grad += len(st.grades[course])
            else:
                print(f"Лектор {st.name} {st.surname} не имеет оценок по курсу {course}")
        return 0 if count_grad == 0 else round(sum_grad / count_grad,2)
    else:
        print('Не все являются лекторами')


best_student = Student('Roy', 'Egan')
best_student.course_in_progress += ['Python']
best_student.course_in_progress += ['Git']
best_student.course_finished += ['Введение в программирование']

cool_reviewer = Reviewer('Mick', 'Hard')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.rate_hw(best_student, 'Python', 8)
cool_reviewer.rate_hw(best_student, 'Python', 9)
cool_reviewer.rate_hw(best_student, 'Python', 7)

some_student = Student('John', 'Doo')
some_student.course_in_progress += ['Python']
some_student.course_in_progress += ['Git']
some_student.course_finished += ['Введение в программирование']


cool_reviewer2 = Reviewer('Pitt', 'Brooks')
cool_reviewer2.courses_attached += ['Python']
cool_reviewer2.rate_hw(some_student, 'Python', 7)
cool_reviewer2.rate_hw(some_student, 'Python', 8)

cool_lecturer = Lecturer('Bobby', 'Charlton')
cool_lecturer.courses_attached += ['Python']
best_student.rate_hw(cool_lecturer, 'Python', 9)
best_student.rate_hw(cool_lecturer, 'Python', 8)

cool_lecturer2 = Lecturer('Bobby', 'Moor')
cool_lecturer2.courses_attached += ['Git']
cool_lecturer2.courses_attached += ['Python']
best_student.rate_hw(cool_lecturer2, 'Git', 9)
best_student.rate_hw(cool_lecturer2, 'Git', 8)
some_student.rate_hw(cool_lecturer2, 'Git', 8)
some_student.rate_hw(cool_lecturer2, 'Git', 7)

print(best_student)
print(some_student)
print(best_student > some_student)
print('Средние оценки студентов: ', calc_av_grade_stud(best_student, some_student, course='Python'))

print(cool_reviewer)
print(cool_reviewer2)

print(cool_lecturer)
print(cool_lecturer2)
print(cool_lecturer > cool_lecturer2)
print('Средние оценки лекторов: ', calc_av_grade_lect(cool_lecturer, cool_lecturer2, course='Python'))
print('Средние оценки лекторов: ', calc_av_grade_lect(cool_lecturer, cool_lecturer2, course='Git'))


