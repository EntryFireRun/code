wawasans = prompt("게시글 아이디를 입력해주세요 ( 예 : 6610125ebf238166bdb91dc0 )")
wawawawawasans = ["* 유저가 좋아요를 취소하고 다시 누른 경우 마지막에 누른 값만 출력됩니다, 당연한걸 왜 말하냐고요? 그것때문에 이 코드를 만들게 되었으니까요ㅠ"]
function wasans(a) {
    a.filter((obj) => {
    wawawasans = new Date(parseInt(obj['id'].slice(0, 8), 16)*1000)
    wawawawasans = `${wawawasans.getFullYear()}년 ${wawawasans.getMonth()+1}월 ${wawawasans.getDate()}일 ${["일", "월", "화", "수", "목", "금", "토"][wawawasans.getDay()]}요일 ${wawawasans.getHours()}시 ${wawawasans.getMinutes()}분 ${wawawasans.getSeconds()}초`
    wawawawawasans.push(`${obj['id'].slice(0,8).toString()} ${wawawawasans.toString()}에 ${obj['user'].nickname.toString()}(${obj['user'].username.toString()})님이 좋아요를 눌렀습니다`);
    });
    wawawawawasans.sort()
    while (wawawawawasans.length != 0) {
        console.log(wawawawawasans[0])
        wawawawawasans.shift()
    }
}

fetch("https://playentry.org/graphql/LIKE_LIST", {headers: {"content-type": "application/json","csrf-token": `${JSON.parse(document.getElementById("__NEXT_DATA__").innerText).props.initialProps.csrfToken}`,"x-client-type": "Client","x-token": `${JSON.parse(document.getElementById("__NEXT_DATA__").innerText).props.initialState.common.user.xToken}`,},referrerPolicy: "unsafe-url",body: `{"query":" query LIKE_LIST($target: String, $groupId: ID){likeList(target:$target,groupId:$groupId){total list{id user{ nickname username}}}}","variables":{"target":"${wawasans}"}}`,method: "POST",mode: "cors",credentials: "include",}).then((response) => response.json()).then((data) => wasans(data.data.likeList.list)); // 코드 정리 쩔죠?ㅋ
