#include <iostream>
#include <stack>
#include <vector>
#include <string>
using namespace std;

int main(void) {
	int n = 0;
	string input;
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> input;
		stack <char> s;

		int size = input.size();
		for(int k =0;k<size;k++){
			if (input[k] == '(') {
				s.push('(');
			}
			else {
				if (!s.empty()) {//비어있지 않으면 (가 존재한다는 뜻
					s.pop();
				}
				else {
					break;
				}
			}
		}
		if (s.empty()) cout << "YES" << endl;
		else cout << "NO" <<endl;
	}

	return 0;
}