package Algorithm.백준;
import java.util.*;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class BOJ1022 {
    static int r1, c1, r2, c2;
    static int R, C;
    static int[][] moves = {{0, 1}, {-1, 0}, {0, -1}, {1, 0}};
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = new StringTokenizer(br.readLine());

        r1 = Integer.parseInt(st.nextToken());
        c1 = Integer.parseInt(st.nextToken());
        r2 = Integer.parseInt(st.nextToken());
        c2 = Integer.parseInt(st.nextToken());
        R = r2 - r1 + 1;
        C = c2 - c1 + 1;
        Long[][] table = new Long[R][C];

        int fillCount = R*C;

        int startY = -r1;
        int startX = -c1;
        int i = 1;
        int direction = 0;
        Long cnt = 1L;

        while (fillCount > 0)
        {
            for(int k =0; k < 2; k ++)
            {
                for(int j = 0; j < i; j ++)
                {
                    if (isInRange(startY, startX))
                    {
                        table[startY][startX] = cnt;
                        fillCount -= 1;
                    }
                    
                    startY += moves[direction][0];
                    startX += moves[direction][1];
                    cnt += 1;
                }

                direction = changeDirection(direction);
            }

            i += 1;
        }

        //bw.write();
        bw.flush();
        bw.close();
        br.close();
	}

    public static int changeDirection(int direction)
    {
        direction += 1;
        return direction % 4;
    }

    public static boolean isInRange(int y, int x)
    {
        return (y >= 0 && y < R) && (x >= 0 && x < C);
    }
}
