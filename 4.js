const EhdlqfurgkwlaktpdyWW = 1;
if (typeof EhdlqfurgkwlaktpdyWW == "number") {
  let wasans = 1;
  if (Entry.FPS == 300) {
    wasans = 0;
  }
  Entry.engine.speeds[5] = 300; // undefind나 null등으로 적은 경우, 작품 상세 페이지에서 64fps로 동작하기 때문에 300으로 변경 (테스트 결과 250 이상은 '그 방법' 없이는 못 넘는 듯)
  document.getElementsByClassName("entrySpeedButtonWorkspace")[0].click();
  document
    .getElementsByClassName("entrySpeedButtonWorkspace")[0]
    .addEventListener("click", () => {
      if (
        document
          .getElementsByClassName("entrySpeedButtonWorkspace")[0]
          .classList.contains("on")
      ) {
        document.getElementById("progressCell5").style.backgroundColor =
          "blue";
        document
          .getElementById("progressCell5")
          .addEventListener("click", () => {
            document.getElementById("progressCell4").classList.remove("on");
            document.getElementById("progressCell3").classList.remove("on");
            document.getElementById("progressCell2").classList.remove("on");
            document.getElementById("progressCell1").classList.remove("on");
            document.getElementById("progressCell5").classList.add("on");
            wasans = 0;
          });
        document
          .getElementById("progressCell4")
          .addEventListener("click", () => {
            wasans = 1;
          });
        document
          .getElementById("progressCell3")
          .addEventListener("click", () => {
            wasans = 1;
          });
        document
          .getElementById("progressCell2")
          .addEventListener("click", () => {
            wasans = 1;
          });
        document
          .getElementById("progressCell1")
          .addEventListener("click", () => {
            wasans = 1;
          });
        if (wasans == 0) {
          document.getElementById("progressCell5").click();
        }
      }
    });
  document.getElementsByClassName("entrySpeedButtonWorkspace")[0].click();
}
// 코드 야매로 구현함ㅋ
