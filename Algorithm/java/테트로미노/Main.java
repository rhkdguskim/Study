package Algorithm.java.테트로미노;
import java.util.*;
import java.io.*;

public class Main {
    static int N;
    static int M;
    static int[][] table;
    private static final int[][][] TETROMINO = {
        // I 자
        {{0, 1}, {0, 2}, {0, 3}},
        {{1, 0}, {2, 0}, {3, 0}},
        // 사각형
        {{1, 0}, {0, 1}, {1, 1}},
        // L 자
        {{0, 1}, {0, 2}, {1, 2}},
        {{0, 1}, {1, 0}, {2, 0}},
        {{1, 0}, {1, 1}, {1, 2}},
        {{1, 0}, {2, 0}, {2, -1}},
        // J 자
        {{1, 0}, {1, -1}, {1, -2}},
        {{0, 1}, {1, 1}, {2, 1}},
        {{0, 1}, {0, 2}, {1, 0}},
        {{1, 0}, {2, 0}, {2, 1}},
        // S 자
        {{0, 1}, {1, 1}, {1, 2}},
        {{1, 0}, {1, -1}, {2, -1}},
        // Z 자
        {{0, -1}, {1, -1}, {1, -2}},
        {{1, 0}, {1, 1}, {2, 1}},
        // ㅜ자
        {{1, 0}, {1, 1}, {2, 0}},
        {{1, -1}, {1, 0}, {1, 1}},
        {{1, 0}, {1, -1}, {2, 0}},
        {{0, -1}, {0, 1}, {1, 0}}

};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        table = new int[N][M];

        for(int i=0; i < N; i++) 
        {
            st = new StringTokenizer(br.readLine());
            for(int j=0; j<M; j++)
            {
                table[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        System.out.println(solve());
    }

    public static int solve() {
        int ans = 0;
        for(int i=0; i< N; i++)
        {
            for(int j=0; j<M; j++)
            {
                for(int[][] points: TETROMINO)
                {
                    int n1 = i + points[0][0];
                    int m1 = j + points[0][1];

                    int n2 = i + points[1][0];
                    int m2 = j + points[1][1];

                    int n3 = i + points[2][0];
                    int m3 = j + points[2][1];


                    if(isRange(n1, m1) && isRange(n2, m2) && isRange(n3, m3))
                    {
                        int sum = table[i][j] + table[n1][m1] + table[n2][m2] + table[n3][m3];
                        if(sum > ans) ans = sum;
                    }
                }
            }
        }

        return ans;
    }

    public static boolean isRange(int y, int x) {
        return 0 <= y && y < N && 0 <= x && x < M;
    }

}
