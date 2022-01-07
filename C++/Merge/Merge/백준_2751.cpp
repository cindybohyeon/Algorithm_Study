#include <iostream>
#include <vector>
#include <array>
using namespace std;

int N = 0;

vector<int> arr;

//N개의 수가 주어졌을 떄, 오름차순으로 정렬하기
int merge(int left, int middle, int right, int* s) {
	int len = right - left + 1;
	int* sort_arr = (int*)malloc(sizeof(int) * len);
	int idx = 0;
	int i = left; int j = middle + 1;
	while (i <= middle && j <= right) {
		if (s[i] < s[j]) {
			sort_arr[idx] = s[i];
			i++;
		}
		else {
			sort_arr[idx] = s[j];
			j++;
		}
		idx++;
	}
	if (i > middle) {
		while (j <= right) {
			sort_arr[idx] = s[j];
			//printf("sorted[%d] is %d\n",seq,sorted[seq]); 
			j++; idx++;
		}
	}
	else {//(i>middle
		while (i <= middle) {
			sort_arr[idx] = s[i];
			//printf("sorted[%d] is %d\n",seq,sorted[seq]); 
			i++; idx++;
		}
	}

	idx = 0;
	for (int k = left; k < right + 1; k++) {
		s[k] = sort_arr[idx];
		idx++;
	}
	return 0;
}

int mergesort(int low, int high, int* s) {
	if (high > low) {
		int mid = (low + high) / 2;
		mergesort(low, mid, s);
		mergesort(mid+1, high, s);

		merge(low, mid, high, s);

	}
	return 0;
}
int main() {
	
	cin >> N;
	int* map = (int*)malloc(sizeof(int) * N);
	for (int i = 0; i < N; i++) {
		cin >> map[i];
	}
	mergesort(0, N-1, map);
	for (int i = 0; i < N; i++) {
		cout << map[i] << endl;
	}
	return 0;
}


