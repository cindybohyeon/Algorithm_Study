function insertionSort(arr) {
    const length = arr.length;
    
    for (let i = 1; i < length; i++) {
        let current = arr[i]; // 현재 삽입할 원소
        let j = i - 1; // 정렬된 부분의 마지막 인덱스

        // 현재 원소를 정렬된 부분에 삽입할 위치를 찾습니다.
        while (j >= 0 && arr[j] > current) {
            arr[j + 1] = arr[j]; // 현재 원소보다 큰 원소는 한 칸씩 뒤로 이동합니다.
            j--; // 비교할 대상을 왼쪽으로 이동시킨다.
        }

        arr[j + 1] = current; // 정렬된 부분에 삽입합니다.
        console.log(arr)
    }

    return arr;
}

// 예제 배열을 생성하고 삽입 정렬을 적용합니다.
const exampleArray = [5, 2, 4, 6, 1, 3];
const sortedArray = insertionSort(exampleArray);

console.log("원본 배열:", exampleArray);
console.log("정렬된 배열:", sortedArray);
