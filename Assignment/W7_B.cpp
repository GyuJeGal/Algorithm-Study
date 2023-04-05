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
		int M; //처음 존재하는 햄버거 가게의 수
		int N; //새롭게 생성되는 햄버거 가게의 수
		int K; //인하가 방문할 K번째 가까운 햄버거 가게
		cin >> M >> N >> K;

		priority_queue<Point, vector<Point>, cmp> Q; //큐에는 K개의 객체만 관리(top()은 K번째로 가까운 햄버거 가게)

		for (int i = 0; i < M; i++) //처음 존재하는 햄버거 가게
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
		for (int i = 0; i < N; i++) //새롭게 생성되는 햄버거 가게
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