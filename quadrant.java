import java.util.Scanner;
class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int x = sc.nextInt();
        int y = sc.nextInt();
        int sector = 0;
        if(x > 0 && y > 0){
            sector = 1;
        } else if(x > 0 && y < 0){
            sector = 4;
        } else if(x < 0 && y > 0){
            sector = 2;
        } else if(x < 0 && y < 0){
            sector = 3;
        }
        System.out.println(sector);
    }
}