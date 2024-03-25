package Algorithm.java.수들의합;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int N;
    static int M;
    static long[] tree;

    static long value;
    static long idx;
    public static void main(String[] argv) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        StringTokenizer tokenizer = new StringTokenizer(br.readLine());

        N = Integer.parseInt(tokenizer.nextToken());
        M = Integer.parseInt(tokenizer.nextToken());

        tree = new long[(N*4)+1];

        for(int t = 0; t < M; t ++) {
            tokenizer = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(tokenizer.nextToken());
            if(a == 0) {
                int i = Integer.parseInt(tokenizer.nextToken());
                int j = Integer.parseInt(tokenizer.nextToken());
                long result;
                if (i>j) {
                    result = sum(1, N, 1, j, i);
                } else {
                    result = sum(1, N, 1, i, j);
                }
                System.out.println(result);
            } else {
                idx = Long.parseLong(tokenizer.nextToken());
                value = Long.parseLong(tokenizer.nextToken());
                update(1, N, 1);
            }

        }
    }

    public static long sum(int start, int end, int node, int left, int right) {
        // 범위에 벗어난경우
        if (start > right || left > end) return 0;

        // 범위 안에 있는경우
        if (start >= left && right >= end) {
            return tree[node];
        } else {
            int mid = (start+end) / 2;
            long leftSum = sum(start, mid, node*2, left, right);
            long rightSum = sum(mid+1, end, node*2+1, left, right);
            return leftSum + rightSum;
        }
    }

    public static void update(int start, int end, int node) {
        // 범위가 아닌경우
        if(start > idx || idx > end) return;
        // 리프노드에 도달한경우
        if(start == end) {
            tree[node] = value;
            return;
        } else {
            int mid = (start+end) / 2;            
            update(start, mid, node*2);
            update(mid+1, end, node*2+1);
            tree[node] = tree[node*2] + tree[node*2+1];
            return;
        }
    }
}