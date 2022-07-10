import java.util.Scanner;
class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        String[] arr = sc.nextLine().split("");
        String prev = "";
        for(int i=0; i<arr.length; i++){
            if(arr[i].equals(prev) && arr[i].equals("s")){
                System.out.println("hiss");
                return;
            }
            prev = arr[i];
        }
        System.out.println("no hiss");
    }
}