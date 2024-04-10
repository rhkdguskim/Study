package Algorithm.java.폰켓몬;


import java.util.HashMap;
import java.util.Map;

class Solution {
    public static void main(String[] argv) {
        int[] nums = {3, 3, 3, 2, 2, 2};
        System.out.println(solution(nums));
    }

    public static int solution(int[] nums) {
        Map<Integer, Integer> numMap = new HashMap<>();

        for(int num : nums) {
            numMap.put(num, numMap.getOrDefault(num, 1) + 1);
        }

        return Math.min(numMap.keySet().toArray().length, nums.length / 2);
    }
}