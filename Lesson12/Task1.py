import csv


class NameDescriptor:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if not value.istitle() or not value.replace(" ", "").isalpha():
            raise ValueError("ФИО должно состоять только из букв и начинаться с заглавной буквы")
        instance.__dict__[self.name] = value


class Student:
    name = NameDescriptor()

    def __init__(self, name, subjects_file):
        self.name = name
        self.subjects = {}
        self.load_subjects(subjects_file)

    def load_subjects(self, subjects_file):
        try:
            with open(subjects_file, "r", encoding="utf-8") as file:
                reader = csv.reader(file)
                for row in reader:
                    for subject in row:
                        self.subjects[subject.strip()] = {"grades": [], "test_scores": []}
        except FileNotFoundError:
            raise FileNotFoundError("Файл с предметами не найден")

    def add_grade(self, subject, grade):
        if subject not in self.subjects:
            raise ValueError(f"Предмет {subject} не найден")
        if not isinstance(grade, int) or not (2 <= grade <= 5):
            raise ValueError("Оценка должна быть целым числом от 2 до 5")
        self.subjects[subject]["grades"].append(grade)

    def add_test_score(self, subject, test_score):
        if subject not in self.subjects:
            raise ValueError(f"Предмет {subject} не найден")
        if not isinstance(test_score, int) or not (0 <= test_score <= 100):
            raise ValueError("Результат теста должен быть целым числом от 0 до 100")
        self.subjects[subject]["test_scores"].append(test_score)

    def get_average_test_score(self, subject):
        if subject not in self.subjects:
            raise ValueError(f"Предмет {subject} не найден")
        scores = self.subjects[subject]["test_scores"]
        return sum(scores) / len(scores) if scores else 0

    def get_average_grade(self):
        grades = [grade for subject in self.subjects.values() for grade in subject["grades"]]
        return sum(grades) / len(grades) if grades else 0

    def __str__(self):
        subjects_list = ", ".join(self.subjects.keys())
        return f"Студент: {self.name}\nПредметы: {subjects_list}"


student = Student("Иван Иванов", "subjects.csv")
student.add_grade("Математика", 4)
student.add_test_score("Математика", 85)
student.add_grade("История", 5)
student.add_test_score("История", 92)

average_grade = student.get_average_grade()
print(f"Средний балл: {average_grade}")

average_test_score = student.get_average_test_score("Математика")
print(f"Средний результат по тестам по математике: {average_test_score}")

print(student)
