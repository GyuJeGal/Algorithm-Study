#include <iostream>
#include <vector>
#include <queue>

using namespace std;

class person
{
public:
	person(int a, int b) { time = a, price = b; }
	int time;
	int price;
};

class Desk
{
public:
	Desk() { priceSum = 0, timeSum = 0; }
	int order; //�ڱ� ����
	int priceSum;
	int timeSum;
};

struct cmp
{
	bool operator()(Desk a, Desk b)
	{
		if (a.timeSum == b.timeSum)
		{
			return a.order > b.order;
		}
		else
		{
			return a.timeSum > b.timeSum; //������������ ����
		}
	}
};

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int N, M; //N : ������ ��, M : �մ��� ��
	
	cin >> N >> M;

	int T, P; //Time, Price
	vector<Desk> D(N); //����
	vector<person> H; //����� ��ٸ��� �����
	priority_queue<Desk, vector<Desk>, cmp> Q;

	for (int i = 0; i < M; i++)
	{
		cin >> T >> P;

		person h(T, P);
		H.push_back(h);
	}

	for (int i = 0; i < M; i++)
	{
		if (i < N) //ó���� ���밡 �� �������� ��
		{
			D[i].order = i;
			D[i].priceSum += H[i].price;
			D[i].timeSum += H[i].time;
			Q.push(D[i]);
		}
		else
		{
			int n = Q.top().order;
			Q.pop();
			D[n].priceSum += H[i].price;
			D[n].timeSum += H[i].time;
			Q.push(D[n]);
		}
		
	}
	for (int i = 0; i < N - 1; i++)
	{
		Q.pop();
	}
	cout << Q.top().timeSum << "\n";

	Q.pop();

	for(int i = 0; i < N; i++)
	{
		cout << D[i].priceSum << "\n";
	}

}