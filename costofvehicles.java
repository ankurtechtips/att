class Parts
{
    int tyre,glass;
}
class Car extends Parts
{
    void carcost(int notyre,int noglass)
    {
        int tyre=5000;
        int glass=4000;
        int t=(tyre*notyre)+(glass*noglass);
        System.out.println("Cost for Car = "+t);
    }
}
class Bike extends Parts
{
    void bikecost(int notyre, int noglass)
    {
        int tyre=3000;
        int glass=1500;
        int t=(tyre*notyre)+(glass*noglass);
        System.out.println("Cost for Bike = "+t);
    }
}
class Truck extends Parts
{
    void truckcost(int notyre, int noglass)
    {
        int tyre=8000;
        int glass=6000;
        int t=(tyre*notyre)+(glass*noglass);
        System.out.println("Cost for Truck = "+t);
    }
}
public class Test
{
    public static void main(String args[])
    {
        Car c = new Car();
        c.carcost(5,4);
        Bike b = new Bike();
        b.bikecost(2,1);
        Truck tr = new Truck();
        tr.truckcost(6,2);
    }
}