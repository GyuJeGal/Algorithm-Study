#include <iostream>
#include <queue>
#include <vector>

using namespace std;

class oneRoom
{
public:
	oneRoom(int a, int b) 
	{
		score = a;
		distance = b;
	};
	int score;
	int distance;
};

struct cmp
{
	bool operator()(oneRoom a, oneRoom b)
	{
		return b.score > a.score;
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
		int N;
		cin >> N; //N:¹æÀÇ ¼ö

		vector<oneRoom> V;
		priority_queue<oneRoom, vector<oneRoom>, cmp> Q;

		for (int i = 0; i < N; i++)
		{
			int A, B;
			cin >> A >> B;

			oneRoom newRoom(A, B);
			Q.push(newRoom);
		}
		for (int i = 0; i < N; i++)
		{
			V.push_back(Q.top());
			Q.pop();
		}

		int answer = 0, minDistance;
		for (int i = 0; i < N; i++)
		{
			if (i == 0)
			{
				answer++;
				minDistance = V[i].distance;
			}
			else
			{
				if (V[i].distance < minDistance)
				{
					answer++;
					minDistance = V[i].distance;
				}
			}
		}
		cout << answer << "\n";
	}

}