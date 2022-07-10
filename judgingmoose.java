import java.util.Scanner;
class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int l = sc.nextInt();
        int r = sc.nextInt();
        int x;
        String out = "";
        if(l==0&&r==0){
            System.out.println("not a moose");
            return;
        }
        if(l==r){
            out = "Even";
        } else {
            out = "Odd";
        }
        if(l<r){
            x = r*2;
        } else {
            x = l*2;
        }
        System.out.println(out +" "+ x);
    }
}