package Algorithm.java.다리를지나는트럭;

import java.util.*;

class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int answer = 0;
        int currentWeight = 0;
        int currentCnt = 0;

        // 다리에 트럭의 정보를 담는다.
        Deque<Integer> bridge = new ArrayDeque<>();
        for(int i = 0; i < bridge_length; i ++)
        {
            bridge.add(0);
        }

        // 트럭을 순회하면서 다리에 넣는다.
        for(int i = 0; i < truck_weights.length; i++)
        {
            // 끝에 트럭이 존재한다면 트럭을 도착시킨다.
            Integer truck = bridge.pollLast();
            if(truck > 0)
            {
                currentWeight -= truck;
                currentCnt -= 1;
            }

            // 현재 트럭을 넣을 수 있다면 트럭을 넣는다.
            if(weight >= currentWeight + truck_weights[i] && bridge_length >= currentCnt + 1) {
                bridge.addFirst(truck_weights[i]);
                currentWeight += truck_weights[i];
                currentCnt += 1;
            }
            else {
                // 다음 리터레이션에서 다시 트럭을 넣어야하기때문에 Dummy를 넣고 i를 증감한다.
                bridge.addFirst(0);
                i--;
            }
            answer += 1;
        }

        // 남은 트럭을 꺼낸다.
        while(!bridge.isEmpty())
        {
            bridge.pollLast();
            answer += 1;
        }

        return answer;
    }
}