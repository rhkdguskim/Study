package Algorithm.java.더맵게;

import java.util.PriorityQueue;
class Solution {
    public int solution(int[] scoville, int K) {
        PriorityQueue<Integer> q = new PriorityQueue<>();
        for(int s : scoville)
        {
            q.add(s);
        }

        int cnt = 0;

        while(q.size() >= 2 && q.peek() < K)
        {
            int cur = q.poll();
            int prev = q.poll();

            int newValue = cur + (prev*2);
            q.add(newValue);
            cnt += 1;
        }

        if (q.peek() >= K) {
            return cnt;
        }
        else {
            return -1;
        }
    }
}