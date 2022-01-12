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
		int N, M; //N : 공의 개수, M : 양팔 저울로 측정한 횟수
		cin >> N >> M;
		vector<vector<int>> Ball(N + 1); //예시) Ball[1]에는 1번 보다 더 가벼운 공들 저장
										       //Ball[2]에는 2번 보다 더 가벼운 공들 저장
		vector<int> Va;
		vector<int> Vb;

		int a, b;
		for (int i = 0; i < M; i++)
		{
			cin >> a >> b; //a가 b보다 무거움
			Va.push_back(a);
			Vb.push_back(b);
		}

		for (int i = 0; i < M; i++) //먼저 양팔저울의 정보들을 그대로 저장
		{
			Ball[Va[i]].push_back(Vb[i]);
		}

		for (int i = 1; i <= N; i++)
		{
			// i는 체크할 공의 번호
			for (int j = 0; j < Ball[i].size(); j++)
			{
				int check = Ball[i][j];
				if (Ball[check].empty() == false)
				{
					for (int p = 0; p < Ball[check].size(); p++)
					{
						int same = 0;
						int input = Ball[check][p];
						for (int u = 0; u < Ball[i].size(); u++)
						{
							if (input == Ball[i][u])
							{
								same = 1;
								break;
							}
						}
						if (same == 0)
						{
							Ball[i].push_back(input);
						}
					}
					
				}

			}
		}
		for (int i = 1; i <= N; i++)
		{
			if(i == N)
				cout << Ball[i].size() << "\n";
			else
				cout << Ball[i].size() << " ";
		}
	}
}