import java.io.IOException;
import java.util.*;
public class Main{
	public static void main(String[] args) throws IOException{

		Scanner sc = new Scanner(System.in);
		
		int cnt = sc.nextInt();		
		ArrayList<Integer> cards = new ArrayList<>(cnt);
		int pAlice = 0;
		int pBob = 0;

		for(int i=0; i < cnt; i++){
			cards.add(sc.nextInt());
		}

		sc.close();

		Collections.sort(cards, Collections.reverseOrder());

		for(int i=0; i < cnt; i++){
			if (i % 2 == 0){
				pAlice += (int) cards.get(i);
			}else{
				pBob += (int) cards.get(i);
			}
		}
		
		// 出力
		System.out.println(pAlice - pBob);
	}
}