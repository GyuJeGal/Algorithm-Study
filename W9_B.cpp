#include <iostream>
#include <vector>

using namespace std;

int grid[22][22]; //격자판 (-1:범위 밖, 0:돌 없음, 1:흑, 2:백)

struct point_info
{
	int x;
	int y;
};

vector<point_info> candidate;
vector<int> check[21][21][3]; 
//check[x][y][1]:(x, y)좌표에 흑돌을 놓았을때 뒤집히는 백돌의 방향을 저장
//check[x][y][2]:(x, y)좌표에 백돌을 놓았을때 뒤집히는 흑돌의 방향을 저장

int dx[8] = {0, 1, 1, 1, 0, -1, -1, -1};
int dy[8] = {1, 1, 0, -1, -1, -1, 0, 1};


int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int T;
	cin >> T;
	while (T--)
	{
		int n, Q; //n:격자판 크기, Q:입력의 개수
		cin >> n >> Q;
		
		//게임 초기 돌 세팅
		grid[n / 2][n / 2] = 1;
		grid[n / 2][n / 2 + 1] = 2;
		grid[n / 2 + 1][n / 2] = 2;
		grid[n / 2 + 1][n / 2 + 1] = 1;

		for (int i = 0; i < Q; i++)
		{
			int r, c;
			cin >> r >> c;

		}
	}
}