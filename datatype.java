public class Main {
     {
    String input = "56.73";
        String dataType = null;
        if (input.matches("\\d+")) 
        {
            dataType = "Integer";
        }
        else if (input.matches("\\d*[.]\\d+"))
        {
            dataType = "Double";
        }

        else
        {
            dataType = "String";
        }
	public static void main(String args[])
        System.out.println("The datatype of " + input + " is : " + dataType);
    }
}