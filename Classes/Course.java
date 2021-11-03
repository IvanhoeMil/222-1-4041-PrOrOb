package Classes;

public class Course {
    public String subject;
    public int code;
    public int level;
    public String teacher;

    public Course(String subject, int code, int level, String teacher) {
        super();
        this.subject = subject;
        this.code = code;
        this.level = level;
        this.teacher = teacher;
    }

    public String teacher_subject(String subject, String teacher) {
        return teacher+" teaches "+subject;
    }

    public int next_level(int level, int code) {
        return level+1;
    }

    public static void hello_world() {
        System.out.println("Hello World!");
    }

    public void course_info() {
        System.out.println("All courses must have a subject, code, level and teacher");
    }


}
