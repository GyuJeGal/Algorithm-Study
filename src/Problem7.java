package src;

import java.util.Scanner;

public class Problem7 {
    public String solution(String input) {
        input = input.toLowerCase();

        if (isPalindrome(input)) {
            return "YES";
        }
        return "NO";
    }

    public boolean isPalindrome(String input) {
        int size = input.length() / 2;

        int left = 0;
        int right = input.length() - 1;

        for (int i = 0; i < size; i++) {
            if (input.charAt(left) != input.charAt(right)) {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }

    public static void main(String[] args) {
        Problem7 problem7 = new Problem7();

        Scanner sc = new Scanner(System.in);

        String input = sc.nextLine();

        System.out.print(problem7.solution(input));
    }
}
