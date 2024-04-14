package Algorithm.java.전력망을둘로나누기;

public class Main {

    public static void main(String[] argv)
    {
        Solution sol = new Solution();
        int n = 9;
        int[][] wires = {{1, 3}, {2, 3}, {3, 4}, {4, 5}, {4, 6}, {4, 7}, {7, 8}, {7, 9}};
        System.out.println(sol.solution(n, wires));
    }
}
