#include <iostream>
#include <queue>
#include <vector>

using namespace std;

class Point
{
public:
	Point() {room_number = 0, visit = false, time = 0; };
	bool visit;
	int room_number;
	int time;
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
		Point V[10000];
		for (int i = 0; i < 10000; i++)
		{
			V[i].room_number = i;
		}
		int A, B; //A:시작 방번호, B:탈출 방번호
		cin >> A >> B;

		queue<Point> Q;
		V[A].visit = true;
		Q.push(V[A]);
		while (Q.empty() == false)
		{
			Point dum = Q.front();
			Q.pop();
			if (dum.room_number == B)
			{
				cout << dum.time << "\n";
				break;
			}
			else
			{
				if (dum.room_number == 0)
				{
					if (V[1].visit == false)
					{
						//time, visit변수를 갱신하고 Queue에 넣어야함
						V[1].visit = true;
						V[1].time = V[0].time + 1;
						Q.push(V[1]);
					}
				}
				else if (dum.room_number == 9999)
				{
					if (V[9998].visit == false)
					{
						//time, visit변수를 갱신하고 Queue에 넣어야함
						V[9998].visit = true;
						V[9998].time = V[9999].time + 1;
						Q.push(V[9998]);
					}
				}
				else
				{
					if (V[dum.room_number + 1].visit == false)
					{
						//time, visit변수를 갱신하고 Queue에 넣어야함
						V[dum.room_number + 1].visit = true;
						V[dum.room_number + 1].time = V[dum.room_number].time + 1;
						Q.push(V[dum.room_number + 1]);
					}
					if (V[dum.room_number - 1].visit == false)
					{
						//time, visit변수를 갱신하고 Queue에 넣어야함
						V[dum.room_number - 1].visit = true;
						V[dum.room_number - 1].time = V[dum.room_number].time + 1;
						Q.push(V[dum.room_number - 1]);
					}
					int n = dum.room_number;
					int a = n % 10;
					int b = (n % 100 - a) / 10;
					int c = (n % 1000 - b*10 - a) / 100;
					int d = (n - c*100 - b*10 - a) / 1000;
					n = a * 1000 + b * 100 + c * 10 + d;
					if (V[n].visit == false)
					{
						//time, visit변수를 갱신하고 Queue에 넣어야함
						V[n].visit = true;
						V[n].time = V[dum.room_number].time + 1;
						Q.push(V[n]);
					}
				}
			}
		}
	}
}