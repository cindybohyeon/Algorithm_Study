#include <iostream>
using namespace std;
int n, k;
int w[100001] = { 0, };
int v[1001] = { 0, };
int dp[101][100001] = { 0, };


int main() {

	//��ǰ�� �� N�� �ؼ��� ��ƿ���ִ� ���� K�־�����
	//�ι�° �ٺ���, N���� �ٿ� ���� �� ������ ���� W�� �ش� ������ ��ġV�� �־�����

	cin >> n >> k;

	for (int i = 1; i <= n; i++)
		cin >> w[i] >> v[i];

	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= k; j++) {
			//dp[i][j] : i��° ���Ǳ��� �ִ� j���Ա��� ������ �� �ְ��� ��ġ��
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

