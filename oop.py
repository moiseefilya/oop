import abc


class Person(abc.ABC):

    @abc.abstractmethod
    def sr_grade(self):
        pass

    def __lt__(self, other):
        return self.sr_grade < other.sr_grade

    def __gt__(self, other):
        return self.sr_grade > other.sr_grade


class Student(Person):
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def grades_app(self, lec):
        course = input('Введите курс: ')
        if course not in self.courses_in_progress:
            print('Вы ввели несуществующий курс!')
            return
        grade = int(input('Введите Вашу оценку(1-10): '))
        if isinstance(lec, Lecturer) and course in self.courses_in_progress and course in lec.courses_attached:
            if course in lec.grades:
                lec.grades[course] += [grade]
            else:
                lec.grades[course] = [grade]
        else:
            return 'Ошибка'

    @property
    def sr_grade(self):
        res = 0
        for val in self.grades.values():
            if len(val) != 0:
                sr = sum(val) / len(val)
                res += sr
            else:
                return 0
        return res / len(self.grades.values())

    def __str__(self):
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Средняя оценка: {self.sr_grade}\n' \
              f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)} \n' \
              f'Завершенные курсы: {", ".join(self.finished_courses)}'
        return res


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    @property
    def sr_grade(self):  # подсчет среднего значения оценок
        res = 0
        for val in self.grades.values():
            if len(val) != 0:
                sr = sum(val) / len(val)
                res += sr
            else:
                return 0
        return res/len(self.grades.values())

    def __str__(self):
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Средняя оценка за лекции: {self.sr_grade}'
        return res


class Reviewer(Mentor):
    def rate_hw(self, student):
        course = input('Введите курс: ')
        grade = int(input('Введите оценку: '))
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}'
        return res


peter = Student('Peter', 'Hard', 'man')
mary = Student('Mary', 'Kay', 'girl')
john = Lecturer('John', 'Speed')
maks = Lecturer('Maks', 'Lee')
stefan = Reviewer('Stefan', 'Storm')
susan = Reviewer('Susan', 'Williams')

peter.finished_courses = ['Data Base', 'Введение в программирование']
peter.courses_in_progress += ['Python', 'Git']
peter.grades['Python'] = [8, 7, 9, 10]

john.courses_attached += ['Python', 'Git', 'Java']
john.grades['Python'] = [3, 5, 6]
maks.grades['Python'] = [7, 4, 8, 6]
stefan.courses_attached += ['Python', 'Git']

mary.grades['Python'] = [10, 10, 10, 10]
mary.courses_in_progress += ['Python']

peter.grades_app(john)
stefan.rate_hw(peter)

print(peter)
print(john)
print(stefan)


students_list = [peter, mary]
lecture_list = [john, maks]


def student_rate(student_list, course):
    summa = 0
    count = 0
    res = 0
    for student in student_list:
        for grade in student.grades.get(course):
            if course in student.grades:
                summa += grade
                count += 1
                res = summa / count
    return f'Средняя оценка у студентов по курсу {course} - {res}'


def lecture_rate(lecture_list, course):
    summa = 0
    count = 0
    res = 0
    for lecture in lecture_list:
        for grade in lecture.grades.get(course):
            if course in lecture.grades:
                summa += grade
                count += 1
                res = summa / count
    return f'Средняя оценка у лекторов по курсу {course} - {res}'


print(student_rate(students_list, 'Python'))
print(lecture_rate(lecture_list, 'Python'))
