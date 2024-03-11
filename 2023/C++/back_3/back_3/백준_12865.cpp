#include <iostream>
using namespace std;
int n, k;
int w[100001] = { 0, };
int v[1001] = { 0, };
int dp[101][100001] = { 0, };


int main() {

	//물품의 수 N과 준서가 버틸수있는 무게 K주어진다
	//두번째 줄부터, N개의 줄에 거쳐 각 물건의 무게 W와 해당 물건의 가치V가 주어진다

	cin >> n >> k;

	for (int i = 1; i <= n; i++)
		cin >> w[i] >> v[i];

	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= k; j++) {
			//dp[i][j] : i번째 물건까지 최대 j무게까지 가능할 때 최고의 가치값
			if (w[i] <= j) {
				dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w[i]] + v[i]);
			}
			else {
				dp[i][j] = dp[i - 1][j];
			}
		}
	}
	cout << dp[n][k];

	return 0;
}

