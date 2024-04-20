package Algorithm.java.피로도;

import java.util.Arrays;
import java.util.Comparator;

class Solution {
    boolean[] visited = new boolean[8];
    int length;
    int[][] dungeons;
    public int solution(int k, int[][] dungeons) {
        length = dungeons.length;
        this.dungeons = dungeons;

        return solve(k);
    }

    public int solve(int fatigue)
    {
        int maxValue = 0;
        for(int i = 0; i < length; i ++)
        {
            if(!visited[i])
            {
                visited[i] = true;
                if(fatigue >= dungeons[i][0])
                {
                    maxValue = Math.max(solve(fatigue - dungeons[i][1]) + 1, maxValue);
                }
                visited[i] = false;

            }
        }
        return maxValue;

    }
}