package src;

import java.util.Scanner;
import java.util.Stack;

public class Problem5 {
    public String solution(String input) {
        String result = "";

        Stack<Integer> stack = new Stack();

        for (int i = 0; i < input.length(); i++) {
            if (isAlphabet(input.charAt(i))) {
                stack.push(i);
            }
        }

        for (int i = 0; i < input.length(); i++) {
            if (isAlphabet(input.charAt(i))) {
                Integer popIndex = stack.pop();

                result += input.charAt(popIndex);
            }
            else {
                result += input.charAt(i);
            }
        }

        return result;
    }

    public boolean isAlphabet(char c) {
        if (c >= 65 && c <= 90) {
            return true;
        }
        if (c >= 97 && c <= 122) {
            return true;
        }
        return false;
    }

    public static void main(String[] args) {
        Problem5 problem5 = new Problem5();

        Scanner sc = new Scanner(System.in);

        String input = sc.nextLine();

        System.out.print(problem5.solution(input));
    }
}
