import java.util.Scanner;
class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        double r = sc.nextInt();
        double c = sc.nextInt();
        double area = Math.PI * r * r;
        double cheese = Math.PI * (r-c) * (r-c);
        double percentage = (cheese/area)*100;
        System.out.println(percentage);
    }
}