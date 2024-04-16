function solution(want, number, discount) {
    var answer = 0;
    // 내가 원하는 제품과 수량이 할인하는 날짜와 10일 연속으로 일치할 경우에만    
    
    // (1) 10개의 상품만 확인할 수 있다. 근데, 원하는게 10개이고 모두 할인 받을 수 있는 날
    
    dLen = discount.length // 20
    
    for (var i = 0; i < dLen - 9; i++) { // 시작하는 날짜.
        let newN = JSON.parse(JSON.stringify(number));
        dList = discount.slice(i, i+10)
        // console.log(dList, "d", dList.length)
        for (var j = 0; j < 10; j++){
            for (var k = 0; k < want.length; k++) {
                
                // if (dList.filter(item => item == want[k]).length == number[k])
                if (dList[j] == want[k]) {
                    newN[k] -= 1
                }
            }
        }
        
        // 이중 for문을 filter로 바꿀 수 있다~>
        // if (dList.filter(item => item == want[k]).length == number[k])
        
        // console.log(newN, "new")
        let testN = newN.filter(a => a == 0)
        if (testN.length == want.length) {
            answer += 1
        }

    }
        
        
        // 10개를 담을 수 있는 시작날의 경우의 수.
        // let tempWant = want
//         let tempNumber = number
//         for (var start = i; start < i + 10; start++) {
//         // 시작일부터 10개만 체크한다.
//             for (var check = 0; check < want.length; check++) {
//                 // 해당 원소의 값이 원하는 것과 일치한 지 확인
//                 if (want[check] == discount[start]) {
//                     console.log(")))")
//                     if (tempNumber[check] > 0) {
//                         tempNumber[check] -= 1
//                     }
//                     else {
//                         break
//                     }
//                 }
//             }
//             console.log(tempNumber.length, tempNumber, "temp")
            
//         }
        
        
        
//     }
    
    return answer;
}