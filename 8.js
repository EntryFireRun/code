fetch("https://playentry.org/graphql", {
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
  body: `{"query":" query SELECT_FOLLOWERS( $user: String ){ followers(user: $user) { list { id } } }","variables":{"user":"${prompt('팔로우를 삭제할 유저의 마이페이지 주소 입력\n[최대 8명 그 이상으로 요청을 보내는 경우 429 error를 반환 함]').split('/profile/')[1].split('?')[0]}","pageParam":{"display":10}}}`,
  method: "POST",
  mode: "cors",
  credentials: "include",
})
  .then((response) => response.json())
  .then((data) => {
      console.log(data.data.followers.list.length)
    for (let i = 0; i < (data.data.followers.list.length > 8 ? 8 : data.data.followers.list.length); i++) {
document.querySelector('[type=mypage] > li:nth-child(4) > div > div > em').innerText -= 1
      fetch("https://playentry.org/graphql", {
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
        body: `{"query":" mutation REMOVE_FOLLOW($id: ID!) { removeFollow(id: $id) { status } } ","variables":{"id":"${data.data.followers.list[i].id}"}}`,
        method: "POST",
        mode: "cors",
        credentials: "include",
      });
    }
  });
