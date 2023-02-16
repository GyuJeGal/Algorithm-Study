package src;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.Stack;

public class Problem4 {
    public void solution(List<String> inputList) {
        for (String input : inputList) {
            String result = "";

            Stack<Character> stack = new Stack();

            for (Character c : input.toCharArray()) {
                stack.push(c);
            }

            int size = stack.size();

            for (int i = 0; i < size; i++) {
                result += stack.pop();
            }

            System.out.println(result);
        }
    }

    public static void main(String[] args) {
        Problem4 problem4 = new Problem4();

        Scanner sc = new Scanner(System.in);

        int count = sc.nextInt();
        sc.nextLine();

        List<String> inputList = new ArrayList();

        for (int i = 0; i < count; i++) {
            String input = sc.nextLine();
            inputList.add(input);
        }

        problem4.solution(inputList);
    }
}
