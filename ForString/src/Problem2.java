package src;

import java.util.Scanner;

public class Problem2 {
    public String solution(String input) {
        String result = "";

        for (char c : input.toCharArray()) {
            if(Character.toUpperCase(c) == c) {
                result += (Character.toLowerCase(c));
            }
            else {
                result += (Character.toUpperCase(c));
            }
        }

        return result;
    }

    public static void main(String[] args) {
        Problem2 problem2 = new Problem2();

        Scanner sc = new Scanner(System.in);

        String input = sc.nextLine();

        System.out.print(problem2.solution(input));
    }

}
