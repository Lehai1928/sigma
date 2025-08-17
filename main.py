class Student:
    def __init__(self, name):
        self.name = name
        self.grades = {"Toan": [], "Van": [], "Anh": []}

    def add_grade(self, subject, grade):
        if subject in self.grades:
            self.grades[subject].append(grade)
        else:
            print(f"Môn {subject} chưa có trong hệ thống.")

    def calculate_average(self):
        all_grades = []
        for subject in self.grades.values():
            all_grades.extend(subject)
        if not all_grades:
            return 0
        return sum(all_grades) / len(all_grades)

    def calculate_subject_average(self, subject):
        if subject in self.grades and len(self.grades[subject]) > 0:
            return sum(self.grades[subject]) / len(self.grades[subject])
        return 0


class GradeManager:
    def __init__(self):
        self.students = []

    def add_student(self, name):
        self.students.append(Student(name))

    def record_grade(self, name, subject, grade):
        for student in self.students:
            if student.name == name:
                student.add_grade(subject, grade)
                return True
        return False

    def calculate_average_all(self):
        if len(self.students) == 0:
            return 0
        total = sum(student.calculate_average() for student in self.students)
        return total / len(self.students)

    def save_data(self, filename):
        with open(filename, "w", encoding="utf-8") as f:
            for student in self.students:
                avg = student.calculate_average()
                f.write(f"{student.name}: Trung bình chung = {avg:.2f}\n")
                for subject, grades in student.grades.items():
                    if grades:
                        f.write(f"   {subject}: {student.calculate_subject_average(subject):.2f}\n")
                f.write("\n")


def main():
    manager = GradeManager()

    while True:
        print("\n===== Menu =====")
        print("1. Add a new student")
        print("2. Record a grade for a student")
        print("3. Calculate the average grade of all students")
        print("4. Save the data to a file")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            name = input("Enter student name: ")
            manager.add_student(name)
            print(f"Student '{name}' added successfully.")

        elif choice == "2":
            name = input("Enter student name: ")
            subject = input("Enter subject (Toan/Van/Anh): ")
            try:
                grade = float(input("Enter grade: "))
                if manager.record_grade(name, subject, grade):
                    print("Grade recorded successfully.")
                else:
                    print("Student not found.")
            except ValueError:
                print("Invalid grade. Please enter a number.")

        elif choice == "3":
            avg = manager.calculate_average_all()
            print(f"The average grade of all students: {avg:.2f}")

        elif choice == "4":
            filename = input("Enter filename to save data: ")
            manager.save_data(filename)
            print(f"Data saved to {filename}")

        elif choice == "5":
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please select 1-5.")


if __name__ == "__main__":
    main()
