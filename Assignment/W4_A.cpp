#include <iostream>

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
		int a, b, x, y;
		cin >> a >> b >> x >> y;

		if (a < b)
			swap(a, b);
		int dif = a - b;

		int costx, costy; //ȣ������ �ִ�� �Ҷ� ���õ� ������ ���(x�� Ƚ��), ������  ���(y�� Ƚ��)

		costx = (dif - (b % dif)) * x;

		if (b < dif)
		{
			cout << dif << " " << costx << "\n";
		}
		else
		{
			costy = (b % dif) * y;
			
			if(costx < costy)
				cout << dif << " " << costx << "\n";
			else
				cout << dif << " " << costy << "\n";
		}
		

	}


}