#include <iostream>

using namespace std;

//promising�� ���� 
int N;
int ans = 0;
int main() {
	// ������ ��Ȯ�ϰ� Nų�α׷��� ����ؾ��Ѵ�.
	//�������� 3,5�� �ִ�.
	cin >> N;
	while (N>0) {


		//N�� ���
		//(1) 5�� ���
		//(2) 3�� ���
		//5,3�� ����� �ƴѼ�
		//3-1 5���� ū ��
		//3-2 ����
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
		else {//3-1���� 5�� �� ���� ������ �Ǹ�.
			ans = -1;
			break;
		}
			
		}
	cout << ans;

	return 0;
}