package src;

import java.util.*;

public class Problem3 {
    public void solution(List<Integer> nums) {
        List<Integer> rank = new ArrayList<>();

        for(int num : nums) {
            int count = 1; //자기 보다 점수가 높은 사람이 있으면 +1, 아예 없으면 1위
            for(int check : nums) {
                if(num < check) {
                    count++;
                }
            }
            rank.add(count);
        }

        for (int rankValue : rank) {
            System.out.print(rankValue + " ");
        }
    }

    public static void main(String[] args) {
        Problem3 problem3 = new Problem3();
        Scanner sc = new Scanner(System.in);

        int count = sc.nextInt();
        sc.nextLine();

        List<Integer> arrayList = new ArrayList();
        for(int i = 0; i < count; i++) {
            int num = sc.nextInt();
            arrayList.add(num);
        }

        problem3.solution(arrayList);
    }
}
