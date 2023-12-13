# 2023-2 DB 텀프로젝트

> 목차
>
> - [📌 프로젝트 소개](#프로젝트-소개)
> - [👩‍👩‍👧‍👧 팀원 소개](#팀원-소개)
> - [🚩 시작 가이드](#시작-가이드)
> - [✏️ 주요 기능](#주요-기능)
> - [⭐️ 개발 주안점](#개발-주안점)
> - [📜 ERD](#erd)
> - [📁 파일 구조](#파일-구조)

## 프로젝트 소개

### 개발 동기 및 목적

금정구 배달 관리 시스템(Geumjeong Delivery Management System: GDMS)은 지역 중심의 맞춤형 배달 서비스를 제공하는 플랫폼입니다. 이 서비스는 금정구 내에서만 운영되며, 이는 배달 라이더가 자신이 잘 아는 지역 내에서만 배달을 수행함으로써 서비스의 품질을 향상시키는데 초점을 맞추고 있습니다.

이 시스템은 기존 배달 서비스의 기능을 통합하여 유저에 따른 각각의 기능을 제공합니다. 음식점 주인은 자신의 음식점을 쉽게 등록하고 주문을 효과적으로 관리할 수 있습니다. 고객은 다양한 음식점에서 원하는 음식을 편리하게 주문할 수 있습니다. 그리고 라이더들은 배달 건을 쉽게 관리할 수 있도록 도와줍니다.

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

## 시작 가이드

### 실행 방법

1. 프로젝트 클론

```bash
git clone https://github.com/kimchanho97/2023-db-project.git
cd 2023-db-project
```

2. 실행

```bash
pip install psycopg2
python mocking.py
python main.py
```

- mocking.py: 초기 데이터 생성
- main.py: 프로그램 실행

<br>

### 테스트 계정

- 관리자

  ```
  email: admin@example.com
  password: password
  ```

- 고객

  ```
  email: user1@example.com
  password: password1
  ```

- 음식점 사장님

  ```
  email: client5@example.com
  password: password5
  ```

- 라이더
  ```
  email: rider5@example.com
  password: password5
  ```

<br>

## 주요 기능

> - 고객
>
>   - 음식점 조회(동네, 카테고리, 검색)
>   - 장바구니 담기 및 삭제
>   - 장바구니 주문
>   - 주문 내역 조회
>
> - 음식점 사장님
>   - 음식점 등록
>   - 메뉴 등록 및 삭제
>   - 배달 주문 요청
> - 라이더
>   - 배달 주문 조회 및 접수
>   - 배달 주문 내역 조회

<br>

## 개발 주안점

### 예외 처리

```python
def inputCategory():
    print()
    for key, value in FOOD_CATEGORY.items():
        print("\t" + key + ". " + value)
    print()
    while True:
        category = input("\t음식점 카테고리(번호 입력): ")
        if category in FOOD_CATEGORY.keys():
            break
        else:
            printMessages(["입력이 올바르지 않습니다", "다시 입력해주세요"])
            continue
    return FOOD_CATEGORY[category]
```

이 프로젝트는 사용자의 터미널 입력에 기반하여 동작하는 CLI 환경에서 구현되었습니다. 이러한 환경에서는 웹 프론트엔드와 백엔드에서 수행하는 예외 처리를 터미널 상에서 직접 처리해주어야 합니다. 이를 위해, 모든 사용자 입력은 검증되고 정확한 값이 입력될 때까지 사용자로부터 재입력을 요청하였으며 잘못된 입력이 들어올 경우, 프로그램은 에러 메시지를 터미널에 출력하여 사용자에게 피드백을 제공하도록 구현하였습니다. 이런 방식으로, 사용자 경험을 향상시키면서 프로그램이 정상적으로 작동하도록 보장하였습니다.

<br>

### 트랜잭션

```python
def doneDeliveryRequest(requestId, userId):
    cur.execute("""
        UPDATE delivery_request SET delivery_status = 'completed' WHERE request_id = %s RETURNING order_id;
    """, (requestId,))
    orderId = cur.fetchone()[0]
    cur.execute("""
        UPDATE riders SET current_delivery_count = current_delivery_count - 1 WHERE rider_id = %s ;
    """, (userId,))
    cur.execute("""
        UPDATE orders SET order_status = 'completed' WHERE order_id = %s;
    """, (orderId,))
    con.commit()
    utils.printMessages(["배달 완료 처리 완료"])
```

트랜잭션은 데이터베이스에서 한 번에 수행되어야 하는 작업의 단위를 의미합니다. 트랜잭션 내의 모든 변경 사항은 데이터베이스에 원자적(atomic)으로 적용되어야 하며 이는 트랜잭션 내의 모든 변경 사항이 성공적으로 적용되거나, 아무것도 적용되지 않아야 함을 의미합니다. 위 코드는 배달을 완료했을 때 수행하는 함수로써 배달 완료시 진행되는 쿼리를 수행한 뒤 `con.commit()` 을 호출하여 트랜잭션을 완료하고 있습니다. 이는 `cur.execute()` 를 통해 수행된 모든 SQL 명령의 변경 사항을 데이터베이스에 반영한다는 뜻으로 psycopg2에서는 위와 같이 트랜잭션을 관리합니다. 따라서, 세 개의 SQL 업데이트 명령이 모두 성공적으로 완료되어야만 최종적으로 데이터베이스에 변경 사항이 반영됩니다.

<br>

## ERD

<img width="1000" alt="스크린샷 2023-12-12 오후 6 22 24" src="https://github.com/kimchanho97/2023-db-project/assets/104095041/21bc63f3-bbeb-4966-bcaf-f375abebca73">

<br>

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
