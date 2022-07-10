import java.util.Scanner;
class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        String[] words = sc.nextLine().split(" ");
        for(int i=0; i<words.length; i++){
            for(int j=(i+1); j<words.length; j++){
                if(words[i].equals(words[j])){
                    System.out.println("no");
                    return;
                }
            }
        }
        System.out.println("yes");
    }
}