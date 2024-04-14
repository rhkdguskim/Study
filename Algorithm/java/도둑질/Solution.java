package Algorithm.java.도둑질;

// https://school.programmers.co.kr/learn/courses/30/lessons/42897
class Solution {
    public int solution(int[] money) {
        int n = money.length;
        if (n == 1) return money[0];
        int prev1 = money[0], prev2 = 0;
        int includeFirst = 0, excludeFirst = 0;

        // 첫 번째 집을 포함하는 경우: 마지막 집은 털 수 없음
        for (int i = 1; i < n - 1; i++) {
            includeFirst = Math.max(prev1, prev2 + money[i]);
            prev2 = prev1;
            prev1 = includeFirst;
        }
        includeFirst = prev1;

        // 첫 번째 집을 제외하는 경우: 마지막 집을 털 수 있음
        prev1 = money[1];  // 두 번째 집부터 시작
        prev2 = 0;
        for (int i = 2; i < n; i++) {
            excludeFirst = Math.max(prev1, prev2 + money[i]);
            prev2 = prev1;
            prev1 = excludeFirst;
        }
        excludeFirst = prev1;

        return Math.max(includeFirst, excludeFirst);
    }
}