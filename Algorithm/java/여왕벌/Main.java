package Algorithm.java.여왕벌;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int M;
    static int N;
    static long[] temp;
    static long[][] table;
    public static void main(String[] argv) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        
        StringTokenizer tokenizer = new StringTokenizer(reader.readLine());
        M = Integer.parseInt(tokenizer.nextToken());
        N = Integer.parseInt(tokenizer.nextToken());

        temp = new long[2*M-1];
        table = new long[M][M];

        for(int i = 0; i < M; i++) {
            for(int j = 0; j < M; j ++) {
                table[i][j] = 1;
            }
        }

        for(int i = 0; i < N; i ++) {
            tokenizer = new StringTokenizer(reader.readLine());
            int cursor = 0;
            int a = Integer.parseInt(tokenizer.nextToken());
            cursor += a;
            int b = Integer.parseInt(tokenizer.nextToken());
            for(int j = 0; j < b; j ++) {
                temp[cursor] += 1;
                cursor += 1;
            }

            int c = Integer.parseInt(tokenizer.nextToken());
            for(int j = 0; j < c; j ++) {
                temp[cursor] += 2;
                cursor += 1;
            }
        }

        System.out.println(solve());
    }

    public static String solve() {
        int cursor = 0;
        for(int i = M-1; i >= 0; i--) {
            table[i][0] += temp[cursor];
            cursor += 1;
        }
        for(int i = 1; i < M; i ++) {
            table[0][i] += temp[cursor];
            cursor += 1;
        }

        for(int i = 1; i < M; i++) {
            for(int j = 1; j < M; j ++) {
                table[i][j] = Math.max(table[i-1][j-1], Math.max(table[i-1][j], table[i][j-1]));
            }
        }

        StringBuilder result = new StringBuilder();
        for(int i = 0; i < M; i++) {
            for(int j = 0; j < M; j ++) {
                result.append(table[i][j] + " ");
            }
            result.append("\n");
        }
        return result.toString();
    }
}
