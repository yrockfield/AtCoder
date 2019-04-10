import java.io.IOException;
import java.util.*;
import java.util.concurrent.CountDownLatch;
public class Main{
	public static void main(String[] args) throws IOException{

		Scanner sc = new Scanner(System.in);
		
		String inpMojiN = sc.nextLine();	

		sc.close();

		if(inpMojiN.matches("^(dream|dreamer|erase|eraser)+$")){
			System.out.println("YES");
		}else{
			System.out.println("NO");
		}
	}
}