public class MyClass
{
    static void printPatt()
    {
        int k1 = 3;
        int k2 = 3;
        int gap = 5;
        int n = 3;
        for(int i = 1; i <= 5; i++)
        {
            for(int j = 1; j <= (5 * n); j++)
            {
                if (j > k2 && i < 5)
                {
                    k2 += gap;
                    k1 += gap;
                }
                if (j >= k1 && j <= k2)
                {
                    System.out.print("*");
                }
                else
                {
                    System.out.print(" ");
                }
            }
            if (i + 1 == 3)
            {
                k1 = 1;
                k2 = (5 * n);
            }
            else
            {
                k1 = 3;
                k2 = 3;
                k1--;
                k2++;
            }
            System.out.println();
        }
        
    }
    public static void main(String args[])
{
    printPatt();
}
}