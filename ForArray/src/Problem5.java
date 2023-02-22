package src;

import java.util.*;

public class Problem5 {
    public int solution(int N, int k, int[] arr) {
        int result = 0, cur = 0;

        boolean stop = false;

        while(!stop) {
            int check = 0, sum = 0;

            for(int i = cur; i < N; i++) {
                if(arr[i] == 0) {
                    if(check == 2) {
                        break;
                    }
                    if(check == 0) {
                        cur = i + 1;
                    }
                    check++;
                }
                sum++;
                if(i == N -1) {
                    stop = true;
                }
            }
            result = Math.max(result, sum);
        }
        return result;
    }

    public static void main(String[] args) {
        Problem5 problem5 = new Problem5();
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int k = sc.nextInt();
        sc.nextLine();

        int[] arr = new int[N];
        for (int i = 0; i < N; i++) {
            arr[i] = sc.nextInt();
        }

        System.out.print(problem5.solution(N, k, arr));
    }
}
