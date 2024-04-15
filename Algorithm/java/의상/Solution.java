package Algorithm.java.의상;

// headgear : yellow_hat, green_turban
// eyewear : blue_sunglasses

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

// face : crow_mask, blue_sunglasses, smoky_make_up
class Solution {
    public static void main(String[] argv)
    {
        Solution solution = new Solution();
        String[][] cloths = {{"yellow_hat", "headgear"}, {"blue_sunglasses", "eyewear"}, {"green_turban", "headgear"}};
        solution.solution(cloths);
    }

    private Map<String, List<String>> clothmapList = new HashMap<>();
    int ans = 0;
    public int solution(String[][] clothes) {
        // 종류별로 입력받는다.
        for(String[] cloth: clothes)
        {
            String key = cloth[1];
            String value = cloth[0];
            List<String> list = clothmapList.getOrDefault(key, new ArrayList<>());
            list.add(value);
            clothmapList.put(key, list);
        }

        // 가능한 모든 조합을 탐색.
        solve(clothmapList.keySet().toArray(new String[0]), 0, 1);

        // 모두 착용하지 않는경우는 제외한다.
        return ans-1;
    }

    public void solve(String[] key, int index, int combi)
    {
        if(index == key.length)
        {
            ans += combi;
            return;
        }

        // 착용한경우
        int cnt = clothmapList.get(key[index]).size();
        solve(key, index+1, combi * cnt);

        // 착용하지 않은경우
        solve(key, index+1, combi);
    }
}
