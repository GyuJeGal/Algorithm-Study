import java.util.*;
import java.io.*;

public class Problem14567 {

    static class Node {
        int vertex;
        int semester;

        public Node(int v, int s) {
            this.vertex = v;
            this.semester = s;
        }
    }

    void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        // 연결관계 그래프
        ArrayList<Integer>[] graph = new ArrayList[N + 1];
        for (int i = 0; i < N + 1; i++) {
            graph[i] = new ArrayList<>();
        }
        // 진입차수 저장
        int[] inDegree = new int[N + 1];

        // 선수강 관계 입력
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());

            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            graph[a].add(b);
            inDegree[b]++;
        }

        // 위상정렬 큐
        ArrayDeque<Node> que = new ArrayDeque<>();
        // 결과
        int[] answer = new int[N + 1];

        // 첫학기에 들을 과목 저장
        for (int i = 1; i < N + 1; i++) {
            if (inDegree[i] == 0) {
                que.addLast(new Node(i, 1));
            }
        }

        // 위상정렬 시작
        while (!que.isEmpty()) {
            Node node = que.pollFirst();
            int cur = node.vertex;
            int curSemester = node.semester;

            answer[cur] = curSemester;

            for (int j = 0; j < graph[cur].size(); j++) {
                inDegree[graph[cur].get(j)]--;
                // 연결된 정점의 진입차수가 0인 경우, 큐에 넣기
                if (inDegree[graph[cur].get(j)] == 0) {
                    que.addLast(new Node(graph[cur].get(j), curSemester + 1));
                }
            }

        }

        StringBuilder sb = new StringBuilder();
        for (int i = 1; i < N + 1; i++) {
            sb.append(answer[i]).append(' ');
        }

        System.out.println(sb);

    }

}
