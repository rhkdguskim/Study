package Algorithm.java.치킨배달;

import static java.util.stream.Collectors.toList;
import java.util.*;
import java.io.*;

public class Main {
    static final int EMPTY = 0;
    static final int HOUSE = 1;
    static final int CHICKEN = 2;

    static int N;
    static int M;
    static int[][] city;

    static List<Point> house = new ArrayList<>();
    static Set<Point> chicken = new HashSet<>();
    static List<List<Point>> chList = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        city = new int[N][N];

        for(int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++)  {
                city[i][j] = Integer.parseInt(st.nextToken());
                if(city[i][j] == CHICKEN)  {
                    chicken.add(new Point(i, j));
                } else if (city[i][j] == HOUSE) {
                    house.add(new Point(i, j));
                }
            }
        }
        int ans = Integer.MAX_VALUE;
        getAvailableChicken(0);
        for(List<Point> chic : chList) {
            int city_distance = 0;
            for(Point h : house) {
                int minDistance = Integer.MAX_VALUE;
                for(Point c : chic) {
                    minDistance = Math.min(getDistance(c.y, c.x, h.y, h.x), minDistance);
                }
                city_distance += minDistance;
            }
            ans = Math.min(city_distance, ans);
        }
        System.out.println(ans);
    }

    public static int getDistance(int y1, int x1, int y2, int x2) {
        return Math.abs(y1 - y2) + Math.abs(x1 - x2);
    }

    public static void getAvailableChicken(int idx)
    {
        int i = idx / N;
        int j = idx % N;

        if (i >= N || i < 0 || j >= N || j < 0) return;

        if(chicken.size() == M) {
            chList.add(chicken.stream().map(point -> {
                return new Point(point.y, point.x);
            }).collect(toList()));
            return;
        }

        if (city[i][j] == CHICKEN) {
            chicken.remove(new Point(i, j));
            getAvailableChicken(idx + 1);
            chicken.add(new Point(i, j));
        }

        getAvailableChicken(idx + 1);
    }

    public static class Point {
        public int x;
        public int y;

        Point(int y, int x) {
            this.y = y;
            this.x = x;
        }

        @Override
        public String toString() {
            return String.format("(%d, %d)", y, x);
        }
        @Override
        public boolean equals(Object obj) {
            if(this == obj) {
                return true;
            }

            if (obj == null || getClass() != obj.getClass()) {
                return false;
            }

            Point point = (Point) obj;
            return this.x == point.x && this.y == point.y;
        }
        
        @Override
        public int hashCode() {
            return Objects.hash(y, x);
        }
    }

}
