//삼각형 경로 문제

#include <iostream>
#include <vector>

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
		int N;
		cin >> N;
		vector<vector<int>> Data(N + 1, vector<int> (1, 0));
		vector<vector<int>> Path(N + 1, vector<int> (1, 0));

		for (int i = 1; i <= N; i++)
		{
			for (int p = 1; p <= i; p++)
			{
				int A;
				cin >> A;
				Data[i].push_back(A);
			}
		}

		Path[1].push_back(Data[1][1]);
		for (int i = 2; i <= N; i++)
		{
			Path[i].push_back(Path[i - 1][1] + Data[i][1]);
			for (int p = 2; p <= i - 1; p++)
			{
				if (Path[i - 1][p - 1] < Path[i - 1][p])
				{
					Path[i].push_back(Path[i - 1][p - 1] + Data[i][p]);
				}
				else
				{
					Path[i].push_back(Path[i - 1][p] + Data[i][p]);
				}
			}
			Path[i].push_back(Path[i - 1][i - 1] + Data[i][i]);
		}

		int answer = Path[N][1];
		for(int i = 2; i <= N; i++)
		{
			if (answer > Path[N][i])
				answer = Path[N][i];
		}
		cout << answer << "\n";
	}
}