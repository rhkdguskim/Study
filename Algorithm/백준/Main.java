package Algorithm.백준;
import java.util.*;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

class Main {
    static int N, K, S, X, Y;
    static int[][] table;
	public static void main(String[] args) throws IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        table = new int[N][N];
        
        for(int i = 0; i < N; i++)
        {
            st = new StringTokenizer(br.readLine());
            for(int j = 0; j < N; j++)
            {
                int v = Integer.parseInt(st.nextToken());
                table[i][j] = v;
            }
        }

        st = new StringTokenizer(br.readLine());

        S = Integer.parseInt(st.nextToken());
        X = Integer.parseInt(st.nextToken());
        Y = Integer.parseInt(st.nextToken());
        
        int ans = Solve();

        bw.write(String.valueOf(ans) + "\n");
        bw.flush();
        bw.close();
        br.close();
	}

    static int Solve()
    {
        if (table[X-1][Y-1] != 0)
        {
            return table[X-1][Y-1];
        }

        int maxValue = Integer.MAX_VALUE;
        int minVirus = Integer.MAX_VALUE;

        for(int i = 0; i < N; i ++) 
        {
            for(int j =0; j < N; j ++)
            {
                if (table[i][j] != 0)
                {
                    int dist = getDist(X-1, Y-1, i, j);
                    if (maxValue > dist)
                    {
                        maxValue = dist;
                        minVirus = table[i][j];
                    } else if (maxValue == dist && minVirus > table[i][j])
                    {
                        minVirus = table[i][j];
                    }

                }
            }
        }
        if (maxValue > S) minVirus = 0;
    
        return minVirus;   
    }

    static int getDist(int r1, int c1, int r2, int c2) {
        return Math.abs(r1 - r2) + Math.abs(c1 - c2);
    }
}