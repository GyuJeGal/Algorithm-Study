import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Problem17298 {

    static class Pair {
        int value;
        int index;

        public Pair(int value, int index) {
            this.value = value;
            this.index = index;
        }
    }

    static int[] solution(int N, int[] A) throws Exception {
        int[] answer = new int[N];

        ArrayDeque<Main.Pair> que = new ArrayDeque<>();

        for (int i = 0; i < N; i++) {
            if (que.isEmpty()) {
                que.addLast(new Main.Pair(A[i], i));
            }
            else {
                while (true) {
                    if (que.isEmpty()) {
                        break;
                    }
                    if (que.getLast().value < A[i]) {
                        // que에서 뒤에 값 빼고 answer 갱신
                        Main.Pair last = que.pollLast();
                        answer[last.index] = A[i];
                    }
                    else {
                        break;
                    }
                }
                que.addLast(new Main.Pair(A[i], i));
            }
        }

        int size = que.size();

        for (int i = 0; i < size; i++) {
            Main.Pair last = que.pollLast();
            answer[last.index] = -1;
        }

        return answer;
    }
}
