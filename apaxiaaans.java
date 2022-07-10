import java.util.Scanner;
class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        String[] name = sc.nextLine().split("");
        String newName = "";
        int letters = 0;
        String prev = "";
        
        for(int i=0; i<name.length; i++){
            if(!(name[i].equals(prev))){
                prev = name[i];
                newName += name[i] +"";
            }
        }
        System.out.println(newName);
    }
}