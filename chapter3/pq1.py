class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

student1 = Student("Shaurya", 20)
student1.display()
student2 = Student("Shivam", 22)
student2.display()