package Algorithm.java.스티커붙이기;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    static List<Sticker> stickerList = new ArrayList<>();
    static int N, M, K; // 세로, 가로, 스티커 개수
    static int[][] notebook;
    public static void main(String[] argv) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer tokenizer = new StringTokenizer(reader.readLine());
        N = Integer.parseInt(tokenizer.nextToken());
        M = Integer.parseInt(tokenizer.nextToken());
        K = Integer.parseInt(tokenizer.nextToken());
        notebook = new int[N][M];


        while(K -- > 0) {
            tokenizer = new StringTokenizer(reader.readLine());

            int n, m;
            n = Integer.parseInt(tokenizer.nextToken());
            m = Integer.parseInt(tokenizer.nextToken());
            int[][] table = new int[n][m];
            for(int i = 0; i < n; i ++) {
                tokenizer = new StringTokenizer(reader.readLine());
                for(int j = 0; j<m; j ++) {
                    table[i][j] = Integer.parseInt(tokenizer.nextToken());
                }
            }
            stickerList.add(new Sticker(table, n, m));
        }


        stickerList.forEach(sticker -> {
            loop:
            for(int k = 0; k < 4; k ++) {
                for(int i = 0; i < N; i ++) {
                    for(int j = 0; j < M; j ++) {
                        if (isAvailable(i, j, sticker)) {
                            break loop;
                        }
                    }
                }
                sticker.rotate();
            }
        });
//        for(int [] note : notebook) {
//            System.out.println(Arrays.toString(note));
//        }
        System.out.println(solve());
    }
    public static boolean isAvailable(int y, int x, Sticker sticker) {
        // 조건을 확인한다.
        for(int i = 0; i < sticker.n; i++) {
            for(int j = 0; j < sticker.m; j++) {
                if(i+y >=N || j+x >= M)  return false;

                if(notebook[i+y][j+x] == 1 && sticker.graph[i][j] == 1) return false;
            }
        }

        // 스티커를 붙힌다.
        for(int i = 0; i < sticker.n; i++) {
            for(int j = 0; j < sticker.m; j++) {
                if(notebook[i+y][j+x] == 0 && sticker.graph[i][j] == 1) {
                    notebook[i+y][j+x] = sticker.graph[i][j];
                }
            }
        }
        return true;
    }

    public static int solve()
    {
        int sum = 0;
        for(int i = 0; i < N; i ++) {
            for(int j = 0; j < M; j ++) {
                if(notebook[i][j] == 1) {
                    sum += 1;
                }
            }
        }
        return sum;
    }

    public static class Sticker  {
        public int[][] graph;
        public int n, m;
        Sticker(int[][] graph, int n, int m)
        {
            this.n = n; // 세로
            this.m = m; // 가로
            this.graph = graph;
        }

        public void rotate()  {
            int[][] temp = new int[m][n];

            for(int i = 0; i < n; i++) {
                for(int j = 0; j < m; j ++) {
                    temp[j][n-i-1] = graph[i][j];
                }
            }
            graph = temp;
            int t = m;
            m = n;
            n = t;

//            for(int [] g : graph) {
//                System.out.println(Arrays.toString(g));
//            }

        }
    }
}
