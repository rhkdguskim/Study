package Algorithm.java.퍼즐조각채우기;


// https://school.programmers.co.kr/learn/courses/30/lessons/84021
// BFS 탐색으로 퍼즐을 구한다.
// 퍼즐은 직사각형의 크기형태로 0과 1로 이루어져야한다. ( 90도 회전 )

// 퍼즐을 놓을때 조건
// 퍼즐을 놓을때 모두 반칸 이어야 한다.
// 퍼즐에 인접한 칸에 0 이 있으면 놓지 못한다.

import java.util.*;

class Solution {
    boolean[][] visited;
    boolean[][] visited2;
    int[][] game_board;
    int[][] table;
    int h, w;
    int answer = 0;
    public int solution(int[][] game_board, int[][] table) {
        this.game_board = game_board;
        this.table = table;
        this.h = game_board.length;
        this.w = game_board[0].length;
        this.visited = new boolean[h][w];
        this.visited2 = new boolean[h][w];

        List<Puzzle> puzzles = new ArrayList<>();
        List<Puzzle> emptys = new ArrayList<>();

        for(int i =0; i < w; i ++)
        {
            for(int j =0; j < h; j++)
            {
                if (!visited[i][j] && table[i][j] == 1)
                {
                    puzzles.add(getPuzzle(i, j, visited, table, 1));
                }

                if (!visited2[i][j] && game_board[i][j] == 0)
                {
                    emptys.add(getPuzzle(i, j, visited2, game_board, 0));
                }
            }
        }

        for(Puzzle e : emptys) {
            loop:
            for(Puzzle p : puzzles)
            {
                // 해당 퍼즐은 맞춰진 상태
                if (p.h == -1 || p.w == -1) continue;

                for(int i = 0; i <4; i ++)
                {
                    if(e.equals(p))
                    {
                        answer += p.cnt;
                        p.h = -1;
                        p.w = -1;
                        break loop;
                    }

                    // 돌려보면서 모든 경우의 수를 확인한다. ( 4번 돌리는 이유는 다음 리터레이션에서 원위치를 찾기위해 )
                    p.rotate();
                }
            }
        }

        return answer;
    }

    public Puzzle getPuzzle(int i, int j, boolean[][] visited, int[][] table, int check)
    {
        List<Point> group = new ArrayList<>();
        int[][] moves = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        visited[i][j] = true;

        Deque<Point> q = new ArrayDeque<>();

        q.add(new Point(i, j));
        group.add(new Point(i, j));

        while(!q.isEmpty())
        {
            Point p = q.pollFirst();

            for(int[] m : moves)
            {
                int ny = m[0] + p.i;
                int nx = m[1] + p.j;
                if(h > ny && ny >= 0 && w > nx && nx >=0 && !visited[ny][nx] && table[ny][nx] == check)
                {
                    visited[ny][nx] = true;
                    group.add(new Point(ny, nx));
                    q.add(new Point(ny, nx));
                }
            }
        }
        return new Puzzle(group);
    }


    public static class Point {
        final int i;
        final int j;

        Point(int i, int j)
        {
            this.i = i;
            this.j = j;
        }
    }

    public static class Puzzle {
        int h, w;
        int[][] table;
        int cnt;

        Puzzle(int h, int w, int[][] table)
        {
            this.h = h;
            this.w = w;
            this.table = table;
            this.cnt = 0;

            for(int i = 0; i < h; i ++)
            {
                for(int j = 0; j < w; j++)
                {
                    if (table[i][j] == 1) {
                        cnt += 1;
                    }
                }
            }
        }

        Puzzle(List<Point> group)
        {
            int[] size = getSize(group);
            this.table = new int[size[0]][size[1]];

            for(Point p : group)
            {
                this.table[p.i-size[2]][p.j-size[3]] = 1;
            }

            this.h = size[0];
            this.w = size[1];
            this.cnt = 0;

            for(int i = 0; i < h; i ++)
            {
                for(int j = 0; j < w; j++)
                {
                    if (this.table[i][j] == 1) {
                        cnt += 1;
                    }
                }
            }
        }

        private int[] getSize(List<Point> group)
        {
            int[] result = new int[4];
            result[2] = Integer.MAX_VALUE;
            result[3] = Integer.MAX_VALUE;
            for (Point p1 : group) {
                for (Point p2 : group) {
                    result[0] = Math.max(Math.abs(p1.i - p2.i), result[0]);
                    result[1] = Math.max(Math.abs(p1.j - p2.j), result[1]);
                    result[2] = Math.min(p1.i, result[2]);
                    result[3] = Math.min(p1.j, result[3]);
                }
            }
            result[0] += 1;
            result[1] += 1;
            return result;
        }


        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (o == null || getClass() != o.getClass()) return false;
            Puzzle puzzle = (Puzzle) o;
            return h == puzzle.h && w == puzzle.w && Objects.deepEquals(table, puzzle.table);
        }

        @Override
        public int hashCode() {
            return Objects.hash(h, w, Arrays.deepHashCode(table));
        }

        public void rotate()
        {
            int[][] tempTable = new int[w][h];

            for(int i = 0; i < h; i ++)
            {
                for(int j = 0; j < w; j ++)
                {
                     tempTable[w-1-j][i] = table[i][j];
                }
            }
            int t = h;
            h = w;
            w = t;
            table = tempTable;
        }
    }
}