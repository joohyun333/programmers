function solution(s) {
    var b = s.split(" ")
    var m = []
    for (var i=0;i<b.length;i++){
        var result = []
        for (var j=0; j<b[i].length; j++){
            if (j == 0){
                result.push(b[i][j].toUpperCase());
            }
            else {
                result.push(b[i][j].toLowerCase())
            };
        }
        m.push(result.join(""))
    }
    return m.join(" ");
}
s = "3people unFollowed me"
// s = "for the last week"
console.log(solution(s))