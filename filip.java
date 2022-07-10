import java.util.Scanner;
class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        String in = sc.nextLine();
        StringBuilder sb = new StringBuilder(in);
        String[] input = sb.reverse().toString().split(" ");
        if(Integer.parseInt(input[0])<Integer.parseInt(input[1])){
            System.out.println(input[1]);
        } else {
            System.out.println(input[0]);
        }
    }
}