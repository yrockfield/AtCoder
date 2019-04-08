import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.*;
public class Main{
	public static void main(String[] args) throws IOException{

		Scanner sc = new Scanner(System.in);

		int n = Integer.parseInt(sc.nextLine());
		String inpStr = sc.nextLine();
		int kaisu = -1;

		do {
			kaisu ++;
			inpStr = canContinue(n, inpStr);
		} while(inpStr != null) ;

		sc.close();

		// 出力
		System.out.println(kaisu);
	}

	private static String canContinue(int n , String inp){

		StringBuilder nextStr = new StringBuilder();

		String[] inpArr =  inp.split(" ");

		for (int i=0; i < n; i++){
			if (Integer.parseInt(inpArr[i]) % 2 != 0){
				return null;
			}else{
				nextStr.append( Integer.parseInt(inpArr[i]) / 2 );
				nextStr.append( " ");
			}
		}

		return nextStr.toString();
	}
}