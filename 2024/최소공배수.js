function gcd(a, b) {
    if (b == 0) {
        return a;
    } else {
        return gcd(b, a % b);
    }
}

var ans = gcd(270, 192);
console.log((270 * 192) /ans);

// // 주어진 두개의 수의 최소 공배수 구하기
// function gcd(a, b) {
//     console.log(a, b, "#")
//     if (b == 0) {
//         return a;
//     }
//     // if ( a < 0 || b < 0) {
//     //     return
//     // }
//     // if (a == b) {
//     //     return a
//     // }
//     // let big = Math.max(a, b)
//     // let small = Math.min(a, b)
//     // result = big % small
//     // if (result == 0) {
//     //     return small
//     // }
//     else {
//         gcd(b, a % b);
//     }
// }
// var ans = gcd(270, 192)
// console.log (gcd(270, 192))
// console.log(ans)

