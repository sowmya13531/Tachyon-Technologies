from student import Student

class StudentManager:
    def __init__(self, data):
        self.students = [Student(**s) for s in data]

    def add_student(self):
        name = input("Enter name: ")
        
        try:
            marks = int(input("Enter marks: "))
        except ValueError:
            print("Invalid marks!")
            return
        
        self.students.append(Student(name, marks))
        print("Student added!")

    def show_all(self):
        for s in self.students:
            print(s.name, s.marks)

    def find_topper(self):
        if not self.students:
            print("No students available")
            return
        
        topper = max(self.students, key=lambda x: x.marks)
        print("Topper:", topper.name, topper.marks)

    def update_student(self):
        name = input("Enter name to update: ")
        
        for s in self.students:
            if s.name == name:
                s.marks = int(input("Enter new marks: "))
                print("Updated!")
                return
        
        print("Student not found")

    def delete_student(self):
        name = input("Enter name to delete: ")
        
        for s in self.students:
            if s.name == name:
                self.students.remove(s)
                print("Deleted!")
                return
        
        print("Student not found")

    def to_list(self):
        return [s.to_dict() for s in self.students]