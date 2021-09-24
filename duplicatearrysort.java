public class Main
{
    public static void main(String args[])
    {
        int [] arr = new int [] {1, 2, 3, 4, 2, 7, 8, 8, 3};
        int temp=0, count=0;
        System.out.println("Duplicate elements in given array: ");  
        for(int i = 0; i < arr.length; i++)
        {
            for(int j = i + 1; j < arr.length; j++)
            {  
                if(arr[i] == arr[j])
                {  
                    System.out.println(arr[j]);
                }
            }
        }
        System.out.println("\nSorted array:");
        for(int i = 0; i < arr.length; i++)
        {
            for(int j = i + 1; j < arr.length; j++)
            {  
                if (arr[i] > arr[j])
                {
                    temp = arr[i];
                    arr[i] = arr[j];
                    arr[j] = temp;
                    
                }  
            }
            System.out.println(arr[i]);
        }
    }
}