import java.util.Scanner;
class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = 0;
        while(sc.hasNextInt()){
            int x = sc.nextInt();
            if(x<0){
                m++;
            }
        }
        System.out.println(m);
    }
}