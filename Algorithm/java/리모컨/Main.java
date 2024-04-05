package Algorithm.java.리모컨;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int N;
    static int M;
    static Set<Integer> brokenNumber = new HashSet<>();
    static int visited[];
    public static void main(String[] argv) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(reader.readLine());

        M = Integer.parseInt(reader.readLine());

        if(M > 0) {
            StringTokenizer tokenizer = new StringTokenizer(reader.readLine());
            for(int i = 0; i < M; i ++) {
                brokenNumber.add(Integer.parseInt(tokenizer.nextToken()));
            }
        }


        System.out.println(solve(N));
    }

    public static int solve(int number) {
        int value = Math.abs(number - 100); // 단순 +, -로만 이동 했을경우
        for(int i = 0; i < 1000000; i ++) {
            if(isAvailable(i)) {
                String temp = String.valueOf(i);
                int handleCnt = temp.length(); // 숫자로 움직인 횟수
                value = Math.min(value, handleCnt + Math.abs(number - i));
            }

        }
        return value;
    }

    public static boolean isAvailable(int number) {
        if (number == 0) {
            return brokenNumber.contains(number) ? false : true;
        }

        while (number > 0) {
            int check = number % 10;
            if(brokenNumber.contains(check)) {
                return false;
            }
            number /= 10;
        }

        return true;
    }

}
