import java.io.*;
import java.util.*;
import java.util.regex.Pattern;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        String regex = "(100+1+|01)+";
        Pattern p  = Pattern.compile(regex);

        StringBuilder sb = new StringBuilder();

        while (T-- > 0) {
            boolean result = p.matcher(br.readLine()).matches();
            if (result) {
                sb.append("YES\n");
            } else {
                sb.append("NO\n");
            }
        }

        System.out.println(sb.toString());
    }
}