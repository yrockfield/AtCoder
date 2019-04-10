import java.io.IOException;
import java.util.*;
public class Main{
	public static void main(String[] args) throws IOException{

		Scanner sc = new Scanner(System.in);
		
		int cnt = sc.nextInt();		
		ArrayList<Integer> mochi = new ArrayList<>(cnt);

		for(int i=0; i < cnt; i++){
			mochi.add(sc.nextInt());
		}

		sc.close();

		Collections.sort(mochi);

		for(int i=0; i < mochi.size() -1; i++){

			if (mochi.get(i) == mochi.get(i+1)){
				mochi.remove(i+1);
				i--;
			}
		}
		
		// 出力
		System.out.println(Integer.toString(mochi.size()));
	}
}