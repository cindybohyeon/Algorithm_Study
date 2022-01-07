#include <iostream>
#include <algorithm>
#include <map>

using namespace std;
//int map[300000];
int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	//이진탐색트리는 모든 노드가 많아야 2개의 자식 노드를 가지고 있는 트리

	//수열의 크기 N이 주어진다
	//N개의 줄에는 수열의 수가 차례대로 주어진다
	//N개의 줄에 각 수가 트리에 삽입된 후에 카운터 C 값을 한줄에 하나씩 출력한다.
	int n = 0;
	cin >> n;
	long long C = 0;
	map <int, int> depth;
	for (int i = 0; i < n; i++) {
		int num;
		cin >> num;
		if (i == 0) {
			depth[num] = 1;//root
			cout << C << endl;
			continue;
		}

		auto iterator = depth.upper_bound(num);
		//upper_bound 함수의 경우 컨테이너의 오른쪽 원소 중 기준 원소보다 큰 값 중 가장 왼쪽에 있는 원소를 리턴
		int height = 0;
		//제일 큰 숫자가 아닌 경우
		if (iterator != depth.end()) {
			height = iterator->second;
		}
		if (iterator != depth.begin()) {
			iterator--;
			height = max(height, iterator->second);
		}
		C += height;
		cout << C << endl;
		depth[num] = height + 1;
	}

	return 0;
}