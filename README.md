# 8-HakyeonJiyeon

<html>
<img src="https://user-images.githubusercontent.com/57247474/142752602-2f874976-2f89-4e96-bbac-98ce640e3f47.png"  width="150" height="100"/>                                                                                                 </html>

8팀 학연지연팀 - 내 입맛에 맞는 장보기 서비스, 장봐구니 개발 레포지토리입니다. 

                                                                                
-----

## 💡 Project

- 기존 배달 서비스에서 착안한 내 입맛에 꼭 맞는 장보기 서비스 - ***'Jangbwaguni'***

### 소개
코로나로 인해 '랜선 장보기'의 수요가 늘어난 요즘, 신선식품의 배달에 대한 불만이 증가하였습니다.
                                                                                                                                         
그에 따라 **별점 제도**를 도입하여 라이더를 평가(신선도, 스피드, 정확도)하고, 신선도 점수가 높은 **라이더를 직접 선택**해 주문할 수 있도록 하여 불만을 해결하였습니다.
                                                                                                                                         
또한, **주문자이자 라이더로서 활동**할 수 있으며, 별점 제도로 인해 **배달 사고를 방지**할 수 있도록 하였습니다.

<br>

## 👨‍👦‍👦 Team

- **팀장 김승훈**: 프론트엔드[main, delivery, member], 백엔드[member]
- **팀원 김수아**: 프론트엔드[orderrequest, member], 백엔드[member, orderrequest]
- **팀원 하윤경**: 백엔드[delivery, member, orderrequest]

<br>

## 🔧 Tech Stack
### Server
<span>
<img src="https://user-images.githubusercontent.com/69155170/128126965-8bbf101e-8ed2-4740-92a7-b7b6699267f9.png" width="50px">
<img src="https://user-images.githubusercontent.com/69155170/128126891-f70886b7-a4ed-421d-8180-993639054d38.png" width="50px">
 </span>

<br>

## 🖥 Preview
### 📄 라이더 등록 페이지
<img width="812" alt="image" src="https://user-images.githubusercontent.com/57247474/142752214-18cd53d9-6a7e-4252-9161-5374536a27ec.png">

## 📄 배달 요청 페이지
<img width="1326" alt="image" src="https://user-images.githubusercontent.com/57247474/142752251-33fdfdaa-9569-488e-a690-af6430dfbd7d.png">

## 📄 주문하기 페이지
<img width="1180" alt="image" src="https://user-images.githubusercontent.com/57247474/142752259-ffacdced-6437-48a9-9d22-5bfd9d92a153.png">

## 📄 주문/배달내역 페이지
<img width="1136" alt="image" src="https://user-images.githubusercontent.com/57247474/142752264-d50002b9-9f3c-4053-959a-2be14133b0fa.png">

## 📄 고객/라이더 리뷰 페이지
<img width="965" alt="image" src="https://user-images.githubusercontent.com/57247474/142752273-4017c9c2-02cc-4966-aac1-fdbf1d9e87cc.png">



<br>

* **작업 시작 전 작업 내역 가져오기 (충돌 방지)**
```bash
# 로컬 저장소와 원격 저장소의 변경 사항이 다를 때 이를 비교 대조하고
# git merge 명령어와 함께 최신 데이터를 반영하거나 충돌 문제 등을 해결
$ git fetch

# 원격 저장소의 최신 내용을 로컬 저장소로 가져오면서 병합
$ git pull
```

<br>

* **develop 브랜치에 병합 전 requirements.txt 생성하기 (필요한 패키지 리스트)**
```bash
# pip로 설치된 패키지 목록 작성
$ pip freeze > requirements.txt

# requirements의 패키지 설치
$ pip install -r requirements.txt
```

<br>

* **secrets key 파일 불러오는 방법**
  * jangbwaguni 폴더에 있는 `secrets.json` 파일을 `manage.py` 파일이 있는 폴더로 이동

