#include <iostream>
#include <string>
#include <cmath>
#include <vector>

using namespace std;

int score[24];
int getScore[10000000]; //각 Status에 대해 점수 저장
bool check[10000000]; //각 Status에 대해 영어단어 만들 수 있는지 저장
int result = 0; //결과값 저장
int needAlphabet[24][26];
int restAlphabet[10000000][26];

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	for(int i = 0; i < 26; i++)
	{
		int n;
		cin >> n;

		restAlphabet[0][i] = n;
	}

	int M; //영어단어의 개수
	cin >> M;

	//초기값 설정
	getScore[0] = 0;
	check[0] = true;

	for (int i = 1; i <= M; i++)
	{
		string str;
		int num;
		cin >> str >> num;

		score[i] = num;
		for (int p = 0; p < str.size(); p++)
		{
			int index = str[p] - 97;
			needAlphabet[i][index]++;
		}
	}

	for (int i = 1; i <= M; i++)
	{
		int status = pow(2, i - 1);
		for (int j = 0; j < status; j++)
		{
			if (check[j] == false)
			{
				check[j + status] = false;
				getScore[j + status] = 0;
			}
			else
			{
				int flag = 0; //0이면 영어단어 만들 수 있음, 1이면 못만듦.

				for (int o = 0; o < 26; o++)
				{
					if (restAlphabet[j][o] < needAlphabet[i][o])
					{
						flag = 1;
						break;
					}
				}
				if (flag == 1)
				{
					check[j + status] = false;
					getScore[j + status] = 0;
				}
				else //영어단어를 만들 수 있을 때
				{
					for (int o = 0; o < 26; o++)
						restAlphabet[j + status][o] = restAlphabet[j][o] - needAlphabet[i][o];
					check[j + status] = true;
					getScore[j + status] = getScore[j] + score[i];
					if (result < getScore[j + status])
						result = getScore[j + status];
				}
			}
			
		}
	}
	
	cout << result << "\n";
}