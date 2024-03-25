const form = document.getElementById("form");

//제출 후
form.addEventListener("submit",function(event){
    event.preventDefault(); //기존기능 차단
    
    let userId = event.target.id.value;
    let userPW1 = event.target.pw.value;
    let userPW2 = event.target.pw2.value;
    let userName = event.target.name.value;
    let userPhone = event.target.phone.value;
    let userPosition = event.target.position.value;
    let userGender = event.target.gender.value;
    let userEmail = event.target.email.value;
    let userIntro = event.target.intro.value;

    console.log(userId,userPW1,userPW2,userName,userPhone,userPosition,userGender,userEmail,userIntro);
    
    //아이디 길이
    if(userId.length < 6){
        alert("아이디를 6글자 이상 입력해주세요")
        return;
    }
    //비밀번호 확인
    if(userPW1 !== userPW2){
        alert("비밀번호가 일치하지 않습니다.")
        return;
    }

    //가입 완료 (환영)
    document.body.innerHTML = "";
    const h2 = document.createElement("h2");
    h2.textContent = `${userId}님 환영합니다.`;
    
    const p = document.createElement("p");
    p.textContent = "회원가입 시 입력하신 정보는 다음과 같습니다."

    function notice(str1, str2){
        const noticeP= document.createElement("p");
        noticeP.textContent = `${str1} : ${str2}`;

        return noticeP;
    }
    //string
    // const noticeId = document.createElement("p").textContent = `아이디 : ${userId}`;
    // const noticeName = document.createElement("p").textContent = `이 름 : ${userName}`;
    // const noticePhone = document.createElement("p").textContent = `전화번호 : ${userPhone}`;
    // const noticePosition = document.createElement("p").textContent = `직 무 : ${userPosition}`;

    document.body.appendChild(h2);
    document.body.appendChild(p);
    document.body.appendChild(notice("아이디", userId));
    document.body.appendChild(notice("이 름", userName));
    document.body.appendChild(notice("전화번호", userPhone));
    document.body.appendChild(notice("직 무", userPosition));
})

