import java.util.Scanner;
class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int x = sc.nextInt();
        if(x%2!=0){
            System.out.println("Alice");
        } else {
            System.out.println("Bob");
        }
    }
}