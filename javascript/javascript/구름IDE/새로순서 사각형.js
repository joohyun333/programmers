function solution(line) {
    var n = parseInt(line)
    var arr1 = []
    for (var i=1; i<=n; i++){
        var arr2= []
        for (var j = i; j<=i+((n-1)*n); j+=n){
            arr2.push(j)
        }
        arr1.push(arr2.join(" "));
    }
    return arr1.join(" \n");
}
console.log(solution(11))