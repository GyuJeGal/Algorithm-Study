package src;

import java.util.*;

public class Problem4 {
    public int solution(int N, int M, int[][] ranks) {
        List<List<Integer>> candidates = new ArrayList<>();

        for(int i = 0; i <= N; i++) {
            List<Integer> nums = new ArrayList<>();
            for(int j = 1; j <= N; j++) {
                // 자신의 번호는 멘티 후보에 저장 안함
                if(i != j) {
                    nums.add(j);
                }
            }
            candidates.add(nums);
        }
        
        for(int i = 1; i <= M; i++) {
            //2등 부터 등수 확인해서 후보 제거
            for(int j = 2; j <= N; j++) {
                int studentNum = ranks[i][j];

                for(int k = 1; k < j; k++) {
                    int removeCandidate = ranks[i][k];

                    if(candidates.get(studentNum).contains(removeCandidate)) {
                        int index = candidates.get(studentNum).indexOf(removeCandidate);
                        candidates.get(studentNum).remove(index);
                    }
                }
            }
        }

        int result = 0;
        for(int i = 1; i <= N; i++) {
            result += candidates.get(i).size();
        }
        return result;
    }

    public static void main(String[] args) {
        Problem4 problem4 = new Problem4();
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int M = sc.nextInt();
        sc.nextLine();

        int[][] ranks = new int[M + 1][N + 1];

        for(int i = 0; i < M; i++) {
            for(int j = 0; j < N; j++) {
                int num = sc.nextInt();
                ranks[i + 1][j + 1] = num;
            }
            sc.nextLine();
        }

        System.out.print(problem4.solution(N, M, ranks));
    }
}
