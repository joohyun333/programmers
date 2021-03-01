fetch('https://reqres.in/api/users',{
    method: 'POST', //요청 방법 선택
    headers: {
        'Content-Type': 'application/json' //요청헤더 타입 변경
    },
    body: JSON.stringify({ //요청바디 json화
        name: 'User 1'
    })
}).then(res => {
    if(res.status == '404'){ //상태코드가 404인 경우
        console.log("Err");
    }
    else
        return res.json() //응답받은 json 데이터 토큰화
})
    .then(data => console.log(data))