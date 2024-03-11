#include <iostream>
#define MAX 15
using namespace std;
int N;
int map[MAX];
int ans = 0;
bool promising(int i) {//i번째 퀸과 1~i-1번째 퀸과 비교한다
	int k = 1;//i번째 퀸을 배치하기 전의 퀸 
	bool check = true;

	while (k<i && check)
	{
		if (map[i] == map[k] || abs(map[i] - map[k]) == i - k)
			check = false; 
		//이전의 k퀸과 현재 i퀸이 조건에 맞지 않는 경우, while(check)조건으로바로빠져나간다.
	
		k++;
	}
	return check;
}



int queens(int i) {//queens(i)  :  i번째 퀸을 배치했다 
	int j = 0;

	if (promising(i)) {
		if (i == N)//이제 N행까지 다 배치한 상황
			ans++;
		else {
			for (j = 1; j <= N; j++) {
				map[i + 1] = j;//i+1 행에서 1~N 중 하나에 배치를 한다.
				queens(i + 1);//그다음 행을 배치한다
			}
		}
	}


	return 0;
}

int main() {
	cin >> N;
	queens(0);
	cout << ans;
	return 0;
}
//#include <iostream>
//#define MAX 15
//using namespace std;
//
//int col[MAX];
//int N, total = 0;
//
//bool check(int level)
//{
//    for (int i = 0; i < level; i++)
//        if (col[i] == col[level] || abs(col[level] - col[i]) == level - i)// 대각선이거나 같은 라인
//            return false;
//    //col[i]가 의미하는 것이 X좌표, i가 의미하는것이 Y좌표이므로 차이가 일정하다면 대각선에 있다고 볼 수 있다.
//    return true;
//}
//
//void nqueen(int x)
//{
//    if (x == N)
//        total++;
//    else
//    {
//        for (int i = 0; i < N; i++)
//        {
//            col[x] = i; // 해당 위치에 퀸을 배치
//            if (check(x)) // 유효하다면 다음행의 퀸 배치, 유효하지않다면 다른 위치로 퀸 배치 변경
//                nqueen(x + 1);
//        }
//    }
//}
//int main() {
//    cin >> N;
//    nqueen(0);
//    cout << total;
//}