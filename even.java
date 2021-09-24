public class Main {
	public static void main(String args[])
     {
     int a = 49;
     int c;
     int d=0;
      if(a%2==0)
      {
        System.out.println(a+" is an even number");
        c=a/2;
        System.out.println(a+ " is " +c+ " times 2");
        for (int i=1; i*i<=a; i++)   
        {   
            if((a%i==0) && (a/i==i))   
            {   
                d=1;   
            }
             else
            {
                d=0;
            }
        }
        if(d==1)
        {
          System.out.println(a+ " is a square");
        }
        else
        {
          System.out.println(a+ " is not a square");
        }
      }
      else
      {
        System.out.println(a+" is not an even number");
        for (int i=1; i*i<=a; i++)   
        {   
            if((a%i==0) && (a/i==i))   
            {   
                 d=1;  
            }
             else
            {
                d=0;
            }
        }
        if(d==1)
        {
          System.out.println(a+ " is a square");
        }
        else
        {
          System.out.println(a+ " is not a square");
        }
      }
    }
}