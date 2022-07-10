import java.util.Scanner;
class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int total = 0;
        int x = sc.nextInt();
        int n = sc.nextInt();
        for(int i=0; i<n; i++){
            total += x;
            total -= sc.nextInt();
        }
        total += x;
        System.out.println(total);
    }
}