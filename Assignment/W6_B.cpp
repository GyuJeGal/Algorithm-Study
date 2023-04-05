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
		int N; //N : ��ǥ����� ũ��
		point A, B, C, D; //A : ����, B : ���� ����, C : �˻�, D : ���Ѽ�
		
		int x1, x2, x3, x4;
		int y1, y2, y3, y4;

		cin >> N;

		vector<vector<node>> V(N + 2, vector<node>(N + 2)); //���� ���� �Ѿ�� ���� �����ϴ� ��輱 ������ ����� +2 �ؾߵ�

		cin >> x1 >> y1 >> x2 >> y2;
		cin >> x3 >> y3 >> x4 >> y4;

		A.x = x1, A.y = y1;
		B.x = x2, B.y = y2;
		C.x = x3, C.y = y3;
		D.x = x4, D.y = y4;

		int dx[8] = {0, 1, 1, 1, 0, -1, -1, -1}; //��������� �ð�������� ����
		int dy[8] = {1, 1, 0, -1, -1, -1, 0, 1};


		//���� ���� ǥ��
		for (int i = 0; i < N + 2; i++) //x��ǥ�� 0, N + 1�� ��� && y��ǥ�� 0, N + 1�� ���� �������� ǥ���Ѵ�
		{
			V[i][0].visit = -1;
			V[i][N + 1].visit = -1;
			V[0][i].visit = -1;
			V[N + 1][i].visit = -1;
		}
		for (int i = 0; i < 8; i++) //���Ѽ� ���� ���� ���� ǥ��
		{
			for (int p = 1; p < N + 1; p++)
			{
				if (D.x + dx[i] * p < 1 || D.x + dx[i] * p > N
					|| D.y + dy[i] * p < 1 || D.y + dy[i] * p > N) //��ǥ����� ����� ���
					break;
				if (D.x + dx[i] * p == C.x && D.y + dy[i] * p == C.y)
					break;
				V[D.x + dx[i] * p][D.y + dy[i] * p].visit = -1;
			}
		}
		for (int i = 0; i < 8; i++) //�˻� ���� ���� ǥ��
		{
			//��ǥ����� ����� ��츦 üũ ���ص� ��. �̹� ��ǥ��� �ѷ��� ��ĭ���� ���� -1 �س���
			//��, ���Ѽ��� break�� ����ߵ�.
			V[C.x + dx[i]][C.y + dy[i]].visit = -1;
		}
		V[A.x][A.y].visit = -1;
		//���� ǥ�� ��
		
		queue<point> Q;
		Q.push(A);
		while (Q.empty() == false)
		{
			int x = Q.front().x;
			int y = Q.front().y;
			Q.pop();

			for (int i = 0; i < 8; i++)
			{
				if (V[x + dx[i]][y + dy[i]].visit == 0) //�� �� �ִ� ��ǥ����� ��
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