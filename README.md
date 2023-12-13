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
  최근 배달 어플리케이션을 통해서 음식을 주문하게 되면, 배달시간이 정확하 게 나오지 않고, 실제 소요되는 시간보다 훨씬 크게 측정되어 실제 대기 시작 을 측정하는 데에서 불편함을 느끼고, 과도하게 시간이 측정되는 것을 개선하 기 위해서, 기존의 배달 어플리케이션의 구현된 것을 참고로 하여 현재 배달원 의 위치를 기반으로 한 개선된 어플리케이션을 개발하는 것이 초기의 목표 였 습니다.
  다만, 실시간의 정보를 DB에 저장하여 현재 요청을 수락하는 것이 아닌 DB 에 배달원의 위치 정보가 저장되어, 내가 그 지역에서 받을 수 있는 배달로 구현하였습니다.
  
### 개발 동기 및 목적
  금정배달관리시스템(Geumjeong Delivery Management System: GDMS)은 금정 구 내의 배달관리 시스템을 실제 서비스 되고 있는 어플리케이션(배달의 민족) 과 유사한 서비스를 할 수 있도록 구현 하려 했습니다.
  저희가 중점적으로 담당하려 했던 프로그램 방식은 음식점에서 배달 요구가 들어오면 가까운 거리에 있는 rider가 주문요청을 받아서 서비스되기를 바랐습 니다. 그렇게 하여 배송시간을 최적화 해보려고 했습니다. 다만 구현상의 어려 움으로 직접 거리계산 하는 것은 들어가지 못했습니다. 그래서 테이블 상에 구 정보가 일치하는 배달원rider를 조회하고 배달 요청이 들어갈 수 있도록 구성하 였습니다.

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
> - ✍️ 회원가입
> - 🔍 음식점 검색
    (이름, 지역, 카테고리)
> - 🛒 장바구니
> - 👨‍💼 등록 관리
> - 🏍️ 배달 목록 확인



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
