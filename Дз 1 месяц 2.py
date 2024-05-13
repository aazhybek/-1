class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married
    def introduce_myself(self, introducing):
        print(f'Fullname:{self.fullname},Age:{self.age}, Married:{self.is_married}')

class Student(Person):
    def __init__(self,fullname, age, is_married, marks):
        super().__init__(fullname, age, is_married)
        self.marks = marks

    def calculate_marks(self):
        total_marks = sum(self.marks.values())
        average_marks = total_marks / len(self.marks)
        return average_marks


class Teacher(Person):
    def __init__(self, fullname, age, is_married, experience, base_salary):
        super().__init__(fullname, age, is_married)
        self.experience = experience
        self.base_salary = base_salary

    def calculate_salary(self):
        bonus_percentage = 0.05 * max(0, self.experience - 3)
        bonus_amount = self.base_salary * bonus_percentage
        total_salary = self.base_salary + bonus_amount
        return total_salary

def create_students():
    student1 = Student("Azhybek", 19, False,{"Math": 90, "Science": 85, "History": 90})
    student2 = Student("Zhantai", 25, True, {"Math": 100, "Science": 84, "History": 79})
    student3 = Student("Nuradil", 27, False, {"Math": 100, "Science": 100, "History": 100})
    students = [student1, student2, student3]
    return students

teacher = Teacher("Mr. Kairat",35, True, 10, 60000)


teacher.introduce_myself("Teacher")
print(f"Salary: {teacher.calculate_salary()}")

students_list = create_students()
for student in students_list:
    student.introduce_myself("Student")
    print(f"Avarage Mark: {student.calculate_marks()}")