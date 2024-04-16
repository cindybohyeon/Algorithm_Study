function solution(elements) {
    var answer = 0;
    // 어떤 자연수로 이루어진 원형 수열의 연속하는 부분 수열의 합으로 만들 수 있는 수.
    // 7 9 1 1 4
    // 1개 고르는 경우 5가지 (길이값)
    // 2개 고르는 경우 시작을 5개의 위치에서 한다.?
    // 조합에서 1개를 고르는 경우 ~ 5개를 고르는 경우.
    allSum = []
    for (var select = 0; select < elements.length; select++) {
        // 해당 케이스에서 연속 수열 개수는 5개라고 생각함.
        for (var start = 0; start < elements.length; start++) {
            end = start + select + 1
            let tempList = []
            let tempSum = 0
            if (end > elements.length) {
                addIndex = end - elements.length
                preList = elements.slice(start)
                pList = elements.slice(0, addIndex)
                tempSum = preList.reduce((a, c) => a + c, 0) + 
                    pList.reduce((a, c) => a + c, 0)
                // console.log(addIndex, "##", preList, pList)
                
            }
            else {
                tempList = elements.slice(start, start+select+1)  
                tempSum = tempList.reduce((a, c) => a + c, 0)
            } 
            
            // console.log(tempSum)
            allSum.push(tempSum)
        }
        
    }
    allSum.sort()
    // console.log(allSum)
    answer = allSum.length
    for (var i = 0; i < allSum.length - 1; i++) {
        if (allSum[i] == allSum[i+1]) {
            answer -= 1
        }
    }
    
    return answer;
}