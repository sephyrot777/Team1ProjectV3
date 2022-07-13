<!-- login -->
const muserid = document.querySelector('#muserid');
const mpasswd = document.querySelector('#mpasswd');
const loginbtn = document.querySelector('#loginbtn');
const logoutbtn = document.querySelector('#logoutbtn');


try {
    loginbtn.addEventListener('click', () => {
        if (muserid.value == '') {
            alert('아이디를 입력하세요!!');
            muserid.focus();
        } else if (mpasswd.value == '') {
            alert('비밀번호를 입력하세요!!');
            mpasswd.focus();
        } else {
            // document.loginfrm.action = '{% url 'login' %}';
            document.loginfrm.action = '/login/';
            document.loginfrm.submit();
        }
    });
} catch (e) {

}

try {
    logoutbtn.addEventListener('click', () => {
    location.href = '/logout/';
});
}catch (e){

}

<!-- search id -->
//ajax로 넘겨야 디자인이 안 깨짐!
const email=document.querySelector('#semail')
const suserid=document.querySelector('#suserid');
const searchbtn = document.querySelector('#searchbtn');
const wmsg= document.querySelector('#wmsg');

// try {searchbtn.addEventListener('click',()=>{
//     let qry = '?email=' +email.value;
//     location.href='/searchid/' + qry
// });}
// catch (e) {
//
// }

searchbtn.addEventListener('click', () => {
        let qry = '?email=' + email.value;
        fetch('/searchid/' + qry)
            .then(response => response.text())
            .then(text => searchID(text));
    });

const searchID = (emails)=>{
    console.log(emails);
    emails = JSON.parse(emails);  // 문자열을 JSON객체로 변환
    console.log(emails[0]);

    let fuserid = '';
    let msg=''

    emails.forEach((data, idx)=>{
        fuserid=data.fields.userid;
        suserid.value=fuserid;
    });
    if (suserid.value==0){
        msg='아이디가 존재하지 않습니다.'
    };
    wmsg.innerHTML=msg;
}

<!-- 닫기 버튼/이전페이지 버튼 누를 시 아이디 조회 input에 남아있는 값들 다 지움 -->
const cmdlbtn = document.querySelector('#cmdlbtn');
cmdlbtn.addEventListener('click', ()=>{
    email.value='';
    suserid.value='';
    wmsg.innerHTML='';
});

const backbtn = document.querySelector('#backbtn');
backbtn.addEventListener('click', ()=>{
    email.value='';
    suserid.value='';
    wmsg.innerHTML='';
});