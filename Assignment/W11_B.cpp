#include <iostream>
#include <queue>
#include <vector>

using namespace std;

class Point
{
public:
	Point(int a, int b, int c)
	{
		x = a, y = b, size = c;
	};
	int x;
	int y;
	int size;
};

bool check(int x, int y, int size, vector<vector<char>> &V)
{
	char c = V[x][y];
	for (int i = 0; i < size; i++)
	{
		for (int p = 0; p < size; p++)
		{
			if (V[x + p][y + i] != c)
			{
				return false;
			}
		}
	}
	return true;
}

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int T;
	cin >> T;
	while (T--)
	{
		int N;
		cin >> N; // 종이의 크기

		vector<vector<char>> Paper(N + 1, vector<char>(N + 1));

		for (int i = 1; i <= N; i++) //초기 설정
		{
			for (int p = 1; p <= N; p++)
			{
				char c;
				cin >> c;
				Paper[i][p] = c;
			}
		}

		int red = 0, blue = 0; //빨간색, 파란색 종이의 개수
		int red_size = 0, blue_size = 0; //빨간색, 파란색 종이들의 크기 합

		queue<Point> Q;
		Point p(1, 1, N);
		Q.push(p);
		while (Q.size() != 0)
		{
			int x = Q.front().x;
			int y = Q.front().y;
			int size = Q.front().size;

			Q.pop();

			if (check(x, y, size, Paper) == true)
			{
				if (Paper[x][y] == 'R')
				{
					red++;
					red_size += size * size;
				}
				else
				{
					blue++;
					blue_size += size * size;
				}
			}
			else
			{
				Point p1(x, y, size / 2);
				Point p2(x + size/2, y, size / 2);
				Point p3(x, y + size/2, size / 2);
				Point p4(x + size/2, y + size/2, size / 2);

				Q.push(p1);
				Q.push(p2);
				Q.push(p3);
				Q.push(p4);
			}
		}

		cout << red << " " << red_size << " " << blue << " " << blue_size << "\n";

	}

}