package Algorithm.java.주식가격;

import java.util.Arrays;

public class Main {
    public static void main(String[] argv)
    {
        Solution solution = new Solution();
        int[] prices = {1, 2, 3, 2, 3};
        System.out.println(Arrays.toString(solution.solution(prices)));
    }
}
