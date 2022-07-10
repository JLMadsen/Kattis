import java.util.Scanner;
class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        while(true){
            int n = sc.nextInt();
            if(n == -1){
                return;
            }
            int distance = 0;
            int hours = 0;
            for(int i=0; i<n; i++){
                int mph = sc.nextInt();
                int time = sc.nextInt();
                int newtime = (time-hours);
                distance += (mph*newtime);
                hours += newtime;
            }
            System.out.println(distance +" miles");
        }
    }
}