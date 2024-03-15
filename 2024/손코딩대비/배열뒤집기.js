var arr = [1, 2, 3, 4, 5];
var temp = arr.reverse()
console.log(temp)

// 문자열 뒤집기
// 문자열의 길이는 ==? str.length !!!!!!!!
var str = "hello";
var str2 = "";
for (var i = str.length - 1; i >=0; i--) {
    str2 += str[i]
    
}
console.log(str2)


// 중복된 문자열 제거
str = "people"
var str3 = ""
for (var i = 0; i < str.length; i++) {
    if (i != str.length) {
        if (str[i] == str[i+1]) {
            continue
        }
    }
    str3 += str[i]
}
console.log(new Set(str3))

// 중복된 문자 제거
const dupArr = [1, 2, 3, 1, 2, 4]
const result = dupArr.filter((d, i) => dupArr.indexOf(d) == i)
console.log(result)
// 중복된 문자 제거 2
const result2 = []
dupArr.forEach(d => {
    if (!result2.includes(d)) {
        result2.push(d)
    }
})
console.log(result2)



// 정리 : str의 길이는?
// arr의 함수들 filter, indexOf, reverse, forEach, includes
// arr 함수 넣을 때의 함수는?


// 구구단
