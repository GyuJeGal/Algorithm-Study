#include <iostream>
#include <vector>

using namespace std;

int grid[22][22]; //������ (-1:���� ��, 0:�� ����, 1:��, 2:��)

struct point_info
{
	int x;
	int y;
};

vector<point_info> candidate;
vector<int> check[21][21][3]; 
//check[x][y][1]:(x, y)��ǥ�� �浹�� �������� �������� �鵹�� ������ ����
//check[x][y][2]:(x, y)��ǥ�� �鵹�� �������� �������� �浹�� ������ ����

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
		int n, Q; //n:������ ũ��, Q:�Է��� ����
		cin >> n >> Q;
		
		//���� �ʱ� �� ����
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