package src;

import java.util.Scanner;

public class Problem6 {
    public String solution(String input) {
        String result = "";

        for (int i = 0; i < input.length(); i++) {
            String candidate = String.valueOf(input.charAt(i));
            if(!result.contains(candidate)) {
                result += candidate;
            }
        }

        return result;
    }

    public static void main(String[] args) {
        Problem6 problem6 = new Problem6();

        Scanner sc = new Scanner(System.in);

        String input = sc.nextLine();

        System.out.print(problem6.solution(input));
    }
}
