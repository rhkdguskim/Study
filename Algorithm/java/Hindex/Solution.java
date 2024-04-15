package Algorithm.java.Hindex;


// 6 5 3 1 0

import java.util.Arrays;

class Solution {

    // 정렬된 데이터에서 H를 기준으로 이분탐색한다.
    // 카운팅 한 개수가 h번 이상인 개수가 h이상이고, h번 이하 인용되었다면 증가시킨다.
    // 카운팅 한 개수가 그렇지 않은경우 감소시킨다.
    public static void main(String[] argv)
    {
        Solution solution = new Solution();
        int[] citations = {3, 0, 6, 1, 5};
        System.out.println(solution.solution(citations));
    }
    public int solution(int[] citations) {

        int start = 0;
        int end = citations.length;
        int answer = 0;

        while(end >= start)
        {
            int mid = (start + end)/2;
            int h = 0;

            for(int num : citations)
            {
                if(num >= mid)
                {
                    h += 1;
                }
            }

            if(h >= mid)
            {
                // h를 더 중가시켜본다.
                answer = mid;
                start = mid + 1;
            }
            else {
                // h를 감소시켜본다.
                end  = mid - 1;
            }
        }
        return answer;
    }
}