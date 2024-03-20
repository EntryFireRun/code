# 실행을 위해 다음을 설치해야 합니다
# FFmpeg, python os 모듈, python requests 모듈, python requests 모듈(스파게티 코드로 짜면서 나온건데, 이거 필요 없을 수도 있음), python BeautifulSoup 모듈,
# (추가로 모듈을 설치하기 위해 pip 필요), (해당 코드를 실행하기 위해 python 필요)
# 해당 코드는 윈도우에 맞춰져있습니다, 윈도우로 실행해주세요, 오류나거나, 만들어진 파일 안 지워지거나, 파일이 안합쳐질 수도 있습니다
# 아프리카 tv가 업데이트 되면 제대로 실행이 안될 수 있습니다, 업데이트로 문제가 생기면 계속 계산하지 않고, 코드를 끝내도록 설계되었으나, 그것도 오류가 날 수 있으니, 이상하다 싶으면 알아서 끄세요
# 중지는 Ctrl Z나 Ctrl C 로 가능할거예요
# 아 맞다, 이거 새 폴더에서 실행해주세요, 파일 이름 겹치면 파일을 잃거나 고장날 수 있습니다, 근데 위에 말하려고 했던 이야기는 아닌 것 같음
# 만든 이유는, yt-dlp로 아프리카tv VOD저장 고장나서 만들거예요
# 레포가 entrycode지만 엔트리와 관련 없고 그냥 올리는거
# 몇 몇 영상 다운 안되는데 귀찮아서 안 고칠 예정

import urllib.request
import os
import requests
from bs4 import BeautifulSoup

def save_video(video_url, a) :
    save_name = f"chunk-{a}.ts"
    urllib.request.urlretrieve(video_url, save_name)
    file = open('file.txt', "a")
    file.write(f"file 'chunk-{a}.ts'\n")
    file.close()
    print(f"저장됨 : {save_name} / chunk-{dsans}.ts")
isnumber = input("아프리카tv VOD 저장 프로그램입니다!\nVOD URL : ")
wtfbro = input("저장할 파일 명 (확장자는 자동으로 mp4가 적용됩니다): ")

file = open('file.txt', "w")
file.write("")
file.close()

response = requests.get(isnumber)
soup = BeautifulSoup(response.text, "html.parser")
div_tag = soup.find_all('meta')
asans = str(div_tag).split("videoimg")[1].split("og:image")[0].split("evod2_")[1].split("_")[0]
bsans = str(div_tag).split("videoimg")[1].split("og:image")[0].split("rowKey=")[1].split("_")[0]
csans = f"https://vod-archive-kr-cdn-z01.afreecatv.com/v101/hls/evod/{bsans}/{asans}/{bsans}_evod2_{asans}.smil/original/both/"
dsans = 100 # 처음부터 계산하면 너무 느리고, 404는 데이터 받는게 빠르게 때문에 효율적인 알고리즘 사용
esans = 0
while True:
    if requests.get(f"https://vod-archive-kr-cdn-z01.afreecatv.com/v101/hls/evod/{bsans}/{asans}/{bsans}_evod2_{asans}.smil/original/both/seg-{dsans}.ts").status_code == 200:
        if dsans >= 100:
            dsans += 10
            if esans == 1:
                break
        else:
            break
    else:
        dsans -= 1
        esans = 1
        print(f"영상 청크 검색 중... / 현재 검색된 개수 : {dsans}")
        if dsans == 0:
            print("오류 : 검색 인덱스 범위 초과\n님 이상한 url 적으셨죠;")
            quit()
removeList = []
if os.path.isfile(f"{wtfbro}.mp4"):
    os.remove(f"{wtfbro}.mp4")
for i in range(int(dsans) + 1):
    save_video(f"{csans}seg-{i}.ts", i)
    removeList.append(f"chunk-{i}.ts")

os.system(f"ffmpeg -f concat -i file.txt -c copy {wtfbro}.mp4")
os.remove("file.txt")
for i in removeList:
    os.remove(i)
os.system('cls')
print(f"\"{wtfbro}\"파일이 생성되었습니다, 제대로 생성되지 못한 경우, 다시 시도해주세요")
# https://vod.afreecatv.com/player/119563493 <== test URL
