#include <iostream>
#include <vector>
#include <queue>

using namespace std;

class Point
{
public:
	Point(int a, int b) 
	{ this->x = a, this->y = b, this->distance = a*a + b*b; };
	int x;
	int y;
	int distance;
};

struct cmp
{
	bool operator()(Point a, Point b)
	{
		if (a.distance == b.distance)
		{
			if (a.x == b.x)
			{
				return a.y < b.y;
			}
			else
			{
				return a.x < b.x;
			}
		}
		else
		{
			return a.distance < b.distance;
		}
	}
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
		int M; //ó�� �����ϴ� �ܹ��� ������ ��
		int N; //���Ӱ� �����Ǵ� �ܹ��� ������ ��
		int K; //���ϰ� �湮�� K��° ����� �ܹ��� ����
		cin >> M >> N >> K;

		priority_queue<Point, vector<Point>, cmp> Q; //ť���� K���� ��ü�� ����(top()�� K��°�� ����� �ܹ��� ����)

		for (int i = 0; i < M; i++) //ó�� �����ϴ� �ܹ��� ����
		{
			int x, y;
			cin >> x >> y;

			if (i < K)
			{
				Point p(x, y);
				Q.push(p);
			}
			else
			{
				Point p(x, y);
				Q.push(p);
				Q.pop();
			}
		}
		for (int i = 0; i < N; i++) //���Ӱ� �����Ǵ� �ܹ��� ����
		{
			int x, y;
			cin >> x >> y;

			Point p(x, y);
			Q.push(p);
			Q.pop();
			
			cout << Q.top().x << " " << Q.top().y << "\n";
		}
	}
}