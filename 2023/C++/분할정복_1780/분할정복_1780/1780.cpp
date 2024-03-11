#include <iostream>
#include <vector>
using namespace std;

int result[3] = { 0, };
int map[2200][2200];


bool check(int row, int col, int num) {
	// 시작점
	int start = map[row][col];
	for (int i = row; i < row + num; i++) {
		for (int j = col; j < col + num; j++) {
			if (start != map[i][j])
				return false;
		}
	}
	return true;
}





int divide(int row, int col, int N) {
	//(1) 같은지 확인
	//(2) 아니라면 나누기 9개로 나눠야하니까 나누기 3을 해서 재귀함수. 
	//9개가 나오는데 그걸 어떠케 하쥐 이중for문으로ㅋㅋㅋ
	
	if (check(row, col,N)) {
		result[map[row][col] + 1]++;
	}
	else {
		int size = N/ 3;
		for (int i = 0; i < 3; i++) {
			for (int j = 0; j < 3; j++) {
				divide(row +size* i, col+size * j, size);
			}
		}
	}


	return 0;
}

int main() {
	int n = 0;
	cin >> n;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cin >> map[i][j];//2차원 배열로 받기 
		}
	}
	divide(0,0,n);//2차원 배열이 매개변수인게 좀 불편하다. 
	//행, 렬, 종이의 개수를 보낸다
	printf("%d\n%d\n%d", result[0], result[1], result[2]);
	return 0;
}