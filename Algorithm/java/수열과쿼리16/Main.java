package Algorithm.java.수열과쿼리16;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int N;
    static int M;
    static Long[] A;
    static Long[] tree;
    static int[] index;
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
        index = new int[N*4];

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
                Long temp[] = query(0, N-1, 1);
                result.append(temp[1]+1);
                result.append("\n");
            }
        }

        System.out.println(result.toString());
    }

    public static void init(int start, int end, int node) {
        if (start == end) {
            tree[node] = A[start];
            index[node] = start;
            return;
        } else {
            int mid = (start + end) / 2;
            init(start, mid, node*2);
            init(mid+1, end, node*2+1);
            if (tree[node*2] > tree[node*2+1]) {
                index[node] = index[node*2+1];
            } else {
                index[node] = index[node*2];
            }
            tree[node] = Math.min(tree[node*2], tree[node*2+1]);
            return;
        }
    }

    public static Long[] query(int start, int end, int node) {
        // 범위에 벗어난경우
        if (start > right || left > end) {
            return new Long[]{Long.MAX_VALUE, Long.MAX_VALUE};
        }

        if (start >= left && right >= end) {
            return new Long[]{tree[node] , Long.valueOf(index[node])};
        } else {
            int mid = (start+end) / 2;
            Long[] left = query(start, mid, node*2);
            Long[] right = query(mid+1, end, node*2+1);
            Long[] minValue = new Long[2];
            if (left[0] > right[0]) {
                minValue[0] = right[0];
                minValue[1] = right[1];
            } else {
                minValue[0] = left[0];
                minValue[1] = left[1];
            }
            return minValue;
        }
    }

    public static void update(int start, int end, int node) {
        if(start > idx || idx > end) return;

        if(start == end) {
            A[start] = value;
            tree[node] = value;
            index[node] = start;
        } else {
            int mid = (start+end) / 2;
            update(start, mid, node*2);
            update(mid+1, end, node*2+1);

            if (tree[node*2] > tree[node*2+1]) {
                index[node] = index[node*2+1];
            } else {
                index[node] = index[node*2];
            }

            tree[node] = Math.min(tree[node*2], tree[node*2+1]);
        }
    }
}