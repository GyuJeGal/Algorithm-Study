#include <iostream>
#include <queue>
#include <vector>

using namespace std;

class check
{
public:
	check(int a, int b) { order = a, value = b; };
	int order;
	int value;
};

struct cmp
{
	bool operator()(check a, check b)
	{
		return a.value < b.value;
	}
};

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int t;
	cin >> t;
	while (t--)
	{
		int n;
		cin >> n;
		int resulta = 0, resultb = 0;
		vector<int> a, b; //a = ÀÎÇÏ, b = ºñ·æ ¿Õ±¹ÀÇ ÀÚ¿ø °¡Ä¡
		priority_queue < check, vector < check>, cmp > q;

		for (int i = 0; i < n; i++)
		{
			int a, b;
			cin >> a >> b;
			a.push_back(a), b.push_back(b);
			check c(i, a + b);
			q.push(c);
		}

		for (int i = 0; i < n; i++)
		{
			if (i % 2 == 0) //ÀÎÇÏ ¿Õ±¹ Â÷·Ê
			{
				int index = q.top().order;
				resulta += a[index];
				q.pop();
			}
			else //ºñ·æ ¿Õ±¹ Â÷·Ê
			{
				int index = q.top().order;
				resultb += b[index];
				q.pop();
			}
		}

		cout << resulta - resultb << "\n";

	}



}