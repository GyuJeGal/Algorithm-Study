package src;

import java.util.Scanner;

public class Problem1 {
    public int solution(int[] students, int count) {
        int result = 0;

        int maxHeight = 0;

        for (int i = 0; i < count; i++) {
            if(maxHeight < students[i]) {
                result++;
                maxHeight = students[i];
            }
        }
        return result;
    }

    public static void main(String[] args) {
        Problem1 problem1 = new Problem1();
        Scanner sc = new Scanner(System.in);

        int count = sc.nextInt();
        sc.nextLine();

        int[] students = new int[count];

        for (int i = 0; i < count; i++) {
            int height = sc.nextInt();

            students[i] = height;
        }
        System.out.print(problem1.solution(students, count));
    }
}
