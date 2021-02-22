// Run by Node.js

const readline = require("readline");
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.on("line", function(line) {
    function isPrime(n) {
        if (n<=1){
            result = "False";
            return ;
        }
        let divisor = 2;
        while (n>divisor){
            if (n%divisor==0){
                result = "False";
                return;
            }
            divisor++;
        }
        return;
    }
    var result = "True"
    isPrime(line);
    console.log(result);
    rl.close();
}).on("close", function() {
    process.exit();
});