import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int count = 0;		
		
		int N = in.nextInt();
		int[] arr = new int[N];
		
		for(int i = 0; i < N; i++) {
	        arr[i] = in.nextInt();
	    }
		
		int v = in.nextInt();
		
		for(int i = 0; i < arr.length; i++) {
			if (v == arr[i]) {
				count ++;
			}
		}
		
		System.out.println(count);
	}
}