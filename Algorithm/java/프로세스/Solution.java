package java.프로세스;

import java.util.ArrayDeque;
import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.Queue;

class Solution {
    private final PriorityQueue<Integer> pq = new PriorityQueue<>(Comparator.reverseOrder());
    public static class Process {
        int index;
        int value;
        Process(int index, int value) {
            this.index = index;
            this.value = value;
        }
    }
    public int solution(int[] priorities, int location) {
        
        Queue<Process> q = new ArrayDeque<>();

        int answer = 0;
        int index = 0;
        for(int process : priorities)
        {
            pq.add(process);
            q.add(new Process(index, process));
            index += 1;
        }

        while (!q.isEmpty())
        {
            Process currentProcess = q.poll();
            
            if (pq.peek() > currentProcess.value) {
                q.offer(currentProcess);
            } else {
                answer += 1;
                if (location == currentProcess.index) {
                    break;
                }
                pq.poll();
            }
        }
        
        return answer;
    }
}
