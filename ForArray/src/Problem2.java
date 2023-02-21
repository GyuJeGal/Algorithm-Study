package src;

import java.util.ArrayList;
import java.util.Scanner;

public class Problem2 {
    public void solution(ArrayList<Integer> nums) {
        for(int num : nums) {
            if(isPrime(toReverse(num))) {
                System.out.print(toReverse(num) + " ");
            }
        }
    }

    public int toReverse(int num) {
        ArrayList<Integer> arrayList = new ArrayList();

        int check = num;
        while(check != 0) {
            int element = check % 10;
            arrayList.add(element);
            check = check / 10;
        }

        int result = 0;

        for(int i = 0; i < arrayList.size(); i++) {
            result += arrayList.get(i) * Math.pow(10, arrayList.size() - 1 - i);
        }

        return result;
    }

    public boolean isPrime(int num) {
        if(num == 1) {
            return false;
        }

        int sqrtNum = (int) Math.sqrt(num) + 1;
        for(int i = 2; i < sqrtNum; i++) {
            if(num % i == 0) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        Problem2 problem2 = new Problem2();
        Scanner sc = new Scanner(System.in);

        int count = sc.nextInt();
        sc.nextLine();

        ArrayList<Integer> nums = new ArrayList<>();
        for(int i = 0; i < count; i++) {
            int num = sc.nextInt();
            nums.add(num);
        }
        problem2.solution(nums);
    }
}
