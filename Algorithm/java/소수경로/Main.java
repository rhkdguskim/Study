
package Algorithm.java.소수경로;
// https://www.acmicpc.net/problem/1963

import java.util.Scanner;
import java.util.LinkedList;
import java.util.Queue;
public class Main {
    static int T;
    
    public static void main(String[] argv) {
        try (Scanner sc = new Scanner(System.in)) {
            T = sc.nextInt();
            for(int i=0; i<T; i++) {
                int start = sc.nextInt();
                int end = sc.nextInt();
                System.out.println(solve(start, end));
            }
        }
    }
    
    public static int change(int cur, int index, int digit) {
        StringBuilder sb = new StringBuilder(String.valueOf(cur));
        sb.replace(index, index + 1, String.valueOf(digit));
        return Integer.parseInt(sb.toString());
    }

    public static boolean isPrime(int num) {
        if (num <= 1) {
            return false;
        }
        for (int i = 2; i <= Math.sqrt(num); i++) {
            if (num % i == 0) {
                return false;
            }
        }
        return true;
    }
    
    public static int solve(int start, int end) {
        Queue<Integer> q = new LinkedList<>();
        boolean[] visited = new boolean[10000];
        int[] count = new int[10000];

        q.add(start);
        visited[start] = true;

        while (!q.isEmpty()) {
            int cur = q.poll();
            if (cur == end) {
                return count[cur];
            }
            for (int i = 0; i < 4; i++) {
                for (int j = 0; j < 10; j++) {
                    int next = change(cur, i, j);
                    if (next >= 1000 && isPrime(next) && !visited[next]) {
                        q.add(next);
                        visited[next] = true;
                        count[next] = count[cur] + 1;
                    }
                }
            }
        }
        return -1;
    }
}