package Algorithm.java.이중우선순위큐;

import java.util.Comparator;
import java.util.PriorityQueue;

class Solution {
    public static class Number {
        int index;
        int number;
        Number(int number, int index)
        {
            this.number = number;
            this.index = index;
        }


    }

    public int[] solution(String[] operations) {
        int n = operations.length;

        boolean[] visited = new boolean[n];
        Comparator<Number> com = Comparator.comparingInt(n2 -> n2.number);
        Comparator<Number> com2 = (n1, n2) -> n2.number- n1.number;

        PriorityQueue<Number> minQ = new PriorityQueue<>(com);
        PriorityQueue<Number> maxQ = new PriorityQueue<>(com2);
        int index = 0;
        for(String operation : operations)
        {
            String[] temp = operation.split(" ");
            if(temp[0].equals("I")) {
                minQ.add(new Number(Integer.parseInt(temp[1]), index));
                maxQ.add(new Number(Integer.parseInt(temp[1]), index));
                visited[index] = true;
            } else {
                while (!maxQ.isEmpty() && !visited[maxQ.peek().index])
                {
                    maxQ.poll();
                }

                while (!minQ.isEmpty() && !visited[minQ.peek().index])
                {
                    minQ.poll();
                }

                if(Integer.parseInt(temp[1]) == 1) {
                    // 최대값 POP
                    if(!maxQ.isEmpty())
                    {
                        Number num = maxQ.poll();
                        visited[num.index] = false;
                    }

                } else {
                    // 최소값 POP
                    if(!minQ.isEmpty())
                    {
                        Number num = minQ.poll();
                        visited[num.index] = false;
                    }
                }
            }

            index += 1;
        }

        while (!maxQ.isEmpty() && !visited[maxQ.peek().index])
        {
            maxQ.poll();
        }

        while (!minQ.isEmpty() && !visited[minQ.peek().index])
        {
            minQ.poll();
        }

        int[] answer = new int[2];
        if(!minQ.isEmpty() && !maxQ.isEmpty())
        {
            Number n1 = maxQ.peek();
            Number n2 = minQ.peek();
            answer[0] = n1.number;
            answer[1] = n2.number;
        }

        return answer;
    }

    public static class DualPriorityQueue
    {
        private final PriorityQueue<Integer> minQueue = new PriorityQueue<>();
        private final PriorityQueue<Integer> maxQueue = new PriorityQueue<>(Comparator.reverseOrder());

        public void push(int number)
        {
            if(maxQueue.isEmpty())  {
                minQueue.add(number);
            }
            else {
                if(maxQueue.peek() > number) {
                    minQueue.add(number);
                } else {
                    maxQueue.add(number);
                }
            }
        }

        public int popMax()
        {
            while(!minQueue.isEmpty())
            {
                maxQueue.add(minQueue.poll());
            }

            if(!maxQueue.isEmpty())  {
                return maxQueue.poll();
            }
            else {
                return 0;
            }
        }

        public int popMin()
        {
            while(!maxQueue.isEmpty())
            {
                minQueue.add(maxQueue.poll());
            }

            if(!minQueue.isEmpty()) {
                return minQueue.poll();
            }
            else {
                return 0;
            }
        }
    }
}