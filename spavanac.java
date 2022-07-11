import java.util.Scanner;
/*
 * 10 10
 * 
 * 9 25
 */
 
class main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int h = sc.nextInt();
        int m = sc.nextInt();
        
        if(m < 45){
            if(h == 00){
                h = 23;
            } else {
                h--;
            }
            m = m + 60 - 45;

        } else {
            m -= 45;
        }
        System.out.println(h +" "+ m);
    }
}