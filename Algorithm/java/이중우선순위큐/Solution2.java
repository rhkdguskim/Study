package Algorithm.java.이중우선순위큐;


import java.util.Comparator;
import java.util.PriorityQueue;

class Solution1 {
    public int[] solution(String[] operations) {
        int n = operations.length;

        DualPriorityQueue queue = new DualPriorityQueue();

        for(String operation : operations)
        {
            String[] temp = operation.split(" ");
            if(temp[0].equals("I")) {
                queue.push(Integer.parseInt(temp[1]));
            } else {
                if(Integer.parseInt(temp[1]) == 1) {
                    // 최대값 POP
                    queue.popMax();

                } else {
                    // 최소값 POP
                    queue.popMin();
                }
            }
        }
        int[] answer = new int[2];
        answer[0] = queue.getMax();
        answer[1] = queue.getMin();
        return answer;
    }

    public static class DualPriorityQueue
    {
        private final PriorityQueue<Integer> minQueue = new PriorityQueue<>();
        private final PriorityQueue<Integer> maxQueue = new PriorityQueue<>(Comparator.reverseOrder());

        public void push(int number)
        {
            minQueue.add(number);
        }

        public int getMax()
        {
            while(!minQueue.isEmpty())
            {
                maxQueue.add(minQueue.poll());
            }

            if(!maxQueue.isEmpty())  {
                return maxQueue.peek();
            }
            else {
                return 0;
            }
        }

        public int getMin()
        {
            while(!maxQueue.isEmpty())
            {
                minQueue.add(maxQueue.poll());
            }

            if(!minQueue.isEmpty()) {
                return minQueue.peek();
            }
            else {
                return 0;
            }
        }

        public void popMax()
        {
            while(!minQueue.isEmpty())
            {
                maxQueue.add(minQueue.poll());
            }
            maxQueue.poll();
        }

        public void popMin()
        {
            while(!maxQueue.isEmpty())
            {
                minQueue.add(maxQueue.poll());
            }
            minQueue.poll();
        }
    }
}