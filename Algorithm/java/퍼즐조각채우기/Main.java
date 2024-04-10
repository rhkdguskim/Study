package Algorithm.java.퍼즐조각채우기;

public class Main {

    public static void main(String[] argv)
    {
        Solution solution = new Solution();

        int[][] gameboard = {{1,1,0,0,1,0},{0,0,1,0,1,0},{0,1,1,0,0,1},{1,1,0,1,1,1},{1,0,0,0,1,0},{0,1,1,1,0,0}};
        int[][] table = {{1,0,0,1,1,0},{1,0,1,0,1,0},{0,1,1,0,1,1},{0,0,1,0,0,0},{1,1,0,1,1,0},{0,1,0,0,0,0}};
        //int[][] gameboard = {{0,0,0},{1,1,0},{1,1,1}};
        //int[][] table = {{1,1,1}, {1,0,0},{0,0,0}};

        System.out.println(solution.solution(gameboard, table));
    }
}
