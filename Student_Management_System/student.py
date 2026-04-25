class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def to_dict(self):
        return {
            "name": self.name,
            "marks": self.marks
        }