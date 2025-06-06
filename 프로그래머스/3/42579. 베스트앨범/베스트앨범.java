import java.util.*;

public class Solution {
    public int[] solution(String[] genres, int[] plays) {
        Map<String, List<int[]>> genreSongs = new HashMap<>();
        Map<String, Integer> genrePlays = new HashMap<>();

        for (int i = 0; i < genres.length; i++) {
            String genre = genres[i];
            int play = plays[i];

            genreSongs.putIfAbsent(genre, new ArrayList<>());
            genreSongs.get(genre).add(new int[]{i, play});

            genrePlays.put(genre, genrePlays.getOrDefault(genre, 0) + play);
        }

        List<String> sortedGenres = new ArrayList<>(genrePlays.keySet());
        sortedGenres.sort((a, b) -> genrePlays.get(b) - genrePlays.get(a));

        List<Integer> answer = new ArrayList<>();

        for (String genre : sortedGenres) {
            List<int[]> songs = genreSongs.get(genre);

            songs.sort((a, b) -> {
                if (b[1] == a[1]) return a[0] - b[0];
                return b[1] - a[1];
            });

            for (int i = 0; i < Math.min(2, songs.size()); i++) {
                answer.add(songs.get(i)[0]);
            }
        }

        return answer.stream().mapToInt(i -> i).toArray();
    }
}
