#include <iostream>
#define MAX 15
using namespace std;
int N;
int map[MAX];
int ans = 0;
bool promising(int i) {//i��° ���� 1~i-1��° ���� ���Ѵ�
	int k = 1;//i��° ���� ��ġ�ϱ� ���� �� 
	bool check = true;

	while (k<i && check)
	{
		if (map[i] == map[k] || abs(map[i] - map[k]) == i - k)
			check = false; 
		//������ k���� ���� i���� ���ǿ� ���� �ʴ� ���, while(check)�������ιٷκ���������.
	
		k++;
	}
	return check;
}



int queens(int i) {//queens(i)  :  i��° ���� ��ġ�ߴ� 
	int j = 0;

	if (promising(i)) {
		if (i == N)//���� N����� �� ��ġ�� ��Ȳ
			ans++;
		else {
			for (j = 1; j <= N; j++) {
				map[i + 1] = j;//i+1 �࿡�� 1~N �� �ϳ��� ��ġ�� �Ѵ�.
				queens(i + 1);//�״��� ���� ��ġ�Ѵ�
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
//        if (col[i] == col[level] || abs(col[level] - col[i]) == level - i)// �밢���̰ų� ���� ����
//            return false;
//    //col[i]�� �ǹ��ϴ� ���� X��ǥ, i�� �ǹ��ϴ°��� Y��ǥ�̹Ƿ� ���̰� �����ϴٸ� �밢���� �ִٰ� �� �� �ִ�.
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
//            col[x] = i; // �ش� ��ġ�� ���� ��ġ
//            if (check(x)) // ��ȿ�ϴٸ� �������� �� ��ġ, ��ȿ�����ʴٸ� �ٸ� ��ġ�� �� ��ġ ����
//                nqueen(x + 1);
//        }
//    }
//}
//int main() {
//    cin >> N;
//    nqueen(0);
//    cout << total;
//}