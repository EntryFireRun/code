# 실행을 위해 다음을 설치해야 합니다
# FFmpeg, python os 모듈, python requests 모듈, python requests 모듈(스파게티 코드로 짜면서 나온건데, 이거 필요 없을 수도 있음), python BeautifulSoup 모듈
# (추가로 모듈을 설치하기 위해 pip 필요), (해당 코드를 실행하기 위해 python 필요)
# 해당 코드는 윈도우에 맞춰져있습니다, 윈도우로 실행해주세요, 오류나거나, 만들어진 파일 안 지워지거나, 파일이 안합쳐질 수도 있습니다
# 아프리카 tv가 업데이트 되면 제대로 실행이 안될 수 있습니다, 업데이트로 문제가 생기면 계속 계산하지 않고, 코드를 끝내도록 설계되었으나, 그것도 오류가 날 수 있으니, 이상하다 싶으면 알아서 끄세요
# 중지는 Ctrl Z나 Ctrl C 로 가능합니다
# 새 폴더에서 실행해주세요, 파일 이름 겹치면 파일을 잃거나 고장날 수 있습니다
# 지원하는 VOD : 유저VOD, 업로드VOD, 유저 클립, 하일라이트, 캐치
# 다시보기는 용량 문제로 지원하지 않을 예정 (다운로드가 yt-dlp에 비해 훨씬 느리고 구린 알고리즘을 사용)

import urllib.request
import os
import requests
from bs4 import BeautifulSoup

def save_video(video_url, a) :
    global gsans
    try:
        save_name = f"chunk-{a}.ts"
        urllib.request.urlretrieve(video_url, save_name)
        file = open('chunk-l.txt', "a")
        file.write(f"file 'chunk-{a}.ts'\n")
        file.close()
        gsans += os.path.getsize(save_name)
        print(f"저장됨 : {save_name} / chunk-{dsans}.ts | 예상 용량 : {int(dsans*gsans/(1024*1024)/(a+1))}mb | 현재 용량 : {int(gsans/(1024*1024))}mb  ",end='\r')
    except:
        print("\n프로그램에 오류가 있어, 파일을 정리한 후 프로그램이 종료됩니다")
        os.remove("chunk-l.txt")
        for i in removeList:
            os.remove(i)
        quit()

isnumber = input("아프리카tv VOD 저장 프로그램입니다!\nVOD URL : ")
wtfbro = input("저장할 파일 명 (확장자는 자동으로 mp4가 적용됩니다, 파일이 이미 있는 경우 제거됩니다) : ")
file = open('chunk-l.txt', "w")
file.write("")
file.close()

response = requests.get(isnumber)
soup = BeautifulSoup(response.text, "html.parser")
div_tag = soup.find_all('meta')
try:
    asans = str(div_tag).split("videoimg")[1].split("og:image")[0].split("evod2_")[1].split("_")[0]
    bsans = str(div_tag).split("videoimg")[1].split("og:image")[0].split("rowKey=")[1].split("_")[0]
    csans = f"https://vod-archive-kr-cdn-z01.afreecatv.com/v101/hls/evod/{bsans}/{asans}/{bsans}_evod2_{asans}.smil/original/both/"
except:
    try:
        asans = str(div_tag).split("save/afreeca/station/")[1].split(".")[0].split("_")[0].split("/thumb/")[0]
        bsans = str(div_tag).split("save/afreeca/station/")[1].split("/thumb/")[1].split("_")[0]
        csans = f"https://vod-normal-kr-cdn-z01.afreecatv.com/v101/hls/save/afreeca/station/{asans}/{bsans}.smil/original/both/"
    except:
        try:
            asans = str(div_tag).split("videoimg")[1].split("og:image")[0].split("_")[0].split("=")[-1]
            bsans = str(div_tag).split("videoimg")[1].split("og:image")[0].split("_")[1].split("_")[0]
            if requests.get(f"https://vod-normal-kr-cdn-z01.afreecatv.com/v101/hls/review_clip/{asans}/{bsans}/{asans}_{bsans}_1.smil/original/both/seg-0.ts").status_code == 200:
                csans = f"https://vod-normal-kr-cdn-z01.afreecatv.com/v101/hls/review_clip/{asans}/{bsans}/{asans}_{bsans}_1.smil/original/both/"
            else:
                bsans = str(div_tag).split("videoimg")[1].split("og:image")[0].split("_")[1].split("_")[0] + "_" + str(div_tag).split("videoimg")[1].split("og:image")[0].split("_")[2].split("_")[0]
                csans = "https://vod-archive-kr-cdn-z01.afreecatv.com/v101/hls/highlight/20160822/207/bd72bbaa_180467207_1_2_A.mp4/original/both/"
        except:
            try:
                asans = str(div_tag).split("clip/")[1].split("_")[0]
                csans = f"https://vod-normal-kr-cdn-z01.afreecatv.com/v101/hls/clip/{asans}.smil/original/both/"
                bsans = "변수 재활용 개꿀ㅋ"
            except:        
                file = open('errorDebug.txt', "w")
                file.write(div_tag)
                file.close()
                print("지원하지 않는 정보입니다")
                print(f"이슈로 해당 URL을 보내주세요 : {isnumber}\n(스스로 해결하시려면, errorDebug.txt 파일을 확인해주세요)")
                quit()
if bsans == "변수 재활용 개꿀ㅋ":
    hsans = 20
else:
    hsans = 70
dsans = hsans # 처음부터 계산하면 너무 느리고, 404는 데이터 받는게 빠르게 때문에 70청크 부터 계산하는 효율적인 알고리즘 사용
esans = 0
fsans = 0
while True:
    if requests.get(f"{csans}seg-{dsans}.ts").status_code == 200:
        if dsans >= hsans:
            if esans == 1:
                break
            else:
                dsans += 10
                print(f"영상 청크 검색 중... / 현재 검색된 개수 : {dsans} ",end='\r')
        else:
            break
    else:
        dsans -= 1
        esans = 1
        print(f"영상 청크 검색 중... / 현재 검색된 개수 : {dsans} ",end='\r')
        if dsans == 0:
            print("\n오류 : 검색 인덱스 범위 초과 : URL을 다시 확인해주세요")
            quit()
removeList = []
gsans = 0
print()
if os.path.isfile(f"{wtfbro}.mp4"):
    os.remove(f"{wtfbro}.mp4")
for i in range(int(dsans) + 1):
    save_video(f"{csans}seg-{i}.ts", i)
    removeList.append(f"chunk-{i}.ts")
os.system(f"ffmpeg -f concat -i chunk-l.txt -c copy {wtfbro}.mp4")
os.remove("chunk-l.txt")
for i in removeList:
    os.remove(i)
os.system('cls')
print(f"\"{wtfbro}.mp4\"파일이 생성되었습니다, 제대로 생성되지 못한 경우, 다시 시도해주세요")
