package Algorithm.java.완주하지못한선수;
public class Main {

    public static void main(String[] argv) {
        var solve = new Solution();
        String[] p = {"marina", "josipa", "nikola", "vinko", "filipa"};
        String[] c = {"josipa", "filipa", "marina", "nikola"};

        System.out.println(solve.solution(p, c));
    }
}
