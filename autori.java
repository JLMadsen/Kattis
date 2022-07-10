import java.util.Scanner;
class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        String[] in = sc.nextLine().split("-");
        String out = "";
        for(int i=0; i<in.length; i++){
            out += Character.toString(in[i].charAt(0));
        }
        System.out.println(out);
    }
}