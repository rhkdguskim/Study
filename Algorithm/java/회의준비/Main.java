package Algorithm.java.회의준비;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;
import java.util.stream.IntStream;

public class Main {
    static int N;
    static int M;
    static boolean[] visited;
    static List<Integer> edge[];
    static int[][] distance;
    public static void main(String[] argv) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(reader.readLine());
        M = Integer.parseInt(reader.readLine());
        edge = new ArrayList[N+1];
        distance = IntStream.range(0, N +1)
                    .mapToObj(i -> IntStream.range(0, N+1).map((j) ->  {
                        if (i == j) {
                            return 0;
                        }
                        else {
                            return 101;
                        }
                    })
                    .toArray())
                    .toArray(int[][]::new);

        for(int i = 0; i< N+1; i++) {
            edge[i] = new ArrayList<>();
        }

        visited = new boolean[N+1];

        for (int i =0; i < M; i ++) {
            StringTokenizer tokenizer = new StringTokenizer(reader.readLine());
            int person1 = Integer.parseInt(tokenizer.nextToken());
            int person2 = Integer.parseInt(tokenizer.nextToken());
            distance[person1][person2] = 1;
            distance[person2][person1] = 1;
            edge[person2].add(person1);
            edge[person1].add(person2);
        }
        List<List<Integer>> group = new ArrayList<>();

        for (int i =1; i< N+1; i ++) {
            if (!visited[i]) {
                group.add(bfs(i));
            }
        }

        for(List<Integer> g : group) {
            for(int k : g) {
                for(int i : g) {
                    for(int j : g) {
                        if (i != j) {
                            distance[i][j] = Integer.min(distance[i][j], distance[i][k] + distance[k][j]);
                        }
                    }
                }
            }
        }
        List<Integer> result = new ArrayList<>();

        for(List<Integer> g : group) {
            result.add(findPerson(g));
        }
        result.sort(Integer::compare);
        System.out.println(result.size());
        for(int i : result) {
            System.out.println(i);
        }
    }

    public static int findPerson(List<Integer> group) {
        int min_person = group.get(0);
        int min_cnt = Integer.MAX_VALUE;
        for(int person : group) {
            int cnt = 0;
            for(int person2 : group) {
                if(person != person2) {
                    cnt = Integer.max(distance[person][person2], cnt);
                }
            }

            if (min_cnt > cnt) {
                min_person = person;
                min_cnt = cnt;
            }
        }
        return min_person;
    }

    public static List<Integer> bfs(int person) {
        List<Integer> group = new ArrayList<>();
        
        visited[person] = true;
        Queue<Integer> queue = new LinkedList<>();
        
        queue.add(person);
        group.add(person);

        while(!queue.isEmpty()) {
            Integer p = queue.poll();
            for(Integer p2 : edge[p]) {
                if(!visited[p2]) {
                    visited[p2] = true;
                    queue.add(p2);
                    group.add(p2);
                }
            }
        }

        return group;
    }
}
