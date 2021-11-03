import Classes.Course;

public class Main2 {

    public static void main(String[] args) {
        //System.out.println("OOP 1st Java Exam");
        Course first_course = new Course("Object Oriented Programming", 100, 4, "Luis Guerra");
        Course secondCourse = new Course("Structured Programming", 50, 3, "Martin Onesimo");

        System.out.println(first_course.teacher_subject(first_course.subject, first_course.teacher));
        System.out.println("Next Course Level is "+secondCourse.next_level(secondCourse.level,secondCourse.level));

        Course.hello_world();
        first_course.course_info();
    }
}
