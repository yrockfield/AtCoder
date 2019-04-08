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

		loop500:
		for (int i=0; i<=coins500; i++) {
			if(500 * i > kingaku){
				break loop500;
			}else if (500 * i == kingaku){
				ptn++;
			}else{
				loop100:
				for (int j=0; j<=coins100; j++ ){
					if(500 * i + 100 * j > kingaku ){
						break loop100;
					}else if (500 * i + 100 * j == kingaku ){
						ptn++;
					}else{
						loop50:
						for(int k=0; k<=coins50; k++ ){
							if(500 * i + 100 * j + 50 * k > kingaku ){
								break loop50;
							}else if (500 * i + 100 * j + 50 * k == kingaku ){
								ptn++;
							}
						}
					}

				}

			}


		}
		
		// 出力
		System.out.println(ptn);
	}
}