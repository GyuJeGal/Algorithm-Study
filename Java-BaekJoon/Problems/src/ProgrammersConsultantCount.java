import java.util.*;

public class ProgrammersConsultantCount {
    static class Mentor {
        int endTime = 0;

        public Mentor() {}
    }

    class Solution {
        public ArrayList<ArrayList<Integer>> mentorArrange(int k, int n) {
            ArrayList<ArrayList<Integer>> result = new ArrayList<>();

            ArrayDeque<ArrayList<Integer>> deque = new ArrayDeque<>();

            for (int i = 1; i <= n - k + 1; i++) {
                ArrayList<Integer> dum = new ArrayList<>();
                dum.add(i);
                deque.addLast(dum);
            }

            while (true) {
                if (deque.peekFirst().size() == k) break;

                ArrayList<Integer> cur = deque.poll();

                int sum = 0;
                for (int i = 0; i < cur.size(); i++) {
                    sum += cur.get(i);
                }

                int limit = (n - sum) - (k - cur.size()) + 1;
                for (int i = 1; i <= limit; i++) {
                    ArrayList<Integer> temp = new ArrayList<>();
                    for (int j = 0; j < cur.size(); j++) {
                        temp.add(cur.get(j));
                    }
                    temp.add(i);
                    deque.addLast(temp);
                }
            }

            while (!deque.isEmpty()) {
                result.add(deque.pollFirst());
            }

            return result;
        }

        public int solution(int k, int n, int[][] reqs) {
            int answer = 10000000;

            // 완전탐색으로 멘토 유형 배정
            ArrayList<ArrayList<Integer>> cases = mentorArrange(k, n);

            // 배정된 멘토 유형으로 기다리는 시간 계산
            for (ArrayList<Integer> mentorCount : cases) {
                ArrayList<ArrayList<Mentor>> mentors = new ArrayList<>();

                mentors.add(new ArrayList<Mentor>());

                for (int i = 0; i < k; i++) {
                    ArrayList<Mentor> temp = new ArrayList<>();
                    for (int j = 0; j < mentorCount.get(i); j++) {
                        temp.add(new Mentor());
                    }
                    mentors.add(temp);
                }

                int waitTime = 0;

                // reqs 배열을 돌면서 기다리는 시간 계산하기
                for (int i = 0; i < reqs.length; i++) {
                    if (waitTime >= answer) break;

                    int start = reqs[i][0];
                    int duration = reqs[i][1];
                    int type = reqs[i][2];

                    int idx = 0;
                    int MIN = 1200;

                    for (int j = 0; j < mentors.get(type).size(); j++) {
                        Mentor mentor = mentors.get(type).get(j);

                        if (mentor.endTime < MIN) {
                            idx = j;
                            MIN = mentor.endTime;
                        }
                    }
                    // 기다려야 되는 경우
                    if (start < mentors.get(type).get(idx).endTime) {
                        waitTime += mentors.get(type).get(idx).endTime - start;
                        mentors.get(type).get(idx).endTime += duration;
                    }
                    // 기다림 없이 바로 가능한 경우
                    else {
                        mentors.get(type).get(idx).endTime = start + duration;
                    }

                }

                answer = Math.min(answer, waitTime);
            }

            return answer;
        }
    }
}
