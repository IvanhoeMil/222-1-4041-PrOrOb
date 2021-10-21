package Classes;

public class Human {
    //  Attributes
    int born_year = 1999;

    //Methods
    public void say_hello(){
        System.out.println("Hello!");
    }

    public String say_hello_user(String user_name){
        return "Hello "+user_name;
    }

    public int born_year(int year){
        return year;
    }

}
