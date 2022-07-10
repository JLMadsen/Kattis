import java.util.Scanner;
class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        double cost = 0;
        double price = sc.nextDouble();
        int lawns = sc.nextInt();
        for(int i=0; i<lawns; i++){
            cost += ((sc.nextDouble()*sc.nextDouble())*price);
        }
        System.out.println(cost);
    }
}