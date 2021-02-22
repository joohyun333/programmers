function solution(line) {
    let result = new Set();
    for (i=1;i<parseInt(Math.sqrt(line)+1); i++){
        if (line%i==0){
            result.add(i);
            result.add(line/i);
        }
    }
    let answer = Array.from(result);
    return answer.reduce(function (a, b) {
        return a+b;
    })
}
var n = 20
console.log(solution(n))