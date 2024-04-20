package Algorithm.백준;
import java.util.*;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

// 탐색을 해가며 해당 위치에서 블록을 추가한다.
// 빈칸일 경우 해당블록에 추가를 하는데 연결할 수 있는 파이프를 따져보아야 한다.
// 만약, 가다가 갈 수가 없는 경우가 생긴다면 백트래킹 M이 도달되었다면 True를 반환하고 global 변수에 위치와 블록을 갱신한다.


public class BOJ2931 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = new StringTokenizer(br.readLine());

        //bw.write();
        bw.flush();
        bw.close();
        br.close();
	}
}
