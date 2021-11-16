package Tarea.Classes;

public class Job {
    public float job_salary;
    public String job_position;
    public String job_description;
    public String job_location;
    public String job_company;
    public int job_working_hours;

    public Job(float job_salary, String job_position, String job_description, String job_location, String job_company, int job_working_hours) {
        this.job_salary = job_salary;
        this.job_position = job_position;
        this.job_description = job_description;
        this.job_location = job_location;
        this.job_company = job_company;
        this.job_working_hours = job_working_hours;
    }

    public void job_is_hiring() {
        System.out.println("+Job is hiring");
    }

    public void job_is_not_hiring() {
        System.out.println("+Job is not hiring");
    }

    public void job_is_open() {
        System.out.println("+Job is open");
    }

    public void new_job_position(float job_salary, String job_position, String job_location, String job_company) {
        System.out.println("+There is a new job position at " +job_company+" with a starting salary of $"+job_salary+". Company is located in "+job_location+". They're looking for a "+job_position);
    }

    public void will_employee_get_raise(String job_position, int job_working_hours){
        if(job_working_hours > 40 && job_position.equals("Software Engineer")){
            System.out.println("+The employee will get a raise because they work more than 40 hours per week");
        }else{
            System.out.println("+The employee will not get a raise");
        }
    }

    public void job_salary_increase(float job_salary, String job_position, int job_working_hours){
        if(job_working_hours > 40 && job_position.equals("Software Engineer")){
            job_salary = job_salary * 1.25f;
            System.out.println("+The salary for the "+job_position+" position will increase to $"+job_salary+" because the employee works more than 40 hours per week");
        }else{
            System.out.println("+The salary for the "+job_position+" position has not increased");
        }
    }



}
