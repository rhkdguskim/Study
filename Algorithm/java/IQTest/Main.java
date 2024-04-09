package Algorithm.java.IQTest;

// https://www.acmicpc.net/problem/1111

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static int N;
    static int[] arr;

    public static void main(String[] argv) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(reader.readLine());

        StringTokenizer tokenizer = new StringTokenizer(reader.readLine());
        arr = new int[N];

        for(int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(tokenizer.nextToken());
        }

        if(N == 1 || (N == 2 && arr[0] != arr[1])) {
            System.out.println('A');
        } else if(N == 2) {
            System.out.println(arr[0]);
        } else {
            int a, b;
            if(arr[0] == arr[1]) {
                a = 1;
                b = 0;
            } else {
                a = (arr[2] - arr[1]) / (arr[1] - arr[0]);
                b = arr[1] - (arr[0] * a);
            }


            int i = 1;
            for (; i < N; i++) {
                if (arr[i] != (arr[i - 1] * a + b))
                    break;
            }
            if (i != N) {
                System.out.println("B");
            } else {
                System.out.println(arr[N - 1] * a + b);
            }
        }
    }
}
