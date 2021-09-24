public class MyClass
{
    public static void main(String args[])
    {
        int [][] arr1 = new int [][] {{1, 5, 3,},{ 4, 2, 7,}};
        int [][] arr2 = new int [][] {{3,5,3},{ 4,9,7}};
        int [][] arr3 = new int [2][3];
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
        for(int i=0;i<2;i++)
        {
            for (int j=0;j<3;j++)
            {
                if(arr1[i][j]==arr2[i][j])
                {
                    arr3[i][j]=arr1[i][j]-arr2[i][j];
                    System.out.print(" "+arr3[i][j]);
                }
                else
                {
                    System.out.print(" "+arr1[i][j]);
                }
            }
            System.out.print("\n");
        }
        System.out.print("\n");
        System.out.print("\n");
        for(int i=0;i<2;i++)
        {
            for (int j=0;j<3;j++)
            {
                if(arr1[i][j]==arr2[i][j])
                {
                    arr3[i][j]=arr1[i][j]-arr2[i][j];
                    System.out.print(" "+arr3[i][j]);
                }
                else
                {
                    System.out.print(" "+arr2[i][j]);
                }
            }
            System.out.print("\n");
        }
    }
}