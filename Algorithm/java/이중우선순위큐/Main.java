package Algorithm.java.이중우선순위큐;

import java.util.Arrays;

public class Main {

    public static void main(String[] argv)
    {
        String[] operations = {"I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"};
        Solution solution = new Solution();
        System.out.println(Arrays.toString(solution.solution(operations)));
    }
}
