#include <iostream>

using namespace std;

class Pair
{
public:
	Pair(long long a, long long b) { exp = a, sum = b; };
	long long exp;
	long long sum;
};

Pair Sum(long long X, long long N, long long M)
{
	if (N == 1)
	{
		Pair A(X % M, X % M);
		return A;
	}

	Pair answer = Sum(X, N / 2, M);

	long long a = answer.exp;
	long long b = answer.sum;
	
	if (N % 2 == 0) //NÀÌ Â¦¼ö
	{
		answer.exp = (a * a) % M;
		answer.sum = ((a + 1) * b) % M;
	}
	else //NÀÌ È¦¼ö
	{
		answer.exp = (X * a * a) % M;
		answer.sum = (X + X * (a + 1) * b) % M;
	}

	return answer;
}

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int T;
	cin >> T;
	while (T--)
	{
		long long X, N, M;
		cin >> X >> N >> M;

		Pair result = Sum(X, N, M);

		cout << result.sum << "\n";
	}
}