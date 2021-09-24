public class Test
{
    public static void main(String args[])
    {
        project p1 = new project(1000,2,5,100,30);
        p1.show_details();
    }
}

abstract class employee
{
    String position;
    int salary;
}
class developer extends employee
{
    developer(int x){
       salary=x;
       position="Developer";
    }
}
class manager extends employee
{
    manager(int x){
        salary=x;
        position="Manager";
    }
}
class project
{
    int cost;
    int budget;
    int No_of_managers;
    int No_of_developers;
    developer d;
    manager m;
    project(int cost, int No_of_managers, int No_of_developers, int salary_of_manager, int salary_of_developer)
    {
        this.cost=cost;
        this.No_of_managers=No_of_managers;
        this.No_of_developers=No_of_developers;
        d = new developer(salary_of_developer);
        m = new manager(salary_of_manager);

    }
    void budget_calculator()
    {
        this.budget = this.cost - (this.No_of_developers*this.d.salary+this.No_of_managers+this.m.salary);
    }
    void show_details()
    {
        budget_calculator();
        System.out.println("Project cost : "+cost);
        System.out.println("Project budget : "+budget);


    }

}