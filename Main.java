import Classes.User;

public class Main{

    public static void main(String[] args)  {
        System.out.println("Learning OOP with Java");

        User object_user = new User(122110810, "Ivan de Santiago", "ivanodesantiago@gmail.com");

        System.out.println("User ID: " + object_user.id);
        System.out.println("Full Name: " + object_user.full_name);
        System.out.println("Personal email: " + object_user.personal_email);


    }

}