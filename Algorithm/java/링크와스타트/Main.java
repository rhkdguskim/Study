package Algorithm.java.링크와스타트;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

// https://www.acmicpc.net/problem/15661
// 팀은 1명이상 꾸려야하고 각 두 팀간의 팀워크 점수 차이가 가장 작은 값을 찾는다.
// A, B, C, D, E
public class Main {
    static int N;
    static boolean[] isInStartTeam;
    static int[][] table;
    static int ans = Integer.MAX_VALUE;

    public static void main(String[] argv) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(reader.readLine());
        isInStartTeam = new boolean[N];
        table = new int[N][N];

        for (int i = 0; i < N; i++) {
            StringTokenizer tokenizer = new StringTokenizer(reader.readLine());
            for (int j = 0; j < N; j++) {
                table[i][j] = Integer.parseInt(tokenizer.nextToken());
            }
        }

        solve(0);
        System.out.println(ans);
    }

    public static void solve(int idx) {
        if (idx == N) {
            int startTeamSize = 0;
            for (boolean inStart : isInStartTeam) {
                if (inStart) startTeamSize++;
            }

            // 모든 선수가 한 팀에만 속하는 경우 제외
            if (startTeamSize == 0 || startTeamSize == N) return;

            List<Integer> startTeam = new ArrayList<>();
            List<Integer> linkTeam = new ArrayList<>();
            for (int i = 0; i < N; i++) {
                if (isInStartTeam[i]) startTeam.add(i);
                else linkTeam.add(i);
            }
            ans = Math.min(ans, diff(startTeam, linkTeam));
            return;
        }

        isInStartTeam[idx] = true;
        solve(idx + 1);

        isInStartTeam[idx] = false;
        solve(idx + 1);
    }

    public static int diff(List<Integer> startTeam, List<Integer> linkTeam) {
        int startTeamSum = 0, linkTeamSum = 0;

        for (Integer i : startTeam) {
            for (Integer j : startTeam) {
                if (i != j) startTeamSum += table[i][j];
            }
        }
        for (Integer i : linkTeam) {
            for (Integer j : linkTeam) {
                if (i != j) linkTeamSum += table[i][j];
            }
        }

        return Math.abs(startTeamSum - linkTeamSum);
    }
}

