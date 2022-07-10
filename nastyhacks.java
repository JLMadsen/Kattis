import java.util.Scanner;
class main {
    
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        
        for(int i=0; i<n; i++) {
            int r = sc.nextInt();
            int e = sc.nextInt();
            int c = sc.nextInt();
            
            int diff = (r+c)-e;
            
            if(diff == 0) {
                System.out.println("does not matter");
            } else if(diff < 0) {
                System.out.println("advertise");
            } else {
                System.out.println("do not advertise");
            }
        }
    }
}