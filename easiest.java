import java.util.Scanner;
class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        Reader re = new Reader();
        
        while(sc.hasNextInt()){
            int n = sc.nextInt();
            if(n == 0){
                return;
            }
            for(int i=11; i<100000; i++){
                int b = n*i;
                if(re.sum(b) == re.sum(n)){
                    System.out.println(i);
                    break;
                }
            }
        }
    }
}
class Reader{
    public Reader(){}
    public int sum(int x){
        String z = Integer.toString(x);
        String[] y = z.split("");
        int re = 0;
        for(int i=0; i<y.length; i++){
            re += Integer.parseInt(y[i]);
        }
        return re;
    }
}