package Algorithm.java.연구소;
import java.util.*;
import java.util.stream.IntStream;
import java.io.*;

public class Main {
    static int N;
    static int M;
    static int[][] table;
    static int[][] copyedtable;
    static int ans;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        
        table = new int[N][M];
        copyedtable = new int[N][M];
        IntStream.range(0, N).forEach(i-> {
            try {
                StringTokenizer new_st = new StringTokenizer(br.readLine());
                IntStream.range(0, M).forEach(j-> {
                    table[i][j] = Integer.parseInt(new_st.nextToken());
                });
            } catch (IOException e) {
                e.printStackTrace();
            }
        });

        solve(0, 0);
        System.out.println(ans);
    }

    public static void solve(int index, int wall)
    {
        if (wall == 3) {
            ans = Math.max(ans, getSafeArea());
            return;
        }

        int i = index / N;
        int j = index % M;

        // 범위에 벗어난경우 return
        if(i < 0 || i >= N || j < 0 || j >= M) return;


        for(int k = index; k < N * M; k++) {
            int x = k / M;
            int y = k % M;
            if(table[x][y] == 0) {
                table[x][y] = 1;
                solve(index + 1, wall + 1);
                table[x][y] = 0;
            }
        }
    }

    public static int getSafeArea()
    {
        int cnt = 0;
        Deque<Integer> q = new ArrayDeque<>();

        for(int i = 0; i < N; i++) {
            for(int j = 0; j < M; j++) {
                copyedtable[i][j] = table[i][j];
                if(table[i][j] == 2) {
                    q.addLast(i * M + j);
                }
            }
        }

        int[][] moves = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

        // 바이러스를 퍼트린다.
        while(!q.isEmpty()) {
            int index = q.pollFirst();
            int x = index / M;
            int y = index % M;

            for(int[] move : moves) {
                int nx = x + move[0];
                int ny = y + move[1];

                if(nx < 0 || nx >= N || ny < 0 || ny >= M) continue;

                if(copyedtable[nx][ny] == 0) {
                    copyedtable[nx][ny] = 2;
                    q.addLast(nx * M + ny);
                }
            }
        }

        // 안전영역을 구한다.
        for(int i = 0; i < N; i++) {
            for(int j = 0; j < M; j++) {
                if(copyedtable[i][j] == 0) {
                    cnt++;
                }
            }
        }

        return cnt;
    }
}
