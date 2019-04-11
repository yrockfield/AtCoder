import java.io.IOException;
import java.util.*;

public class Main{
	public static void main(String[] args) throws IOException{

		String ans = "Yes";
		int time = 0;
		int timePrev = 0;
		int x = 0;
		int y = 0;
		int xPrev = 0;
		int yPrev = 0;
		int move = 0;

		Scanner sc = new Scanner(System.in);
		
		int kaisu = sc.nextInt();

		for(int i=0; i < kaisu; i++){
			time = sc.nextInt();
			x = sc.nextInt();
			y = sc.nextInt();

			//とりあえずx,yごとに最短距離で到達できるか
			move = Math.abs(x - xPrev) + Math.abs(y - yPrev);
			//移動回数をオーバーしたらNO
			if(move > time - timePrev) {
				ans = "No";
				break;
			}

			//最短距離で到達できても、寄り道するには2ターンずつ必要では？＝移動回数の余りが偶数じゃなかったらダメっぽい気がする
			if ( (time - timePrev - move) % 2 != 0 ){
				ans = "No";
				break;
			}

			timePrev = time;
			xPrev = x;
			yPrev = y;

		}

		sc.close();

		//出力
		System.out.println(ans);

	}
}