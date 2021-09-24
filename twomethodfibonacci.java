public class Fibonacci
{
    public static void main(String args[])
    {
        Fibonacci obj = new Fibonacci();
        for (int i=0;i<5;i++)
        {
                obj.tryme();
                obj.callme();
        }
    }
        int n1=0,n2=1,n3;
        public void calc()
        {
                n3=n1+n2;
                n1=n2;
                n2=n3; 
        }
        void tryme()
        {
            System.out.print(" "+n1);
            calc();
        }
        void callme()
        {
            System.out.print(" "+n1);
            calc();
        }
}