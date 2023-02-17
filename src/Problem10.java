package src;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Problem10 {
    public String solution(int count, String input) {
        String result = "";

        for (int i = 0; i < count; i++) {
            String substringCode = input.substring(i * 7, (i * 7) + 7).replace('#', '1').replace('*', '0');

            int num = Integer.parseInt(substringCode, 2);
            result += (char) num;
        }

        return result;
    }

    public static void main(String[] args) {
        Problem10 problem10 = new Problem10();
        Scanner sc = new Scanner(System.in);

        int count = sc.nextInt();
        sc.nextLine();

        String input = sc.nextLine();

        System.out.print(problem10.solution(count, input));
    }
}
