#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;
int main(void) {
	//도로 정비 계획은 각 도시를 잇는 도로들. 
	//한 도로가 정비될 때 마다 각 도시 별로 수도를 방문하는
	//최단 경로 구하기

	int n = 0;
	int m = 0;
	cin >> n >> m;//도시의 개수 (노드의 개수) 도로의 개수(edge의 개수)
	vector <vector<int>> street;
	for (int i = 0; i < m; i++) {
		cin >> street[i][0] >> street[i][1];

	}







}
