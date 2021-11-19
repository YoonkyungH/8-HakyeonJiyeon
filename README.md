# 8-HakyeonJiyeon
8팀 학연지연팀 - 내 입맛에 맞는 장보기 서비스, 장봐구니 개발 레포지토리입니다. 

-----

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
