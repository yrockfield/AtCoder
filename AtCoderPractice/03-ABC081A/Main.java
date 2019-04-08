import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.*;
public class Main{
	public static void main(String[] args) throws IOException{

		Scanner sc = new Scanner(System.in);

		String inpStr = sc.nextLine();

		// 一桁ずつ取得
		int s1 = Integer.parseInt(inpStr.substring(0,1));
		int s2 = Integer.parseInt(inpStr.substring(1,2));
		int s3 = Integer.parseInt(inpStr.substring(2,3));

		//s1からs3のうち、"1"の個数
		int kosu = s1 + s2 + s3;

		sc.close();

		// 出力
		System.out.println(kosu);
	}
}