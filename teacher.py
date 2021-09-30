class Teacher:
    subject = "Programming"

    def greet_students(self, subject):
        print("Welcome to "+subject+" class")


teacher_one = Teacher()
teacher_one.greet_students(teacher_one.subject)