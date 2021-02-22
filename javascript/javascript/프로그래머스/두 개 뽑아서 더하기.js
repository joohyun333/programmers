function solution(numbers) {
    const answer = new Set();
    for(var i =0 ; i<numbers.length; i++){
        for(var j=0; j<numbers.length; j++){
            if (i != j){
                answer.add(numbers[i]+numbers[j]);
            }
        }
    }
    return Array.from(answer).sort(function (a,b) {
        return a-b;
    });
}
n = [5,0,2,7]
console.log(solution(n))