wawasans = prompt("유저 아이디를 입력해주세요 ( 예 : 64b27bd05ebb6c00251dc5f5 )") // 코드 그냥 입력하시면 됩니다, 유저 아이디 입력 저 부분 수정 안하셔도 되고요, 이 글자도 지우실 필요 없습니다
wawawasans = new Date(parseInt(wawasans.slice(0, 8), 16)*1000).toString().split(" ")[0].replace("Mon", "월요일").replace("Tue", "화요일").replace("Wed", "수요일").replace("Thu", "목요일").replace("Fri", "금요일").replace("Sat", "토요일").replace("Sun", "일요일");
function wasans(a) {
    alert(`${a.split("-")[0]}년 ${a.split("-")[1]}월 ${a.split("-")[2].split("T")[0]}일 ${wawawasans} ${parseInt(a.split("T")[1].split(":")[0])+9}시 ${a.split(":")[1]}분 ${a.split(":")[2].slice(0, -1)}초에 생성된 계정입니다 `)
}

fetch("https://playentry.org/graphql/FIND_USERSTATUS_BY_USERNAME", {
      headers: {
      "content-type": "application/json",
      "csrf-token": `${
        JSON.parse(document.getElementById("__NEXT_DATA__").innerText).props
          .initialProps.csrfToken
      }`,
      "x-client-type": "Client",
      "x-token": `${
        JSON.parse(document.getElementById("__NEXT_DATA__").innerText).props
          .initialState.common.user.xToken
      }`,
    },
  referrerPolicy: "unsafe-url",
  body: `{"query":"query FIND_USERSTATUS_BY_USERNAME($id: String){userstatus(id: $id){created}}","variables":{"id":"${wawasans}"}}`,
  method: "POST",
  mode: "cors",
  credentials: "include",
}).then((response) => response.json()).then((data) => wasans(data.data.userstatus.created));
