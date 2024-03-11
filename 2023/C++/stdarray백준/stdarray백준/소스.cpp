#include <iostream>
#include <array>
#include <algorithm>
using namespace std;

bool compare(string a, string b) {

}


int main() {

	int n;
	cin >> n;
	array<int, n> arr1;
	int* arr = new int[n];
	for (int i = 0; i < n; i++) {
		cin >> arr[i];
	}
	//??? ?? ???.

	sort(arr.front(), arr.back(), compare);


}