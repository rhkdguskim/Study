package Algorithm.java.AC;

import java.util.*;
import java.io.*;
import java.util.stream.Collectors;
import java.util.stream.IntStream;;

public class Main {
    static int T;
    static BufferedReader bufferedReader;
    public static void main(String[] argv) throws IOException {
        bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer tokenizer = new StringTokenizer(bufferedReader.readLine());
        
        T = Integer.parseInt(tokenizer.nextToken());

        IntStream.range(0, T).forEach(i -> {
            try {
                solve();
            } catch (IOException e) {
                // TODO Auto-generated catch block
                e.printStackTrace();
            }
             catch (NoSuchElementException e) {
                System.out.println("error");
             }
        });

    }

    public static void solve() throws IOException
    {
        StringTokenizer tokenizer = new StringTokenizer(bufferedReader.readLine());
        String p = tokenizer.nextToken();
        tokenizer = new StringTokenizer(bufferedReader.readLine());

        int n = Integer.parseInt(tokenizer.nextToken());
        Deque<Integer> deque = new ArrayDeque<>();


        tokenizer = new StringTokenizer(bufferedReader.readLine());

        String arr = tokenizer.nextToken();
        arr = arr.substring(1, arr.length()-1);

        String[] temp = arr.split(",");
        for(int i = 0; i < n; i ++) {
            deque.addLast(Integer.parseInt(temp[i]));
        }
        
        boolean isReversed = false;
        for(int i = 0; i < p.length(); i ++) {
            char c = p.charAt(i);
            if (c == 'R') {
                isReversed = !isReversed;
            } else {
                if(isReversed) {
                    deque.removeLast();
                } else {
                    deque.removeFirst();
                }
            }
        }
        List<Integer> list = deque.stream().collect(Collectors.toList());

        if(isReversed)
            Collections.reverse(list);

        System.out.println(Arrays.toString(list.toArray()).replaceAll(" ", ""));
    }
}
