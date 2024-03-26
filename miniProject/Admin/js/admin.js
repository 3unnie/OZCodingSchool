//크롤링 임시 데이터
const data = [
    { 
        check: "0", 
        category: "간식",
        brand: "PETHROOM",
        count: "11",
        product: "프리미엄 한방 보약 짜먹는 츄르 스틱 간식 퓨레",
        price: "19,000",
        score: "4.8"
    },
    { 
        check: "0", 
        category: "배변용품",
        brand: "모찌네",
        count: "7",
        product: "모찌네모래24L 고양이모래(무향)",
        price: "18,900",
        score: "2.8"
    },
    { 
        check: "0", 
        category: "사료",
        brand: "로얄캐닌",
        count: "42",
        product: "로얄캐닌 캣파우치 키튼 그레이비 1박스(12개)",
        price: "15,500",
        score: "4.9"
    },
    { 
        check: "0", 
        category: "사료",
        brand: "하림펫푸드",
        count: "21",
        product: "밥이보약 고양이 건강고민 맞춤 사료 3.4kg",
        price: "39,200",
        score: "4.9"
    },
    { 
        check: "0", 
        category: "사료",
        brand: "나투어리베",
        count: "18",
        product: "레오나르도 캣 고양이사료 샘플 500g",
        price: "2,000",
        score: "4.8"
    },
    { 
        check: "0", 
        category: "캣타워",
        brand: "그린웨일",
        count: "2",
        product: "클래식 5단 원목 고양이 캣폴",
        price: "119,000",
        score: "4.9"
    },
    { 
        check: "0", 
        category: "장난감",
        brand: "PETHROOM",
        count: "5",
        product: "티저 토이 고양이 낚시대 장난감",
        price: "17,800",
        score: "5.0"
    }
]

const dataTable = document.getElementById("data-table");
      
data.forEach((item) => {
    const row = dataTable.insertRow();
    row.insertCell(0).innerHTML=`<input type="checkbox" class="check" value="1">`; 
    row.insertCell(1).innerHTML = item.category;
    row.insertCell(2).innerHTML = item.brand;
    row.insertCell(3).innerHTML = item.count;
    row.insertCell(4).innerHTML = item.product;
    row.insertCell(5).innerHTML = item.price;
    row.insertCell(6).innerHTML = item.score;
});

//메뉴 클릭 이벤트
const newProduct = document.getElementById("newProduct");
const soldOut = document.getElementById("soldOut");
const tableBox = document.getElementById("tableBox");
const tableBox2 = document.getElementById("tableBox2");

newProduct.addEventListener("click",function(){
    tableBox2.style.display = "none";
    tableBox.style.display = "";
})

soldOut.addEventListener("click",function(){
    tableBox.style.display = "none";
    tableBox2.style.display = "";
})

//페이지 기능
const previous = document.getElementById("previous");
const next = document.getElementById("next");
const firNum = document.getElementById("firNum");
const secNum = document.getElementById("secNum");

let nowPageNum = parseInt(firNum.textContent);
let totalPageNum = parseInt(secNum.textContent);

//이전페이지 클릭 이벤트
previous.addEventListener("click",function(){
    if(nowPageNum > 1){
        nowPageNum -= 1;
        firNum.textContent = nowPageNum;
    };
});
//다음페이지 클릭 이벤트
next.addEventListener("click",function(){
    if(totalPageNum > nowPageNum){
        nowPageNum += 1;
        firNum.textContent = nowPageNum;
    };
});

//선택취소 기능
const resetBtn = document.getElementById("resetBtn");
const deleteBtn = document.getElementById("deleteBtn");
const checkBoxes = document.getElementsByClassName("check");

resetBtn.addEventListener("click",function(){
    //for문을 사용해보자
    for(let i=0;i < checkBoxes.length; i += 1){
        checkBoxes[i].checked = false;
    };
});

//삭제기능
deleteBtn.addEventListener("click",function(){
    
    const ask = confirm("삭제하시겠습니까?");

    if(ask){
        let deleteItems = [];
        for (let i = 0; i < checkBoxes.length; i += 1) {
            if (checkBoxes[i].checked) {
                deleteItems.push(checkBoxes[i]);
            };
        };
        deleteItems.forEach((item) => {
            item.parentElement.parentElement.remove()
        }); 
    }
});

