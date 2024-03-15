function quickSort(arr) {
    if (arr.length <= 1) {
        return arr; // 배열의 크기가 1 이하면 이미 정렬된 상태입니다.
    }

    const pivot = arr[0]; // 첫 번째 요소를 피벗으로 선택합니다.
    const left = [];
    const right = [];

    for (let i = 1; i < arr.length; i++) { // n
        // logn
        if (arr[i] < pivot) {
            left.push(arr[i]); // 피벗보다 작은 요소는 왼쪽 배열에 추가합니다.
        } else {
            right.push(arr[i]); // 피벗보다 큰 요소는 오른쪽 배열에 추가합니다.
        }
    }

    // 왼쪽 배열과 오른쪽 배열을 재귀적으로 정렬하고 합쳐줍니다.
    return quickSort(left).concat(pivot, quickSort(right));
}

// 예제 배열을 생성하고 퀵 정렬을 적용합니다.
const exampleArray = [3, 1, 4, 1, 5, 9, 2, 6, 5];
const sortedArray = quickSort(exampleArray);

console.log("원본 배열:", exampleArray);
console.log("정렬된 배열:", sortedArray);
