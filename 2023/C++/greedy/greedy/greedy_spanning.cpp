#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
//int W[10000][10000] = { 0, };
//int Edge[10000] = { 0, };
	int V = 0;
	int E = 0;

	//int from = 0;
	//int to = 0;
	long long ans = 0;
	
//int prim(void) {
//	int nearest[10000] = {0,};
//	int distance[10000] = {0,};
//	int vnear = 0;
//	for (int i = 2; i <= V; i++) {
//		nearest[i] = 1;//i와 가장 가까운 Y 원소들
//		distance[i] = W[1][i];
//	}
//	int k = 1;
//	while (k != V-1) {
//		int min = 100000000000;
//		for (int i=2;i<=V;i++)//distance[i]들 중 제일 작은 값을 min에 저장한다.
//			//그때의 Y밖의 vertex = vnear
//		{
//			if (0 <= distance[i] || distance[i] < min) {
//				min = distance[i];
//				vnear = i;
//			}
//		}
//			ans+= W[vnear][nearest[vnear]];
//			distance[vnear] = -1;
//		
//		for (int j = 2; j <= V; j++) {
//			if (W[j][vnear] < distance[j]) {
//				distance[j] = W[j][vnear];
//				nearest[j] = vnear;
//			}
//		}
//		k++;
//	}
//
//
//	return 0;
//}

int parent[10001];

struct edge {
	int u, v, w;
	edge(int u, int v, int w) {
		this->u = u;
		this->v = v;
		this->w = w;
	}
};

//initial : n개의 부분집합을 초기화하고 하나의 원소들이 들어가잇도록 한다.
//find(i) : point 만들기 
int find(int u) {
	if (u == parent[u])
		return u;
	return parent[u] = find(parent[u]);
}

void merge(int u, int v) {
	u = find(u);
	v = find(v);

	parent[v] = u;
}
int compare_comp(const edge& a, const edge& b) {
	return a.w < b.w;//edge값은 세번째 인자이니까.
}
int main() {
	cin >> V >>  E;
	vector<edge> v;

	for (int i = 1; i <= V; i++) {
		parent[i] = i;
	}//(1) vertex들의 모임, Initial(). 하나의 set에 하나의 원소들어간다.
	int A, B, C;
	for (int i = 0; i < E; i++) {
		cin >> A >> B >> C;
		v.push_back(edge(A, B, C));
	}

	sort(v.begin(), v.end(), compare_comp);//(2) edge 오름차순 정렬

	for (auto vertex : v) {
		if (find(vertex.v) != find(vertex.u)) {//(3) 같은 set에 있는지 확인한다.
			merge(vertex.u, vertex.v);//(4) 다른 set인 경우 merge
			ans += vertex.w;//
		}
	}
	cout << ans;
	return 0;
	//for (int i = 0; i < E; i++) {
	//	cin >> from;
	//	cin >> to;
	//	cin >> W[from][to];
	//	W[to][from] = W[from][to];
	//}

	//prim();
	////prim : E들의 가중치의 순서?
	//// kruskal : 

}