package src;

import java.util.ArrayList;
import java.util.Scanner;

public class Problem9 {
    public void solution(String input) {
        ArrayList<ArrayList<Character>> resultList = new ArrayList<ArrayList<Character>>();

        ArrayList<Character> candidate = new ArrayList();
        for (Character c : input.toCharArray()) {
            if (candidate.isEmpty()) {
                candidate.add(c);
            }
            else {
                if (candidate.get(0) != c) {
                    resultList.add(candidate);
                    candidate = new ArrayList();
                    candidate.add(c);
                }
                else {
                    candidate.add(c);
                }
            }
        }
        resultList.add(candidate);

        for(ArrayList<Character> check : resultList) {
            System.out.print(check.get(0));
            if (check.size() != 1) {
                System.out.print(check.size());
            }
        }
    }

    public static void main(String[] args) {
        Problem9 problem9 = new Problem9();
        Scanner sc = new Scanner(System.in);

        String input = sc.next();

        problem9.solution(input);
    }
}
