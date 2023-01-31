function getNotificationPermission() {

    if (!("Notification" in window)) {

        while(1){

            alert("ㅋㅋㄹㅃㅃ");

        }

    }

    Notification.requestPermission(function (result) {

        if(result == 'denied') {

            alert('알림을 허용해주세요');

            getNotificationPermission()

            return false;

        }

    });

}

new Notification("아아", {body:'아아아아아아아아아아아아아아아아아아아아아앙아아아아아'});
