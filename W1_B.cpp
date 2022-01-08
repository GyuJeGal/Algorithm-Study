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

		vector<int> min;
		vector<int> max;
		vector<int> inputData;

		for (int i = 0; i < N; i++)
		{
			int a, b; //a : 질의 종류(1:블록 쌓기 후 출력, 2:위의 블록제거)
			cin >> a;
			if (a == 1) //삽입연산
			{
				cin >> b;

				if (inputData.empty() == true)
				{
					inputData.push_back(b);
					min.push_back(b);
					max.push_back(b);
				}
				else
				{
					inputData.push_back(b);

					if (min.back() > b)
					{
						min.push_back(b);
						max.push_back(max.back());
					}
					else if (max.back() < b)
					{
						max.push_back(b);
						min.push_back(min.back());
					}
					else
					{
						min.push_back(min.back());
						max.push_back(max.back());
					}
				}

				cout << min.back() << " " << max.back() << "\n";
			}
			else //삭제 연산
			{
				if (inputData.empty() == false)
				{
					min.pop_back();
					max.pop_back();

					inputData.pop_back();
				}
			}
		}
	}
}