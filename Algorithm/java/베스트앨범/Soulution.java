package Algorithm.java.베스트앨범;

import java.util.*;

// https://school.programmers.co.kr/learn/courses/30/lessons/42579
// 가장 많이 재생된 노래를 두개씩 모아 베스트 앨범을 출시
// 각 장르별로 우선순위 큐를 활용하여 최대 2개씩 뽑아야한다.
// (장르, 재생횟수), Map(장르,노래들)
class Solution {
    public int[] solution(String[] genres, int[] plays) {
        int[] answer = {};
        Comparator<Music> comparator = (music1, music2) -> music2.plays - music1.plays;

        Map<String, Genre> map = new HashMap<>();

        for(int i = 0; i < genres.length; i++)
        {
           Genre genre = map.getOrDefault(genres[i], new Genre(genres[i], comparator));
           genre.totalPlays += plays[i];
           genre.musics.add(new Music(i, plays[i]));
           map.put(genres[i], genre);
        }

        Comparator<Genre> comparator1 = (g1, g2) -> g2.totalPlays - g1.totalPlays;
        PriorityQueue<Genre> queue = new PriorityQueue<>(comparator1);
        for(var key : map.keySet())
        {
            queue.add(map.get(key));
            //System.out.println(String.format("genre:%s, total:%d", key, map.get(key).totalPlays));
        }

        List<Integer> result = new ArrayList<>();

        while(!queue.isEmpty()) {
            Genre g = queue.poll();

            for(int i =0; i < 2; i ++) {
                if(!g.musics.isEmpty())
                {
                    Music m = g.musics.poll();
                    result.add(m.id);
                }
            }

        }
        return result.stream().mapToInt(i -> i).toArray();
    }

    public static class Genre
    {
        public String genre;
        public int totalPlays;
        public PriorityQueue<Music> musics;

        public Genre(String genre, Comparator<Music> comparator)
        {
            this.genre = genre;
            this.totalPlays = 0;
            this.musics = new PriorityQueue<>(comparator);
        }
    }

    public static class Music
    {
        public int id;
        public int plays;

        Music(int id, int plays)
        {
            this.id = id;
            this.plays = plays;
        }

        @Override
        public String toString() {
            return String.format("id:%d, plays:%d", id, plays);
        }
    }
}