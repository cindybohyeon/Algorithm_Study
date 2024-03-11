#include <iostream>

using namespace std;

//promising의 조건 
int N;
int ans = 0;
int main() {
	// 설탕을 정확하게 N킬로그램을 배달해야한다.
	//봉지에는 3,5가 있다.
	cin >> N;
	while (N>0) {


		//N의 경우
		//(1) 5의 배수
		//(2) 3의 배수
		//5,3의 배수가 아닌수
		//3-1 5보다 큰 수
		//3-2 음수
		if (N % 5 == 0) {
			ans++;
			N -= 5;
		}
		else if (N % 3 == 0) {
			ans++;
			N -= 3;
		}
		else if (N > 5) {
			ans++;
			N -= 5;
		}
		else {//3-1에서 5를 뺀 값이 음수가 되면.
			ans = -1;
			break;
		}
			
		}
	cout << ans;

	return 0;
}