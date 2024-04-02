package Algorithm.java.계란으로계란치기;
import java.io.*;
import java.util.*;

public class Main {

    static int N;
    static Egg[] eggs;
    static int ans = 0;
    public static void main(String[] argv) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer tokenizer = new StringTokenizer(bufferedReader.readLine());
        N = Integer.parseInt(tokenizer.nextToken());

        eggs = new Egg[N];

        for(int i = 0; i < N; i ++) {
            tokenizer = new StringTokenizer(bufferedReader.readLine());
            long durability = Long.parseLong(tokenizer.nextToken());
            long weight = Long.parseLong(tokenizer.nextToken());
            eggs[i] = new Egg(weight, durability);
        }

        solve(0);
        
        System.out.println(ans);
    }

    public static void solve(int curIdx) {

        if (curIdx == N) {
            int cnt = 0;
            for(int i = 0; i < N; i++) {
                if (eggs[i].durability <= 0) {
                    cnt += 1;
                }
            }
            ans = Math.max(cnt, ans);
            return;
        }

        if (eggs[curIdx].durability <= 0) {
            solve(curIdx + 1);
            return;
        }

        boolean isAllbreak = true;
        for(int i = 0; i < N; i ++) {
            if ( i == curIdx ) continue;

            if (eggs[i].durability > 0) {
                isAllbreak = false;
                break;
            }
        }

        if (isAllbreak) {
            ans = Math.max(ans, N-1);
            return;
        }

        for(int i = 0; i < N; i ++) {
            if (curIdx == i || eggs[i].durability <= 0) continue;

            eggs[i].durability -= eggs[curIdx].weight;
            eggs[curIdx].durability -= eggs[i].weight;
            solve(curIdx+1);
            eggs[i].durability += eggs[curIdx].weight;
            eggs[curIdx].durability += eggs[i].weight;
        }

    }

    public static class Egg {
        public long weight;
        public long durability;

        Egg(long weight, long durability) {
            this.weight = weight;
            this.durability = durability;
        }
    
    }

}
