//#include <iostream>
//#include <algorithm>
//using namespace std;
//
//int map[101][101]={0,};
//
//void floyd(int n) {
//	int i, j, k;
//	for (k = 1; k <= n; k++) {
//		for (i = 0; i <= n; i++) {
//			for (j = 1; j <= n; j++)
//				map[i][j] = min(map[i][j], map[i][k] + map[k][j]);
//		}
//	}
//}
//
//
//int main() {
//	//n개의 도시가 있다 그리고 한 도시에서 출발하여 다른 도시에 도착하는 버스
//	//각 버스는 한번 사용할때 필요한 비용이 있따. 
//	//모든 도시의 쌍에 대해서 도시 A에서 B로 가는데 필요한 비용의 최솟값
//	//첫째 줄에 도시의 개수가 주어짐 , 버스의 개수가 주어짐
//	int n = 0;
//	int m = 0;
//	int from = 0;
//		int  to = 0;
//		int cost = 0;
//	cin >> n;
//	cin >> m;
//	//버스의 정보가 주어진다.
//	//버스의 정보는 버스의 시작도시, 도착도시, 한번 타는데 필요한 비용 
//	for (int i = 0; i < m; i++) {
//
//		cin >> from >> to >> cost;

//			map[from][to] = min(map[from][to], cost);
//
//	}
//	floyd(n);
//	for (int i = 1; i <= n; i++)
//
//	{
//
//		for (int j = 1; j <= n; j++)
//
//			cout << map[i][j] << " ";
//
//		cout << "\n";
//
//	}
//
//
//	return 0;
//}

#include <iostream>
#include <algorithm>
using namespace std;

#define INF 987654321
#define ARR_SIZE 100 + 1 
int vertex, edge;
int arr[ARR_SIZE][ARR_SIZE];
int from, to, weight;

void floyd_warshall() {
    for (int i = 1; i <= vertex; i++)             // i vertex를 거치는 경우
        for (int j = 1; j <= vertex; j++)         // from vertex
            for (int k = 1; k <= vertex; k++)     // to vertex
                if (arr[j][i] != INF && arr[i][k] != INF)
                    arr[j][k] = min(arr[j][k], arr[j][i] + arr[i][k]);
}

int main() {
    cin >> vertex >> edge;
    for (int i = 1; i <= vertex; i++) {        // vectex table 초기화
        for (int j = 1; j <= vertex; j++) {
            arr[i][j] = INF;
        }
    }
    for (int i = 0; i < edge; i++) {    // from vertex에서 to vertex 입력, 가중치 입력
        cin >> from >> to >> weight;
        if (arr[from][to] > weight)
            arr[from][to] = weight;
    }
    floyd_warshall();
    for (int i = 1; i <= vertex; i++) {
        for (int j = 1; j <= vertex; j++) {
            if (i == j || arr[i][j] == INF)
                cout << 0 << " ";
            else
                cout << arr[i][j] << " ";
        }
        cout << endl;
    }
    return 0;
}
