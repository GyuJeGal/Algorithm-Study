#include <iostream>
#include <string>
#include <vector>
#include <queue>

using namespace std;

class check
{
public:
	check() { correct = false; };
	string str;
	bool correct;	
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
		int N, M; // N : ģ������ ��, M : �ܾ��� ��
		cin >> N >> M;
		vector<check> V; //�������� ���� ����
		vector<queue<string>> Q(N); // �л����� �ʱ��� �ܾ��
		
		for (int i = 0; i < M; i++)
		{
			check C;
			cin >> C.str;
			V.push_back(C);
		}
		for (int i = 0; i < N; i++)
		{
			int k;
			cin >> k;
			string str;
			for (int p = 0; p < k; p++)
			{
				cin >> str;
				Q[i].push(str);
			}
		}
		int count = 1; //�ؿ� for���� ���� 1�̸� ����, 0�̸� ����
		for (int i = 0; i < M; i++)
		{
			for (int p = 0; p < N; p++) 
			{
				if (Q[p].front() == V[i].str)
				{
					V[i].correct = true;
					Q[p].pop();
					break;
				}
			}

			if (V[i].correct == false)
			{
				count = 0;
				break;
			}
		}
	
		cout << count << "\n";
	}
}