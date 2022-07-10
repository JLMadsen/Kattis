import java.util.Scanner;
class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        double qaly = 0;
        for(int i=0; i<n; i++){
            double ql = sc.nextDouble();
            double per = sc.nextDouble();
            qaly += (ql*per);
        }
        System.out.println(qaly);
    }
}