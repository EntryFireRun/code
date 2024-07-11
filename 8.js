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
  body: `{"query":" query SELECT_FOLLOWERS( $user: String ){ followers(user: $user) { list { user { id } } } }","variables":{"user":"${prompt('팔로우를 삭제할 유저의 마이페이지 주소 입력 [최대 10명]').split('/profile/')[1].split('?')[0]}","pageParam":{"display":10}}}`,
  method: "POST",
  mode: "cors",
  credentials: "include",
})
  .then((response) => response.json())
  .then((data) => {
      console.log(data.data.followers.list.length)
    for (let i = 0; i < data.data.followers.list.length; i++) {
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
        body: `{"query":" mutation REMOVE_FOLLOW($id: ID!) { removeFollow(id: $id) { result } } ","variables":{"id":"${data.data.followers.list[i].user.id}"}}`,
        method: "POST",
        mode: "cors",
        credentials: "include",
      });
    }
  });
