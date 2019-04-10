import java.io.IOException;
import java.util.*;
import java.util.concurrent.CountDownLatch;
public class Main{
	public static void main(String[] args) throws IOException{

		Scanner sc = new Scanner(System.in);
		
		int cnt = sc.nextInt();	
		int kingaku = sc.nextInt();	

		sc.close();
		
		int b_10k = -1;
		int b_5k = -1;
		int b_1k = -1;

		int cnt_10k=0;
		int cnt_5k=0;
		int cnt_1k=0;

		while(cnt_10k <= cnt) {

			cnt_5k = 0;

			while (cnt_10k + cnt_5k <= cnt ){

				cnt_1k = 0;

				while (cnt_10k + cnt_5k + cnt_1k <= cnt){
					if (cnt_10k * 10000 + cnt_5k * 5000 + cnt_1k * 1000 == kingaku && cnt_10k + cnt_5k + cnt_1k == cnt){
						b_10k = cnt_10k;
						b_5k = cnt_5k;
						b_1k = cnt_1k;
						break;
					}
					cnt_1k++;
				}
				cnt_5k++;
			}
			cnt_10k++;
		}
		
		// 出力
		System.out.println(Integer.toString(b_10k) + " " + Integer.toString(b_5k) + " " + Integer.toString(b_1k) );
	}
}