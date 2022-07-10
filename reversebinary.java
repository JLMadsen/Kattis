import java.util.Scanner;
class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        String re = "";
        boolean convertet = false;
        while(!convertet){
            if(n%2==0){
                re += 0 +"";
            } else {
                re += 1 +"";
            }
            n = n/2;
            if(n == 0){
                convertet = true;
            }
        }
        String reverse = "";
        for(int i = re.length() - 1; i >= 0; i--)
        {
            reverse = reverse + re.charAt(i);
        }
        int out = 0;
        for(int j=0; j<reverse.length(); j++){
            if(Character.toString(reverse.charAt(j)).equals("1")){
                out += (int) 1*(Math.pow(2, j));
            }
        }
        System.out.println(out);
    }
}