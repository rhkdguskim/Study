package Algorithm.java.완주하지못한선수;
import java.util.HashMap;
import java.util.Map;


public class Solution {
    public String solution(String[] participant, String[] completion) {
        Map<String, Integer> p = new HashMap<>();
        Map<String, Integer> c = new HashMap<>();

        for(String a : participant)
        {
            p.put(a, p.getOrDefault(a, 1) + 1);
        }

        for(String a : completion)
        {
            c.put(a, c.getOrDefault(a, 1) + 1);
        }

        for(String key : c.keySet())
        {
            p.put(key, p.get(key) - c.get(key));
        }

        for(String key : p.keySet())
        {
            if(p.get(key) > 0)
            {
                return key;
            }
        }
        return "";
    }
}