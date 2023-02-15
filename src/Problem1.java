package src;

import java.util.Scanner;

public class Problem1 {
    public int solution(String str, char c) {
        int result = 0;

        str = str.toUpperCase();
        c = Character.toUpperCase(c);

        for (char i : str.toCharArray()){
            if (i == c) {
                result++;
            }
        }
        return result;
    }

    public static void main(String[] args) {
        Problem1 problem1 = new Problem1();

        Scanner scanner = new Scanner(System.in);

        String inputStr = scanner.nextLine();

        char inputChar = scanner.next().charAt(0);

        System.out.print(problem1.solution(inputStr, inputChar));
    }

}
