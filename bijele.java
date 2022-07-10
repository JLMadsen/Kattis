import java.util.Scanner;
class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int[] ref = {1, 1, 2, 2, 2, 8};
        String out = "";
        for(int i=0; i<ref.length; i++){
            int x = sc.nextInt();
            out += (ref[i]-x) +" ";
        }
        System.out.println(out);
        sc.close();
    }
}