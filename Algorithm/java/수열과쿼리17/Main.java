package Algorithm.java.수열과쿼리17;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int N;
    static int M;
    static Long[] A;
    static Long[] tree;
    static int left;
    static int right;
    static int idx;
    static Long value;
    public static void main(String[] argv) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer tokenizer = new StringTokenizer(br.readLine());
        N = Integer.parseInt(tokenizer.nextToken());
        A = new Long[N];
        tree = new Long[N*4];

        tokenizer = new StringTokenizer(br.readLine());
        for(int i = 0; i < N; i ++ ) {
            A[i] = Long.parseLong(tokenizer.nextToken());
        }

        tokenizer = new StringTokenizer(br.readLine());
        M = Integer.parseInt(tokenizer.nextToken());
        
        StringBuilder result = new StringBuilder();

        init(0, N-1, 1);

        for(int i = 0; i < M; i++) {
            tokenizer = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(tokenizer.nextToken());
            if (a == 1) {
                idx = Integer.parseInt(tokenizer.nextToken()) - 1;
                value = Long.parseLong(tokenizer.nextToken());
                update(0, N-1, 1);
            } else {
                left = Integer.parseInt(tokenizer.nextToken()) - 1;
                right = Integer.parseInt(tokenizer.nextToken()) - 1;
                Long temp = query(0, N-1, 1);
                result.append(temp);
                result.append("\n");
            }
        }

        System.out.println(result.toString());
    }

    public static void init(int start, int end, int node) {
        if (start == end) {
            tree[node] = A[start];
            return;
        } else {
            int mid = (start + end) / 2;
            init(start, mid, node*2);
            init(mid+1, end, node*2+1);
            tree[node] = Math.min(tree[node*2], tree[node*2+1]);
            return;
        }
    }

    public static Long query(int start, int end, int node) {
        // 범위에 벗어난경우
        if (start > right || left > end) {
            return Long.MAX_VALUE;
        }

        if (start >= left && right >= end) {
            return tree[node];
        } else {
            int mid = (start+end) / 2;
            return Math.min(query(start, mid, node*2), query(mid+1, end, node*2+1));
        }
    }

    public static void update(int start, int end, int node) {
        if(start > idx || idx > end) return;

        if(start == end) {
            A[start] = value;
            tree[node] = value;
        } else {
            int mid = (start+end) / 2;
            update(start, mid, node*2);
            update(mid+1, end, node*2+1);
            tree[node] = Math.min(tree[node*2], tree[node*2+1]);
        }
    }
}