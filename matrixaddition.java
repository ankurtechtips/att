public class MyClass
{
    public static void main(String args[])
    {
        int [][] arr1 = new int [][] {{1, 5, 3,},{ 4, 2, 7,}};
        for(int i=0;i<2;i++)
        {
            for (int j=0;j<3;j++)
            {
                System.out.print(" "+arr1[i][j]);
            }
            System.out.print("\n");
        }
        System.out.print("\n");
        System.out.print("\n");
        int [][] arr2 = new int [][] {{3,6,4},{ 4,9,7}};
        for(int i=0;i<2;i++)
        {
            for (int j=0;j<3;j++)
            {
                System.out.print(" "+arr2[i][j]);
            }
            System.out.print("\n");
        }
        System.out.print("\n");
        System.out.print("\n");
        int [][] arr3 = new int [2][3];
        for(int i=0;i<2;i++)
        {
            for (int j=0;j<3;j++)
            {
                arr3[i][j]=arr1[i][j]+arr2[i][j];
                System.out.print(" "+arr3[i][j]);
            }
            System.out.print("\n");
        }
        
    }
}