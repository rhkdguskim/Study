package Algorithm.java.베스트앨범;

import java.util.Arrays;

public class Main {

    public static void main(String[] argv)
    {
        Solution solution = new Solution();
        String[] genres = {"classic", "pop", "classic", "classic", "pop"};
        int[] plays = {500, 600, 150, 800, 2500};
        int[] result = solution.solution(genres, plays);
        System.out.println(Arrays.toString(result));

    }
}
