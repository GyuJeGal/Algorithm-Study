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

	for (int i = 0; i < N; i++) { // houseArr[i]번에 사람을 넣을 수 있냐?
		if (house <= houseArr[i]) { // house값보다 뒤에 있거나 같은 집이면 houseArr[i]번에 사람 넣을 수 있다.
			residentcount++; // '사람 들어갔다'
			house = houseArr[i] + length; // house : 누적 길이로 기능
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