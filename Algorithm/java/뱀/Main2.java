package Algorithm.java.뱀;
import java.util.*;
import java.io.*;
import java.awt.*;


// 사과를 먹으면 뱀의 길이가 늘어난다.
// 벽이나 자기자신이랑 부딛히면 게임이 끝난다.
// 맨위 맨 좌측에서 길이가 1인 상태 오른쪽을 바라보며 시작.
public class Main2 {
    static Deque<Point> snake = new LinkedList<>();
    static int moves[][] = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
    static int RIGHT = 0;
    static int DOWN = 1;
    static int LEFT = 2;
    static int UP = 3;

    static int EMPTY = 0;
    static int APPLE = 1;
    static int SNAKE = 2;

    static Map<Integer, String> direction = new HashMap<>();
    static int[][] table; // 보드 정보
    static int N; // 보드 크기
    static int K; // 사과 개수
    static int L; // 뱀의 방향 변환 횟수
    public static void main(String[] argv) throws NumberFormatException, IOException {    
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());
        K = Integer.parseInt(br.readLine());
        table = new int[N][N];
        for(int i = 0; i < K; i ++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int y = Integer.parseInt(st.nextToken());;
            int x = Integer.parseInt(st.nextToken());;
            table[y-1][x-1] = APPLE;
        }
        L = Integer.parseInt(br.readLine());

        for(int i=0; i < L; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            Integer x = Integer.parseInt(st.nextToken());;
            String c = st.nextToken();
            direction.put(x, c);
        }

        snake.addLast(new Point(0, 0));
        System.out.println(solve(0, 0, RIGHT, 0));
    }

    static int solve(int i, int j, int dir, int time)
    {
        // System.out.println(new Point(j, i).toString());
        // System.out.println(String.format("time : %d, dir : %d", time, dir));
        // System.err.println(Arrays.toString(snake.toArray()));
        // 범위를 벗어 난 경우
        if(i < 0 || i >= N || j < 0 || j >= N) {
            return time;
        }

        // 자기자신을 만난 경우
        if (table[i][j] == SNAKE) {
            return time;
        }

        // 사과가 아니라면 꼬리를 제거한다.
        if(table[i][j] != APPLE) {
            Point p = snake.pollFirst();
            if(p != null) {
                table[p.y][p.x] = EMPTY;
            }
        }

        table[i][j] = SNAKE;

        // 해당 시간에 방향이 존재하면 방향을 바꾼다.
        if(direction.get(time) != null) {   
            dir = changeDir(dir, direction.get(time));
        }

        // 이동한다.
        int y = i + moves[dir][0];
        int x = j + moves[dir][1];
        snake.addLast(new Point(y, x));
        return solve(y, x, dir, time + 1);
    }

    static int changeDir(int d, String c)
    {
        if(c.equals("L")) {
            if(d == RIGHT) return UP;
            else if(d == UP) return LEFT;
            else if(d == LEFT) return DOWN;
            else if(d == DOWN) return RIGHT;
        } else {
            if(d == RIGHT) return DOWN;
            else if(d == DOWN) return LEFT;
            else if(d == LEFT) return UP;
            else if(d == UP) return RIGHT;
        }

        return 0;
    }
}
