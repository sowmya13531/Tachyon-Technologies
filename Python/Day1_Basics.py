"""
# Variables
name = "Sowmya"     # string
college = "IIIT Ongole"
age = 1000           # integer
height = 5.4        # float
is_student = True   # boolean

# Input & Outputs
name = input("Enter your name: ")
print("Hello", name)


#Lists
names = ['sowmya', 'poojitha' , 'syamini', 'kavya', 'deepu']
print(names[0])


#Dictionaries
names = {
    "sowmya": "kanithi",
    "age": 678
}
print(names)

#conditions
age = 20
if age > 18:
    print("Eligible to vote")
else:
    print("Not")

# Loops
for i in range(10):
    print(i)

#Functions
def greet(name):
    return "Hello" + name

#List comprehension
nums = [1, 2, 3, 4]

even = [n for n in nums if n % 2 == 0]

# Student Filter System
students = [
    {"name": "Sowmya", "marks": 85},
    {"name": "Rahul", "marks": 60},
    {"name": "Anjali", "marks": 90}
]

def get_top_students(data):
    return [s for s in data if s["marks"] > 80]

top = get_top_students(students)

for s in top:
    print(s["name"], s["marks"])
    """

# Little Mini Project
# Step 1: Create empty list
students = []

# Step 2: Take number of students
n = int(input("Enter number of students: "))

# Step 3: Loop to take input
for i in range(n):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    
    student = {
        "name": name,
        "marks": marks
    }
    
    students.append(student)

# Step 4: Function to find topper
def find_topper(data):
    topper = data[0]
    
    for student in data:
        if student["marks"] > topper["marks"]:
            topper = student
    
    return topper

# Step 5: Get topper
top_student = find_topper(students)

# Step 6: Print result
print("\nTopper is:")
print(top_student["name"], "with", top_student["marks"], "marks")