import java.util.Scanner;

class main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int x = sc.nextInt();
        int y = sc.nextInt();
        int n = sc.nextInt();
        
        for(int i = 1; i<=n; i++){
            int status = 0;
            if( i%x == 0 ){
                status = 1;
            }
            if ( i%y == 0 ){
                if(status == 1){
                    status = 3;
                } else {
                    status = 2;
                }
            }
            switch(status){
                case 0:
                    System.out.println(i);
                    break;
                case 1:
                    System.out.println("Fizz");
                    break;
                case 2:
                    System.out.println("Buzz");
                    break;
                case 3:
                    System.out.println("FizzBuzz");
                    break;
            }
            
        }
    }
}