public class Main {
	public static void main(String args[])
     {
     int n = 99;
     String l = Integer.toString(n);
     int d = l.length();
     System.out.print("Number of digits : "+d);
     if(d%2!=0 && d==0)
     {
         int b=d-1;
         int c=b*b;
         System.out.println("\nSquare of "+b+ " is "+c);
     }
     else
     {
         int c= d*d;
         System.out.println("\nSquare of "+d+ " is "+c);
     }
     
    }
}