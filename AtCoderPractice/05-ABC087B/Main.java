import java.io.IOException;
import java.util.*;
public class Main{
	public static void main(String[] args) throws IOException{

		Scanner sc = new Scanner(System.in);

		int coins500 = sc.nextInt();		//A
		int coins100 = sc.nextInt();		//B
		int coins50 = sc.nextInt();			//C
		int kingaku = sc.nextInt();			//X

		sc.close();

		int ptn = 0;

		for (int i=0; i<=coins500; i++) {
			for (int j=0; j<=coins100; j++ ){
				for(int k=0; k<=coins50; k++ ){
					if (500 * i + 100 * j + 50 * k == kingaku ){
						ptn++;
					}
				}
			}
		}
		
		// 出力
		System.out.println(ptn);
	}
}