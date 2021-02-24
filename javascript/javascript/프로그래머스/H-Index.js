function solution(citations) {
    var m = citations.sort(function (a,b) {
        return b-a;
    })
    var i = 0
    while(i+1<=m[i]){
        i++;
    }
    return i
}
citations = [13, 10, 16, 11, 15]
console.log(solution(citations))