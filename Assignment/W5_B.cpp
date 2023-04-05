#include <iostream>
#include <vector>

using namespace std;

// Global Variables
int N; // # of houses
int M; // # of resident
vector<int> houseArr;

bool check(int length) {
	int house = 1;
	int residentcount = 0;

	for (int i = 0; i < N; i++) { // houseArr[i]���� ����� ���� �� �ֳ�?
		if (house <= houseArr[i]) { // house������ �ڿ� �ְų� ���� ���̸� houseArr[i]���� ��� ���� �� �ִ�.
			residentcount++; // '��� ����'
			house = houseArr[i] + length; // house : ���� ���̷� ���
		}
	}
	if (residentcount >= M)
		return true;
	else
		return false;

}

int solution(int left, int right) {
	int middle;
	if (left == right) { // answer range = 1
		return left;
	}
	if (left + 1 == right) {// answer range = 2
		if (check(right) == true) {
			return right;
		}
		else {
			return left;
		}
	}
	middle = (left + right) / 2;
	if (check(middle)) {
		return solution(middle, right);
	}
	else {
		return solution(left, middle - 1);
	}
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> N >> M;
	for (int i = 0; i < N; i++) {
		int houseNum;
		cin >> houseNum;
		houseArr.push_back(houseNum);
	}
	
	cout << solution(1, houseArr[N - 1]) << "\n";
}