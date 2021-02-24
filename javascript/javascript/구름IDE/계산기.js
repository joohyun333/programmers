function solution(line) {
    var a = line.split(" ")
    if (a[1] == "/"){
        return (a[0]/a[2]).toFixed(2)
    }
    else return eval(line)
}
var num = "10 / 5"
console.log(solution(num))