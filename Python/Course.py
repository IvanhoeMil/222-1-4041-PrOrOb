class Course:
    course_subject = "Object Oriented Programming"
    course_level = 4
    def __init__(self, course_subject, course_code, course_level, course_teacher):
        self.course_subject = course_subject
        self.course_code = course_code
        self.course_level = course_level
        self.course_teacher = course_teacher

my_course = Course("Object Oriented Programming", "100", 4, "Luis Guerra")
my_2nd_course = Course("Computer Centers Implementation", "200", 4, "Laura Topete")

def tuesday_courses(my_course, my_2nd_course):
    print("Tuesday courses are: " + my_course.course_subject + " and " + my_2nd_course.course_subject)

def tuesday_teachers(my_course, my_2nd_course):
    print("Tuesday teachers are: " + my_course.course_teacher + " and " + my_2nd_course.course_teacher)

tuesday_courses(my_course,my_2nd_course)
tuesday_teachers(my_course,my_2nd_course)

def course_subject():
    print("Current course subject is: " + Course.course_subject)

def course_level():
    print("All courses belong to " + str(Course.course_level) + "th level.")

course_subject()
course_level()