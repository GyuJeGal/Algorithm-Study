#include <iostream>

using namespace std;

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int T;
	cin >> T;
	while (T--)
	{
		double x1, y1, x2, y2;
		cin >> x1 >> y1 >> x2 >> y2;

		double x3, y3, x4, y4;
		cin >> x3 >> y3 >> x4 >> y4;


		if (x1 == x2 || x3 == x4)
		{
			if ((x1 == x2) && (x3 == x4)) //두 직선 모두 y축과 평행
			{
				if (x1 != x3) //서로 평행하고 교점이 없음
				{
					cout << 1 << "\n";
				}
				else
				{
					if (y1 < y2) swap(y1, y2);
					if (y3 < y4) swap(y3, y4);
					if (y2 > y3)
					{
						cout << 1 << "\n";
					}
					else if (y2 == y3)
					{
						cout << 2 << "\n";
					}
					else if (y1 < y4)
					{
						cout << 1 << "\n";
					}
					else if (y1 == y4)
					{
						cout << 2 << "\n";
					}
					else if (y2 > y4 && y1 > y3)
					{
						cout << 3 << "\n";
					}
					else if (y2 < y4 && y1 < y3)
					{
						cout << 3 << "\n";
					}
					else
					{
						cout << 4 << "\n";
					}
				}
			}
			else if (x1 == x2 && x3 != x4) //x1 == x2이고 x3 != x4의 경우
			{
				if (x3 > x1 && x4 > x1)
				{
					cout << 1 << "\n";
				}
				else if (x3 < x1 && x4 < x1)
				{
					cout << 1 << "\n";
				}
				else
				{
					int a = y1 - y3;
					int b = y2 - y3;
					if (a * b <= 0)
					{
						cout << 2 << "\n";
					}
					else
					{
						cout << 1 << "\n";
					}
				}
			}

			else //x3 == x4이고 x1 != x2의 경우
			{
				if (x1 > x3 && x2 > x3)
				{
					cout << 1 << "\n";
				}
				else if (x1 < x3 && x2 < x3)
				{
					cout << 1 << "\n";
				}
				else
				{
					int a = y3 - y1;
					int b = y4 - y1;
					if (a * b <= 0)
					{
						cout << 2 << "\n";
					}
					else
					{
						cout << 1 << "\n";
					}
				}
			}
		}
		else
		{
			if (y3 != y1)
			{
				cout << 1 << "\n";
			}
			else
			{
				if (x1 < x2) swap(x1, x2);
				if (x3 < x4) swap(x3, x4);

				if (x2 > x3)
				{
					cout << 1 << "\n";
				}
				else if (x2 == x3)
				{
					cout << 2 << "\n";
				}
				
				else if (x1 < x4)
				{
					cout << 1 << "\n";
				}
				else if (x1 == x4)
				{
					cout << 2 << "\n";
				}
				else if (x1 > x3 && x2 > x4)
				{
					cout << 3 << "\n";
				}
				else if (x2 < x4 && x1 < x3)
				{
					cout << 3 << "\n";
				}
				else
				{
					cout << 4 << "\n";
				}
			}
		}
	}
}