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
		int n;
		cin >> n;

		vector<int> inputdata;
		vector<int> cycle;
		vector<int> check;


		for (int i = 0; i < n; i++)
		{
			int x;
			cin >> x;
			inputdata.push_back(x);
		}

		int count = 0; //check point

		for (int i = 0; i < n; i++)
		{
			if (i == 0) //처음 index일때
			{
				cycle.push_back(inputdata[i]);
			}
			else //처음 index가 아닐때
			{
				if (inputdata[i] == cycle[count])
				{
					check.push_back(inputdata[i]);

					if (count == cycle.size() - 1) //cycle 배열의 범위 보다 넘어서면 안됨. 
					{
						count = 0;
					}
					else
					{
						count++;
					}
				}
				else
				{
					if (check.empty() == false)
					{
						for (int p = 0; p < check.size(); p++)
						{
							cycle.push_back(check[p]);
							count = 0;
						}
						check.clear();
						if (inputdata[i] == cycle[count])
						{
							check.push_back(inputdata[i]);
							count++;
						}
						else
						{
							cycle.push_back(inputdata[i]);
						}
					}
					else
						cycle.push_back(inputdata[i]);
				}

			}
		}

		int samev = 0;
		if (cycle[0] == cycle[1])
		{
			samev++;
			for (int i = 0; i < cycle.size(); i++)
			{
				if (cycle[i] == cycle[i + 1])
				{
					samev++;
				}
				else
				{
					break;
				}
			}
		}
		if (samev == 0) //cycle 배열의 처음에 중복되는값이 없을때
		{
			for (int i = 0; i < cycle.size(); i++)
			{
				if (i == cycle.size() - 1)
					cout << cycle[i] << "\n";
				else
					cout << cycle[i] << " ";
			}
		}
		else
		{
			int x= 0;
			for (int i = n - 1; i >= 0; i--)
			{
				if (cycle[0] == inputdata[i])
				{
					x++;
				}
				else
				{
					break;
				}
			}
			if (x > samev)
			{
				int cal = samev - (x % samev);
				while (cal--)
				{
					cycle.pop_back();
				}
			}
			for (int i = 0; i < cycle.size(); i++)
			{
				if (i == cycle.size() - 1)
					cout << cycle[i] << "\n";
				else
					cout << cycle[i] << " ";
			}
		}

	}
}