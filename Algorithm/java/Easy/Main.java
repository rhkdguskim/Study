package Algorithm.java.Easy;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {
    static int N;
    static int table[][];
    static final int LEFT = 0;
    static final int RIGHT = 1;
    static final int UP = 2;
    static final int DOWN = 3;
    public static void main(String[] argv) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());
        table = new int[N][N];
        for(int i = 0; i < N; i ++) {
            StringTokenizer tokenizer = new StringTokenizer(br.readLine());
            for(int j = 0; j < N; j++) table[i][j] = Integer.parseInt(tokenizer.nextToken());
        }
    }


    public static Value[][] Move(Value[][] table, int dir) {
        Value[][] newTable = new Value[N][N];

        for(int i = 0; i < N; i ++)
        {
            Stack<Point> stack = new Stack<>();
            if(dir == LEFT || dir == RIGHT) {
                if(dir == LEFT) {
                    for(int j = N-1; j >= 0; j--) {
                        if(table[i][j].c != 0) {
                            stack.add(new Point(i, j));
                        }
                    }
                } else {
                    for(int j = 0; j < N; j++) {
                        if(table[i][j].c != 0) {
                            stack.add(new Point(i, j));
                        }
                    }
                }
            } else {
                if(dir == UP) {
                    for(int j = N-1; j >= 0; j--) {
                        if(table[j][i].c != 0) {
                            stack.add(new Point(i, j));
                        }
                    }
                } else {
                    for(int j = 0; j < N; j++) {
                        if(table[j][i].c != 0) {
                            stack.add(new Point(i, j));
                        }
                    }
                }
            }

            // 스택 크기가 0일경우
            if (stack.size() > 0) {
                int idx = 0;
                Point prevPoint = stack.pop();
                while (stack.empty()) {
                    Point curPoint = stack.pop();
                    // 값이 같은경우
                    if(table[prevPoint.y][prevPoint.x].v) {
                        newTable[i][idx].c = table[prevPoint.y][prevPoint.x].c;
                        newTable[i][idx].v = table[prevPoint.y][prevPoint.x].v;

                        prevPoint = curPoint;
                        idx += 1;
                        continue;
                    }

                    if(dir == LEFT || dir == RIGHT) {
                        if (curPoint.equals(prevPoint)) {
                            newTable[i][idx].c = table[curPoint.y][curPoint.x].c * 2;
                            newTable[i][idx].v = true;
                        } else {
                            newTable[i][idx].c = table[prevPoint.y][prevPoint.x].c;
                            prevPoint = curPoint;
                        }
                    } else {
                        if (curPoint.equals(prevPoint)) {
                            newTable[idx][i].c = table[curPoint.y][curPoint.x].c * 2;
                            newTable[idx][i].v = true;
                        } else {
                            newTable[idx][i].c = table[prevPoint.y][prevPoint.x].c;
                            prevPoint = curPoint;
                        }
                    }
                    idx += 1;
                }
            }
        }
        return newTable;
    }

    public static class Value {
        public boolean v;
        public int c;

        Value(int c, boolean v) {
            this.c = c;
            this.v = v;
        }
    }


    public static class Point {
        public int y;
        public int x;

        Point(int y, int x) {
            this.y = y;
            this.x = x;
        }


        public boolean equals(Point p, int[][] table) {
            return table[this.y][this.x] == table[p.y][p.x];
        }
    }
}
