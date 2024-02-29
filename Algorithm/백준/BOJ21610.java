package Algorithm.백준;
import java.util.*;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class BOJ21610 {
    static int N;
    static int M;
    static int[][] table;
    public static void main(String[] argv) throws IOException
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        table = new int[N][N];
        List<Cloud> clouds = new ArrayList<>();

        clouds.add(new Cloud(N-1, 0));
        clouds.add(new Cloud(N-1, 1));
        clouds.add(new Cloud(N-2, 0));
        clouds.add(new Cloud(N-2, 1));

        for(int i = 0; i < N; i++)
        {
            st = new StringTokenizer(br.readLine());
            for(int j = 0; j < N; j ++)
            {
                table[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        for(int i = 0; i < M; i++)
        {
            st = new StringTokenizer(br.readLine());
            int d = Integer.parseInt(st.nextToken());
            int s = Integer.parseInt(st.nextToken());
            clouds = moveCloud(clouds, d, s);
            rainAndCopy(clouds);
            clouds = makeClouds(clouds);
        }

        int ans = sumWater();
        StringBuilder result = new StringBuilder();
        result.append(ans);
        bw.write(result.toString());
        bw.flush();
        bw.close();
        br.close();
    }

    public static class Cloud {
        public int x;
        public int y;

        Cloud(int y, int x)
        {
            this.x = x;
            this.y = y;
        }

        @Override
        public boolean equals(Object obj) {
            if (this == obj) return true;
            if (obj == null || getClass() != obj.getClass()) return false;
            Cloud cloud = (Cloud) obj;
            return x == cloud.x && y == cloud.y;
        }
    
        @Override
        public int hashCode() {
            return Objects.hash(x, y);
        }
    }

    public static boolean isRange(Cloud cloud)
    {
        return N > cloud.y && cloud.y >= 0 && N > cloud.x && cloud.x >= 0;
    }

    public static Cloud moveFix(Cloud cloud)
    {
        if (isRange(cloud)) {
            return cloud;
        }
        else{
            if(cloud.y == N) {
                cloud.y = 0;
            }

            if(cloud.y == -1) {
                cloud.y = N-1;
            }

            if(cloud.x == N) {
                cloud.x = 0;
            }

            if(cloud.x == -1) {
                cloud.x = N-1;
            }
            return cloud;
        }
    }

    public static List<Cloud> moveCloud(List<Cloud> clouds, int direction, int moveCnt)
    {
        int [][]moves = {{0, 0}, {0, -1}, {-1, -1}, {-1, 0}, {-1, 1}, {0, 1}, {1, 1}, {1, 0}, {1, -1}};
        List<Cloud> newClouds = new ArrayList<>();

        for (Cloud cloud : clouds) {
            int tempY = cloud.y;
            int tempX = cloud.x;
            for(int i = 0; i < moveCnt; i ++) {
                int dy = moves[direction][0];
                int dx = moves[direction][1];
                var newCloud = moveFix(new Cloud(dy + tempY, dx + tempX));
                tempY = newCloud.y;
                tempX = newCloud.x;
            }
            newClouds.add(new Cloud(tempY, tempX));
        }
        return newClouds;
    }

    public static void rainAndCopy(List<Cloud> clouds)
    {
        int [][]moves = {{1, 1}, {-1, -1}, {-1, 1}, {1, -1}};

        for(var cloud : clouds)
        {
            table[cloud.y][cloud.x] += 1;
        }

        for(var cloud : clouds)
        {
            for (int i =0; i < 4; i ++)
            {
                int dy = moves[i][0];
                int dx = moves[i][1];
                if (isRange(new Cloud(dy+cloud.y, dx+cloud.x)) && table[dy+cloud.y][dx+cloud.x] >= 1)
                {
                    table[cloud.y][cloud.x] += 1;
                }
            }
        }
    }

    public static List<Cloud> makeClouds(List<Cloud> oldClouds)
    {
        List<Cloud> clouds = new ArrayList<>();
        for(int i = 0; i < N; i++) {
            for(int j = 0; j < N; j++) {
                if (table[i][j] >= 2) {
                    if(!oldClouds.contains(new Cloud(i, j)))
                    {
                        table[i][j] -= 2;
                        clouds.add(new Cloud(i, j));
                    }
                }
            }
        }
        return clouds;
    }

    public static int sumWater()
    {
        int ans = 0;
        for(int i = 0; i < N; i++) {
            for(int j = 0; j < N; j ++) {
                ans += table[i][j];
            }
        }
        return ans;
    }
}
