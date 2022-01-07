#include <iostream>

using namespace std;
int map[16][16] = { 0, };
	int n = 0;
//1~n 까지 번호가 매겨져 있는 도시들이있고, 도시들 사이에는 길이 있다.
//한 회판원이 어느 한도시에서 출발해 N개의 도시를 모두 거쳐
void travel() {
	int i = 0;
	int j = 0;
	int k = 0;
	int D[n][n];

	for (i = 2; i < n; i++)
		D[i][0] = map[i][1];

	for(k=1;k<=n-2;k++)
		for()



}



int main() {


	cin >> n;
	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++)
			cin >> map[i][j];

	return 0;
}