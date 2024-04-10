package Algorithm.java.주식가격;

import java.util.Stack;

class Solution {
    public int[] solution(int[] prices) {
        Stack<Integer> stack = new Stack<>();
        int[] answer = new int[prices.length];

        for(int i = 0; i < prices.length; i++) {
            // 스택이 비어있지 않고, 현재 가격이 스택의 top에 있는 가격보다 작으면
            // 가격이 떨어진 것이므로 스택에서 pop하고 해당 인덱스의 정답을 계산
            while(!stack.isEmpty() && prices[i] < prices[stack.peek()]) {
                int index = stack.pop();
                answer[index] = i - index;
            }
            // 현재 인덱스를 스택에 push
            stack.push(i);
        }

        // 스택에 남아 있는 인덱스는 가격이 떨어지지 않은 것으로, prices 배열의 끝까지 가격이 떨어지지 않음
        while(!stack.isEmpty()) {
            int index = stack.pop();
            answer[index] = prices.length - 1 - index;
        }

        return answer;
    }
}