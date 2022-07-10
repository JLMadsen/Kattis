import java.util.Scanner;
class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int iteration = sc.nextInt();
        int points = 0;
        int squares = 1;
        for(int i=1; i<=iteration; i++){
            squares = squares*2;
        }
        if(iteration == 0){
            points = 4;
        } else {
            points = (squares+1)*(squares+1);
        }
        System.out.println(points);
    }
}