package Algorithm.java.디스크컨트롤러;


import java.util.Comparator;
import java.util.PriorityQueue;

// 끝나는 시점에서 요청부터 종료까지 가장 짧은 시간을 계속 고른다.
// 작업 시간이 가장 짧은 것부터 수행한다. (시작시간, 끝나는시간)
// 시작시간이 끝나는시간보다 크거나 같아야한다.
class Solution {
    public static void main(String[] argv)
    {
        int[][] jobs = {{0, 3}, {1, 9}, {2, 6}};
        Solution solution = new Solution();
        System.out.println(solution.solution(jobs));
    }

    public int solution(int[][] jobs) {
        DiskSchedule schedule = new DiskSchedule(jobs);
        int currentTime = 0;
        while(!schedule.isEmpty())
        {
            Work work = schedule.popNextWork(currentTime);
            currentTime += work.workTime;
        }

        return schedule.getAverage();
    }

    public static class DiskSchedule
    {
        private final PriorityQueue<Work> queue = new PriorityQueue<>();
        private final PriorityQueue<WaitWork> delayedWorks = new PriorityQueue<>();
        int workCnt;
        int workTime;
        DiskSchedule(int[][] jobs)
        {
            for(int[] job : jobs) {
                queue.add(new Work(job[0], job[1]));
            }
            workCnt = queue.size();
        }

        boolean isEmpty()
        {
            return queue.isEmpty();
        }

        Work popNextWork(int currentTime)
        {
            while(!queue.isEmpty())
            {
                Work work = queue.poll();
                int waitTime = work.workTime;
                waitTime += Math.abs(currentTime - work.start);
                delayedWorks.add(new WaitWork(waitTime, work));
            }

            WaitWork waitWork = delayedWorks.poll();
            workTime += waitWork.waitTime;

            while(!delayedWorks.isEmpty())
            {
                queue.add(delayedWorks.poll().work);
            }

            return waitWork.work;
        };

        int getAverage()
        {
            return workTime/workCnt;
        }

    }

    public static class WaitWork implements Comparable<WaitWork>
    {
        int waitTime;
        Work work;

        WaitWork(int waitTime, Work work)
        {
            this.waitTime = waitTime;
            this.work = work;
        }

        @Override
        public int compareTo(WaitWork o) {
            return Integer.compare(this.waitTime, o.waitTime);
        }
    }

    public static class Work implements Comparable<Work>
    {
        int start;
        int workTime;

        Work(int start, int workTime)
        {
            this.start = start;
            this.workTime = workTime;
        }

        @Override
        public int compareTo(Work o) {
            return Integer.compare(this.start, o.start);
        }
    }
}