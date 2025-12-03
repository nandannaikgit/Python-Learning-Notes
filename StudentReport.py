class Student:
    def __init__(self,roll_no, name):
        self.name = name
        self.roll_no = roll_no
        self.__marks = {}
        
    def get_marks(self):
        return self.__marks
        
    def add_marks(self, subject, marks):
        self.__marks[subject] = marks
        
    def calculate_average(self):
        total = 0
        for marks in self.__marks.values():
            total += marks
        average = total/len(self.__marks)
        print(f"{self.name}'s average: {average}")
        return average
       
    def is_passed(self):
        has_failed = any(mark<35 for mark in self.__marks.values())
        if has_failed:
            print(f"{self.name} has failed.")
        else:
            print(f"{self.name} has passed.")
            
    def calculate_grade(self):
        print("Grade: end=""")
        # TODO: Fix this. Not working properly.
        percentage = self.calculate_average() * 100
        if percentage >= 90:
            print("A")
        elif percentage >= 85:
            print("B")
        else:
            print("C")
            
            
class ReportCard:
    def generate(self, student: Student):
        print(f"Name: {student.name} \t Roll No: {student.roll_no}")
        print("-----Marks------")
        for subject,marks in student.get_marks().items():
            print(f"{subject} - {marks}")
        print("------------------")
        print(f"Average: {student.calculate_average()}")
        student.is_passed()
        student.calculate_grade()
  
class ClassRoom:
        def __init__(self, grade, section):
            self.grade = grade
            self.section = section
            self.__students = []
            
        def add_students(self, Student):
            self.__students.append(Student)
            
        def calculate_class_average(self):
            pass
        
        def get_student_list(self, i):
            for student in enumerate(self.__students):
                print(f"{student.roll_no}. {student.name}")
            
a = Student(1, "akash")
a.add_marks("Math", 95)
a.add_marks("Science", 34)

rc = ReportCard()
rc.generate()

c = ClassRoom("10","B")
 