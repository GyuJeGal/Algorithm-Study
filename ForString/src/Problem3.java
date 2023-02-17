package src;

import java.util.Scanner;

public class Problem3 {
    public String solution(String input) {
        String result = "";

        String[] candidates = input.split(" ");

        for (String candidate : candidates) {
            if (result.length() < candidate.length()) {
                result = candidate;
            }
        }

        return result;
    }

    public static void main(String[] args) {
        Problem3 problem3 = new Problem3();

        Scanner sc = new Scanner(System.in);

        String input = sc.nextLine();

        System.out.print(problem3.solution(input));
    }
}
