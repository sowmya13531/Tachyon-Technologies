"""
# File Handling
with open('test.txt', "w") as file:
    file.write("Hello Sowmya")


#JSON
#write JSON
# JSON = data format used in:
#APIs
#AI systems
#Databases
import json

data = [{"name": "Sowmya", "marks": 90}]

with open ("students.json", "w") as file:
    json.dump(data, file)


#Read JSON
with open("students.json", "r") as file:
    data = json.load(file)
print(data)


#error Handling
try:
    marks = int(input("Enter  marks: "))
except ValueError:
    print("Invalid input!")
"""

#Student JSON Manager
import json

FILE_NAME = "students.json"

#Load Existing data
def load_data():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

# Save Data
def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

#Add student
def add_student(data):
    name = input("Enter name:")
    try:
        marks = int(input("Enter marks: "))
    except ValueError:
        print("Invalid marks!")
        return

    student = {"name": name, "marks": marks}
    data.append(student)
    print("Student added!")

# Filter students
def show_top_students(data):
    top = [s for s in data if s["marks"] > 80]
    
    if not top:
        print("No top students found")
    else:
        for s in top:
            print(s["name"], s["marks"])

# Main menu
def main():
    data = load_data()
    
    while True:
        print("\n1. Add Student")
        print("2. Show Top Students")
        print("3. Exit")
        
        choice = input("Enter choice: ")

        if choice == "1":
            add_student(data)
            save_data(data)
        elif choice == "2":
            show_top_students(data)
        elif choice == "3":
            save_data(data)
            break
        else:
            print("Invalid choice")

main()
        
