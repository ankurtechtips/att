import java.util.*;

class MainClass {
    public static void main(String[] args)
    {
        ArrayList<User> ar = new ArrayList<User>();
        ar.add(new User(111, "bob"));
        ar.add(new User(111, "anil"));
        ar.add(new User(105, "sunil"));

        System.out.println("Unsorted");
        for (int i = 0; i < ar.size(); i++)
            System.out.println(ar.get(i));

        Collections.sort(ar, new Sort_Users());

        System.out.println("\nSorted ");
        for (int i = 0; i < ar.size(); i++)
            System.out.println(ar.get(i));
    }
}
class User {
    int Userid;
    String name;
    public User(int userid, String name)
    {
        this.Userid = userid;
        this.name = name;

    }
    public String toString()
    {
        return this.Userid + " " + this.name + " ";
    }
}
class Sort_Users implements Comparator<User> {

    public int compare(User a, User b) {
        if (a.Userid == b.Userid) {
            return a.name.compareTo(b.name);
        } else {
            return a.Userid - b.Userid;
        }
    }
}
