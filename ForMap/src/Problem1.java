package src;

import java.util.*;

public class Problem1 {
    public void solution(String str1, String str2) {
        boolean answer = true;
        HashMap<Character, Integer> map = new HashMap<>();

        for(char c : str1.toCharArray()) {
            map.put(c, map.getOrDefault(c, 0) + 1);
        }

        for(char c : str2.toCharArray()) {
            if(!map.containsKey(c) || map.get(c) == 0) {
                answer = false;
            }
            map.put(c, map.get(c) -1);
        }

        if(answer == true) {
            System.out.print("YES");
        }
        else {
            System.out.print("NO");
        }
    }

    public static void main(String[] args) {
        Problem1 problem1 = new Problem1();
        Scanner sc = new Scanner(System.in);

        String str1 = sc.nextLine();
        String str2 = sc.nextLine();

        problem1.solution(str1, str2);
    }
}
