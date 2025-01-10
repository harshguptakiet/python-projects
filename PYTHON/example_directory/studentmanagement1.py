class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.marks = {}

    def add_mark(self, subject, score):
        self.marks[subject] = score

    def calculate_average(self):
        total_marks = sum(self.marks.values())
        return total_marks / len(self.marks) if self.marks else 0

    def display_info(self):
        print(f"Student: {self.name}, Roll No: {self.roll_no}")
        print("Marks:")
        for subject, score in self.marks.items():
            print(f"{subject}: {score}")
        print(f"Average score: {self.calculate_average():.2f}")
        print("_" * 30)


# Creating student 1 and student 2 objects
student1 = Student("Alice", "101")
student1.add_mark("Math", 95)
student1.add_mark("Science", 88)
student1.add_mark("History", 75)

student2 = Student("Bob", "102")
student2.add_mark("Math", 85)
student2.add_mark("Science", 78)
student2.add_mark("History", 92)

# Displaying information of both students
student1.display_info()
student2.display_info()
