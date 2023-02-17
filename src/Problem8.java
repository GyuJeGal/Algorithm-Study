package src;

import java.util.Scanner;

public class Problem8 {
    public int[] solution(String s, char t) {
        int[] result = new int[s.length()];

        leftToRight(s, t, result);
        rightToLeft(s, t, result);

        return result;
    }

    private void leftToRight(String s, char t, int[] result) {
        int p = 1000;

        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == t) {
                p = 0;
            }
            else {
                p++;
            }
            result[i] = p;
        }
    }

    private void rightToLeft(String s, char t, int[] result) {
        int p = 1000;

        for (int i = s.length() - 1; i >= 0; i--) {
            if (s.charAt(i) == t) {
                p = 0;
            }
            else {
                p++;
                if (p < result[i]) {
                    result[i] = p;
                }
            }
        }
    }

    public static void main(String[] args) {
        Problem8 problem8 = new Problem8();

        Scanner sc = new Scanner(System.in);

        String s = sc.next();
        char t = sc.next().charAt(0);

        for(int x : problem8.solution(s, t)) {
            System.out.print(x + " ");
        }
    }
}
