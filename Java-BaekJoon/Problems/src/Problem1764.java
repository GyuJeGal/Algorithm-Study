import java.util.*;

public class Problem1764 {

    public void solution(int N, int M, String[] noListen, String[] noSee) {
        Map<String, Integer> map = new HashMap<>();

        for (String name : noListen) {
            map.put(name, 1);
        }

        List<String> answer = new ArrayList<>();

        for (String name : noSee) {
            if (map.containsKey(name)) {
                answer.add(name);
            }
        }

        Collections.sort(answer);

        System.out.println(answer.size());
        for (String name : answer) {
            System.out.println(name);
        }

    }

}
