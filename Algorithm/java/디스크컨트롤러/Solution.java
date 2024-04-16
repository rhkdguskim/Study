package Algorithm.java.디스크컨트롤러;

import java.util.PriorityQueue;

// 작업큐와 work 큐를 분리하여 구현
class Solution {
    public static void main(String[] argv)
    {
        int[][] jobs = {{0, 3}, {1, 9}, {2, 6}};
        Solution solution = new Solution();
        System.out.println(solution.solution(jobs));
    }

    public int solution(int[][] jobs) {
        PriorityQueue<int[]> timeQueue = new PriorityQueue<>((w1, w2) -> (w1[0] - w2[0]));
        PriorityQueue<int[]> workQueue = new PriorityQueue<>((w1, w2) -> (w1[1] - w2[1]));
        int currentTime = 0;
        int workingTime = 0;
        for(int[] job : jobs)
        {
            timeQueue.add(job);
        }

        while(!timeQueue.isEmpty() || !workQueue.isEmpty())
        {
            // 1. 현지시간에서 작업할 수 있는 일들을 workQueue에 추가하는데 작업시간이 가장 짧은 순으로 넣는다.
            while(!timeQueue.isEmpty() && currentTime >= timeQueue.peek()[0])
            {
                workQueue.add(timeQueue.poll());
            }

            // 2. WorkQueue에서 하나를 꺼내어 시간을 계산한다.
            // 만약 일을 할 수 있는게 하나도 없다면 timeQueue의 시작시간을 현재시간으로 맞춘다.
            if(workQueue.isEmpty()) {
                currentTime = timeQueue.peek()[0];
            }
            else {
                int[] job = workQueue.poll();
                workingTime += (currentTime - job[0] + job[1]);
                currentTime += job[1];
            }
        }
        workingTime /= jobs.length;
        return workingTime;
    }
}