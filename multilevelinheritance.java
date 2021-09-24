class Country
{
    public void country()
    {
        System.out.println("This is a country");
    } 
}
class state extends Country
{
    public void state()
    {
        System.out.println("This is a state");
    }
}
public class city extends state
{
    public void city()
    {
        System.out.println("This is a city");
    }
     public static void main(String args[])
    {
        city con = new city();
        con.country();
        con.state();
        con.city();
    }
}