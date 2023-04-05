#include <iostream>
#include <string>

using namespace std;

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int t;
	cin >> t; 
	while(t--)
	{
		string str; //입력 문자열
		cin >> str;

		int n; //문자열을 배치할 배열의 행
		cin >> n;

		if (n == 1 || n > str.size())
		{
			cout << str << "\n";
		}
		else
		{
			for (int i = 0; i < n; i++)
			{
				for (int o = 0; o < str.size() / n; o++)
				{
					if (i + 2 * n * o > str.size() - 1)
						break;
					cout << str[i + 2 * n * o];

					if (2 * n - 1 - i + 2 * n * o > str.size() - 1)
						break;
					cout << str[2 * n - 1 - i + 2 * n * o];
				}
			}
			cout << "\n";
		}

	}
	

}
