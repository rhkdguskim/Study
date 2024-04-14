package Algorithm.java.전력망을둘로나누기;

import java.util.*;


class Solution {
    static int nodeSize;
    public int solution(int n, int[][] wires) {
        nodeSize = n+1;
        List<Edge> edges = new ArrayList<>();
        for(int[] i : wires)
        {
            edges.add(new Edge(i[0], i[1]));
        }
        return find(edges);
    }


    public int find(List<Edge> nodes)
    {
        int diff = Integer.MAX_VALUE;
        // BFS 탐색으로 그룹 카운팅을 한다.
        // idx 선을 기준으로 전력망을 둘로 나눈다.
        Map<Integer, List<Integer>> edges = new HashMap<>();
        for (Edge e : nodes) {
            var e1 = edges.getOrDefault(e.i, new ArrayList<>());
            e1.add(e.j);
            var e2 = edges.getOrDefault(e.j, new ArrayList<>());
            e2.add(e.i);
            edges.put(e.i, e1);
            edges.put(e.j, e2);
        }

        for (Edge node : nodes) {
            boolean[][] visited = new boolean[nodeSize][nodeSize];
            visited[node.i][node.i] = true;
            visited[node.j][node.j] = true;
            visited[node.i][node.j] = true;
            visited[node.j][node.i] = true;
            int group1 = bfs(node.i, edges, visited);
            int group2 = bfs(node.j, edges, visited);
            int newDiff = Math.abs(group2 - group1);
            //System.out.println(String.format("node1:(%d:%d), node2:(%d:%d), diff:%d",node.i, group1, node.j, group2, newDiff));
            diff = Math.min(diff, newDiff);
        }
        return diff;
    }

    public int bfs(int n, Map<Integer, List<Integer>> edges, boolean[][] visited)
    {
        int groupCnt = 0;
        Deque<Integer> q = new ArrayDeque<>();
        q.add(n);
        while(!q.isEmpty())
        {
            int node = q.pollFirst();
            groupCnt += 1;
            for (Integer child : edges.get(node)) {
                if (!visited[node][child]) {
                    //System.out.println(String.format("node : %d -> newnode : %d", n, node));
                    visited[node][child] = true;
                    visited[child][node] = true;
                    q.add(child);
                }
            }
        }
        return groupCnt;
    }

    public static class Edge
    {
        int i;
        int j;

        public Edge(int i, int j)
        {
            this.i = i;
            this.j = j;
        }
    }
}