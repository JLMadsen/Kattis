import java.util.Scanner;
class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        String[] moves = sc.nextLine().split("");
        int pos = 1;
        for(int i=0; i<moves.length; i++){
            String move = moves[i];
            if(move.equalsIgnoreCase("a")){
                if(pos == 1){
                    pos = 2;
                } else if(pos == 2){
                    pos = 1;
                }
            }else if(move.equalsIgnoreCase("b")){
                if(pos == 2){
                    pos = 3;
                } else if(pos == 3){
                    pos = 2;
                }
            }else if(move.equalsIgnoreCase("c")){
                if(pos == 1){
                    pos = 3;
                }else if(pos == 3){
                    pos = 1;
                }
            }
        }
        System.out.println(pos);
    }
}