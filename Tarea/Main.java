package Tarea;
import Tarea.Classes.Job;

public class Main {

    public static void main(String[] args) {
        var object_job = new Job(20000, "Software Engineer", "We are looking for a software engineer to join our team", "Guadalajara", "TechCompany", 41);

        object_job.job_is_hiring();
        object_job.job_is_not_hiring();
        object_job.job_is_open();
        object_job.new_job_position(object_job.job_salary, object_job.job_position, object_job.job_location, object_job.job_company);
        object_job.will_employee_get_raise(object_job.job_position, object_job.job_working_hours);
        object_job.job_salary_increase(object_job.job_salary, object_job.job_position, object_job.job_working_hours);
    }

}
