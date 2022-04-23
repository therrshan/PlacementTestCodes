import java.util.*;
import java.io.BufferedReader;
import java.io.InputStreamReader;

class TestClass {
    public static void main(String args[] ) throws Exception {
     BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
     
     String str;
        while ((str = br.readLine()) != null && str.length()!= 0) {
            String result = "";
            for(int i=0;i<str.length();i++)
            {
                char ch = str.charAt(i);
                if(ch =='\\' && i<str.length()-1 && str.charAt(i+1) =='b')
                {
                    if (result.length() > 0) {
                        result = result.substring(0, result.length() -1);
                    }
                    i++;
                }
                else if (ch =='\\' && i<str.length()-1 && str.charAt(i+1)=='n')
                {
                    System.out.println(result);
                    result = "";
                    i++;
                }
                else {
                    result += ch;
                }	
            }
 
            if (result.length() > 0) {
                System.out.println(result);
            }
        }