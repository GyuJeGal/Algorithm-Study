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
		int N, M; // N : 친구들의 수, M : 단어의 수
		cin >> N >> M;
		vector<check> V; //교수님이 말한 문장
		vector<queue<string>> Q(N); // 학생들이 필기한 단어들
		
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
		int count = 1; //밑에 for문을 돌고 1이면 성공, 0이면 실패
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