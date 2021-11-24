class Person:
    def __init__ (self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def say_hello_user(self, username):
        return ("Hello, " + username)

    def say_hello_person(self, first_name, last_name):
        return ("Hello, " + first_name + " " + last_name)


class Student(Person):
    def __init__(self, first_name, last_name):
        #Person.__init__(self,first_name, last_name)
        super().__init__(first_name, last_name)
        # self.nick_name  = nick_name

    def student_id(self, student_id):
        return ("Matricula: " + student_id)


class Teacher(Student, Person):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)

    def teacher_id(self, teacher_id):
        return ("Matricula: " + teacher_id)
        
    def greet_student(self, student_name):
        return ("Hello, student " + student_name+ " Im your teacher "+self.first_name+ " "+self.last_name)

        

object_person = Person("Ivan", "de Santiago")
object_student = Student("Carlos", "Plascencia")
object_teacher = Teacher("Luis", "Guerra")

print(object_student.first_name, " ", object_student.last_name)

print(object_person.first_name, " ", object_person.last_name)


print(object_student.say_hello_user("Carlos"))

print(object_student.student_id("12345"))

print(object_student.say_hello_person(object_student.first_name, object_student.last_name))

print(object_teacher.greet_student(object_student.first_name))

#print(object_student.say_hello_user(object_teacher))

class Basic_Student(Student):
    def __init__(self, first_name, last_name, age, school_grade):
        self.age = age
        self.school_grade = school_grade
        #super().__init__(first_name, last_name)
        Person.__init__(self,first_name, last_name)

    def basic_student_school_grade(self, school_grade):
        return ("Student "+object_basic_student_person.first_name+" courses grade: " + school_grade)

    def basic_student_age(self, age):
        return ("Student is "+object_basic_student_person.first_name+" "+object_basic_student_person.last_name+" Age: " + age)

object_basic_student_person = Basic_Student("Carlitos", "Plascencia", "5", "3")

#object_basic_student = Basic_Student(object_person.first_name,  "20", "10")

object_student = Basic_Student("Carlitos", "Plascencia", "22", "3")


print(object_basic_student_person.basic_student_age(object_basic_student_person.age))

print(object_basic_student_person.basic_student_school_grade(object_basic_student_person.school_grade))

#print(object_basic_student.say_hello_person(object_basic_student_person.first_name, object_basic_student_person.last_name))
