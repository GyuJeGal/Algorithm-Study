#include <iostream>
#include <vector>
#include <queue>

using namespace std;

class point
{
public:
	point() {};
	int x, y;
};

class node
{
public:
	node() { visit = 0, count = 0; };
	int visit;
	int count;
};

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int T;
	cin >> T;
	while (T--)
	{
		int N; //N : 좌표평면의 크기
		point A, B, C, D; //A : 인하, B : 안전 지역, C : 검사, D : 소총수
		
		int x1, x2, x3, x4;
		int y1, y2, y3, y4;

		cin >> N;

		vector<vector<node>> V(N + 2, vector<node>(N + 2)); //범위 밖을 넘어서는 것을 방지하는 경계선 때문에 사이즈를 +2 해야됨

		cin >> x1 >> y1 >> x2 >> y2;
		cin >> x3 >> y3 >> x4 >> y4;

		A.x = x1, A.y = y1;
		B.x = x2, B.y = y2;
		C.x = x3, C.y = y3;
		D.x = x4, D.y = y4;

		int dx[8] = {0, 1, 1, 1, 0, -1, -1, -1}; //윗방향부터 시계방향으로 돌기
		int dy[8] = {1, 1, 0, -1, -1, -1, 0, 1};


		//위험 지역 표시
		for (int i = 0; i < N + 2; i++) //x좌표가 0, N + 1인 경우 && y좌표가 0, N + 1인 경우는 위험지역 표시한다
		{
			V[i][0].visit = -1;
			V[i][N + 1].visit = -1;
			V[0][i].visit = -1;
			V[N + 1][i].visit = -1;
		}
		for (int i = 0; i < 8; i++) //소총수 부터 위험 지역 표시
		{
			for (int p = 1; p < N + 1; p++)
			{
				if (D.x + dx[i] * p < 1 || D.x + dx[i] * p > N
					|| D.y + dy[i] * p < 1 || D.y + dy[i] * p > N) //좌표평면을 벗어나는 경우
					break;
				if (D.x + dx[i] * p == C.x && D.y + dy[i] * p == C.y)
					break;
				V[D.x + dx[i] * p][D.y + dy[i] * p].visit = -1;
			}
		}
		for (int i = 0; i < 8; i++) //검사 위험 지역 표시
		{
			//좌표평면을 벗어나는 경우를 체크 안해도 됨. 이미 좌표평면 둘러서 한칸씩은 경계로 -1 해놓음
			//단, 소총수는 break를 해줘야됨.
			V[C.x + dx[i]][C.y + dy[i]].visit = -1;
		}
		V[A.x][A.y].visit = -1;
		//위험 표시 끝
		
		queue<point> Q;
		Q.push(A);
		while (Q.empty() == false)
		{
			int x = Q.front().x;
			int y = Q.front().y;
			Q.pop();

			for (int i = 0; i < 8; i++)
			{
				if (V[x + dx[i]][y + dy[i]].visit == 0) //갈 수 있는 좌표평면일 때
				{
					point newPoint;
					newPoint.x = x + dx[i], newPoint.y = y + dy[i];
					Q.push(newPoint);
					V[x + dx[i]][y + dy[i]].visit = -1;
					V[x + dx[i]][y + dy[i]].count = V[x][y].count + 1;
				}
			}
		}
		cout << V[B.x][B.y].count << "\n";

	}
}