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
		int N, M; //N : ���� ����, M : ���� ����� ������ Ƚ��
		cin >> N >> M;
		vector<vector<int>> Ball(N + 1); //����) Ball[1]���� 1�� ���� �� ������ ���� ����
										       //Ball[2]���� 2�� ���� �� ������ ���� ����
		vector<int> Va;
		vector<int> Vb;

		int a, b;
		for (int i = 0; i < M; i++)
		{
			cin >> a >> b; //a�� b���� ���ſ�
			Va.push_back(a);
			Vb.push_back(b);
		}

		for (int i = 0; i < M; i++) //���� ���������� �������� �״�� ����
		{
			Ball[Va[i]].push_back(Vb[i]);
		}

		for (int i = 1; i <= N; i++)
		{
			// i�� üũ�� ���� ��ȣ
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