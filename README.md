# 2023-2 DB 텀프로젝트

> 목차
>
> - [📌 프로젝트 소개](#프로젝트-소개)
> - [👩‍👩‍👧‍👧 팀원 소개](#팀원-소개)
> - [✏️ 주요 기능](#주요-기능)
> - [📜 ERD](#erd)
> - [📁 파일 구조](#파일-구조)
> - [🚩 시작 가이드](#시작-가이드)

## 프로젝트 소개

### 개발 동기 및 목적

<br>

### 서비스 소개

1.
2.
3.
4.

<br>

### 개발 기간

2023.11.10 - 2023.12.12

<br>

## 팀원 소개

|          [김찬호](https://github.com/kimchanho97)          |          [이강빈](https://github.com/tonyusingit)          |
| :--------------------------------------------------------: | :--------------------------------------------------------: |
| <img src="https://github.com/kimchanho97.png" width="100"> | <img src="https://github.com/tonyusingit.png" width="100"> |
|                      user, rider 구현                      |                     client, admin 구현                     |

<br>

## ERD

<img width="1000" alt="스크린샷 2023-12-12 오후 6 22 24" src="https://github.com/kimchanho97/2023-db-project/assets/104095041/21bc63f3-bbeb-4966-bcaf-f375abebca73">

<br>

## 주요 기능

> - ✏️ 음식점 검색
> - 🗨️ 채팅 상담
> - 📜 견적서
> - 💯 리뷰
> - 💳 결제

| 음식점 검색                                                                                                                       | 검색 및 필터링                                                                                                                    |
| --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| <img width="380" src="https://github.com/Step3-kakao-tech-campus/Team5_FE/assets/104095041/18e4e9cc-87ed-4053-bec3-fd25e48fda29"> | <img width="380" src="https://github.com/Step3-kakao-tech-campus/Team5_FE/assets/104095041/a52c056e-9912-4062-b926-b1c64eb78eb9"> |
| • 플래너가 등록한 정보, 이미지, 리뷰 등 조회 <br> • 멤버십 사용자 - 이전 계약 정보(가격, 업체 등) 조회 <br>                       | • 지역과 가격 등 필터링 조건 설정 <br> • 플래너 이름 검색                                                                         |

| 채팅 전송                                                                                                              | 채팅 응답                                                                                                                         |
| ---------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| <img width="380" src="https://github.com/kimchanho97/algorithm/assets/104095041/d3b0faf7-d20c-4e83-9d66-00d2c38253c6"> | <img width="380" src="https://github.com/Step3-kakao-tech-campus/Team5_FE/assets/104095041/0863820b-a151-4551-8c01-c8478e3a49ad"> |
| • 이미지 전송                                                                                                          | • 읽음 유무 표시 <br> • 안 읽은 메시지 개수 표시                                                                                  |

| 포트폴리오 작성 / 수정                                                                                                            | 견적서 작성 / 수정                                                                                                                |
| --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| <img width="380" src="https://github.com/Step3-kakao-tech-campus/Team5_FE/assets/104095041/2474a94c-6a19-4e02-b047-500b80b307a6"> | <img width="380" src="https://github.com/Step3-kakao-tech-campus/Team5_FE/assets/104095041/7c2c1e74-4bb1-4682-b26f-51fb07015f1a"> |
| • 플래너의 소개, 가격 등의 정보를 등록 <br> • 수정 및 삭제                                                                        | • 견적서 항목에 대한 정보 등록 <br> • 수정 및 삭제                                                                                |

| 리뷰 작성 / 수정                                                                                                                  | 리뷰 조회                                                                                                                         |
| --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| <img width="380" src="https://github.com/Step3-kakao-tech-campus/Team5_FE/assets/104095041/aed20cd4-a50d-4084-ba63-99c00e160de7"> | <img width="380" src="https://github.com/Step3-kakao-tech-campus/Team5_FE/assets/104095041/4997bb5f-aa6e-47d5-a60c-aea1d166f75c"> |
| • 플래너의 별점 및 후기 등록 <br> • 수정 및 삭제                                                                                  | • 해당 플래너의 리뷰 조회                                                                                                         |

| 결제                                                                                                                              | 찜하기                                                                                                                            |
| --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| <img width="380" src="https://github.com/Step3-kakao-tech-campus/Team5_FE/assets/104095041/1a03508c-5e5a-43c1-a367-3a8a82f92dcb"> | <img width="380" src="https://github.com/Step3-kakao-tech-campus/Team5_FE/assets/104095041/452e1f91-7115-46f2-83de-7e0e007fce99"> |
| • 토스 페이먼츠 연동 <br> • 결제 승인 & 유저 등급 업그레이드                                                                      | • 찜하기 등록 및 삭제 <br> • 찜하기 모아보기                                                                                      |

<br>

## 개발 주안점

### 예외 처리

### 트랜잭션

## 파일 구조

```
├───📂auth
│   ├───📜login.py
│   └───📜signup.py
├───📜admin.py
├───📜client.py
├───📜constant.py
├───📜db_config.py
├───📜main.py
├───📜mocking.py
├───📜rider.py
├───📜user.py
└───📜utils.py
```

<br>

## 시작 가이드

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=white)

> Requirements: Python3, psycopg2

1. 프로젝트 클론

```bash
git clone https://github.com/kimchanho97/2023-db-project.git
cd 2023-db-project
```

2. 실행

```bash
pip install psycopg2
python db_config.py
python mocking.py
python main.py
```

- db_config.py: 테이블 생성 및 Foreign Key 설정
- mocking.py: 초기 데이터 생성
- main.py: 프로그램 실행
  <br>
