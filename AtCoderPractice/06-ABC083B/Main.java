import java.io.IOException;
import java.util.*;
public class Main{
	public static void main(String[] args) throws IOException{

		Scanner sc = new Scanner(System.in);

		int cnt = sc.nextInt();		
		int a = sc.nextInt();		//A
		int b = sc.nextInt();		//B

		sc.close();

		int tmpWa = 0;
		int total = 0;
		String strNum = "";

		for(int i=1; i <= cnt; i++){
			strNum = Integer.toString(i);
			tmpWa = 0;
			for(int j=0; j < strNum.length(); j++){
				tmpWa += Integer.parseInt( strNum.substring(j,j+1) );
			}
			if(tmpWa >= a && tmpWa <= b){
				total += i;
			}
		}
		
		// 出力
		System.out.println(total);
	}
}