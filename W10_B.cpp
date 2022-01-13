#include <iostream>
#include <vector>

using namespace std;

class check
{
public:
	check(int a) { size = a, smaller = 0; };
	int size;
	int smaller; //앞index중 자기 보다 작은 것의 개수 
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
		cin >> N;
		vector<check> V;
		for (int i = 0; i < N; i++)
		{
			int A;
			cin >> A;
			check a(A);
			V.push_back(a);
		}

		vector<check> result;

		for (int i = 0; i < N; i++)
		{
			if (i == 0)
			{
				V[i].smaller = 0;
				result.push_back(V[i]);
			}
			else
			{
				vector<check> Q;

				for (int p = 0; p < i; p++)
				{
					if (V[p].size < V[i].size)
					{
						if (Q.empty() == true)
							Q.push_back(V[p]);
						else
						{
							if (Q.back().smaller < V[p].smaller)
								Q.push_back(V[p]);
						}
					}
				}
				if (Q.empty() == true)
				{
					V[i].smaller = 0;
				}
				else
				{
					V[i].smaller = Q.back().smaller + 1;
				}
				
				if (result.back().smaller < V[i].smaller)
				{
					result.push_back(V[i]);
				}
			}
		}
		cout << result.back().smaller + 1 << "\n";

	}

}