import java.util.*;
public class Main {
	public static void main(String[] args){

		String ans = "";

		Scanner sc = new Scanner(System.in);
		// スペース区切りの整数の入力
		int a = sc.nextInt();
		int b = sc.nextInt();

		//aとbの積
		int seki = a * b;

		//積が奇数なら"odd",偶数なら"even"と出力
		if (seki % 2 == 0){
			ans = "Even";
		}else{
			ans = "Odd";
		}

		sc.close();

		// 出力
		System.out.println(ans);
	}
}