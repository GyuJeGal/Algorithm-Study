#include <iostream>

using namespace std;

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int t;
	cin >> t;
	while (t--)
	{
		double x1, y1, x2, y2;
		cin >> x1 >> y1 >> x2 >> y2;

		double x3, y3, x4, y4;
		cin >> x3 >> y3 >> x4 >> y4;

		if (x1 == x2 || x3 == x4)
		{
			if (x1 == x2 && x3 == x4) //�� ���� ��� y�࿡ �����Ҷ�
			{
				if (x1 != x3) //���� �����ϰ� ������ ����
				{
					cout << 1 << "\n";
				}
				else
				{
					if (y1 < y2) swap(y1, y2);
					if (y3 < y4) swap(y3, y4);
					if (y2 > y3)
					{
						cout << 1 << "\n";
					}
					else if (y2 == y3)
					{
						cout << 2 << "\n";
					}
					else if (y1 < y4)
					{
						cout << 1 << "\n";
					}
					else if (y1 == y4)
					{
						cout << 2 << "\n";
					}
					else if (y2 > y4 && y1 > y3)
					{
						cout << 3 << "\n";
					}
					else if (y2 < y4 && y1 < y3)
					{
						cout << 3 << "\n";
					}
					else
					{
						cout << 4 << "\n";
					}
				}
			}
			else if (x1 == x2) //x1 == x2�̰� x3 != x4�� ���
			{
				if (x3 > x1 && x4 > x1)
				{
					cout << 1 << "\n";
				}
				else if (x3 < x1 && x4 < x1)
				{
					cout << 1 << "\n";
				}
				else
				{
					double b = (y4 - y3) / (x4 - x3); //����
					double n2 = y3 - b * x3; //y����

					double check1 = (b * x1) + n2 - y1;
					double check2 = (b * x2) + n2 - y2;

					if (check1 * check2 <= 0)
					{
						cout << 2 << "\n";
					}
					else
					{
						cout << 1 << "\n";
					}
				}
			}

			else //x3 == x4�̰� x1 != x2�� ���
			{
				if (x1 > x3 && x2 > x3)
				{
					cout << 1 << "\n";
				}
				else if (x1 < x3 && x2 < x3)
				{
					cout << 1 << "\n";
				}
				else
				{
					double a = (y2 - y1) / (x2 - x1); //����
					double n1 = y1 - a * x1; //y����

					double check1 = (a * x3) + n1 - y3;
					double check2 = (a * x4) + n1 - y4;

					if (check1 * check2 <= 0)
					{
						cout << 2 << "\n";
					}
					else
					{
						cout << 1 << "\n";
					}
				}
			}
			continue;
		}

		double a, b;//�� ������ ����
		a = (y2 - y1) / (x2 - x1);
		b = (y4 - y3) / (x4 - x3);

		double n1, n2; //y����
		n1 = y1 - a * x1;
		n2 = y3 - b * x3;

		if (a == b) // ���Ⱑ ������
		{
			if (n1 == n2) //��ġ, ����, ��ħx, �Ϻ� �Ǵ� ���������� ��ħ ���ɼ� ����
			{
				if (a == 0) //x��� ������ ��츦 �������ߵ�, ���� �ڵ�� y������ ���翵���� ������ y���� ���ؼ��� �ٷ�� ����
				{
					if (x1 < x2) swap(x1, x2);
					if (x3 < x4) swap(x3, x4);

					if (x2 > x3)
					{
						cout << 1 << "\n";
					}
					else if (x2 == x3)
					{
						cout << 2 << "\n";
					}

					else if (x1 < x4)
					{
						cout << 1 << "\n";
					}
					else if (x1 == x4)
					{
						cout << 2 << "\n";
					}
					else if (x1 > x3 && x2 > x4)
					{
						cout << 3 << "\n";
					}
					else if (x2 < x4 && x1 < x3)
					{
						cout << 3 << "\n";
					}
					else
					{
						cout << 4 << "\n";
					}
				}
				else
				{
					if (y1 < y2) swap(y1, y2);
					if (y3 < y4) swap(y3, y4);

					if (y2 > y3)
					{
						cout << 1 << "\n";
					}
					else if (y2 == y3)
					{
						cout << 2 << "\n";
					}
					else if (y1 < y4)
					{
						cout << 1 << "\n";
					}
					else if (y1 == y4)
					{
						cout << 2 << "\n";
					}
					else if (y2 > y4 && y1 > y3)
					{
						cout << 3 << "\n";
					}
					else if (y2 < y4 && y1 < y3)
					{
						cout << 3 << "\n";
					}
					else
					{
						cout << 4 << "\n";
					}
				}
			}
			else
			{
				cout << 1 << "\n";
			}
		}
		else //���Ⱑ �ٸ���
		{

			double check1 = (b * x1) + n2 - y1;
			double check2 = (b * x2) + n2 - y2;
			double check3 = (a * x3) + n1 - y3;
			double check4 = (a * x4) + n1 - y4;

			if (check1 * check2 <= 0 && check3 * check4 <= 0)
			{
				cout << 2 << "\n";
			}
			else
			{
				cout << 1 << "\n";
			}


		}
	}
}