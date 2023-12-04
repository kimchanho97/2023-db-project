# 2023 DB 텀프로젝트

## DB Schema

- admin(admin_id INT PK, user_name VARCHAR, password VARCHAR, email VARCHAR)
- client(client_id INT PK, restaurant_id INT FK, user_name VARCHAR, password VARCHAR, email VARCHAR)
- user(user_id INT PK, user_name VARCHAR, password VARCHAR, email VARCHAR, user_type ENUM{'normal', 'vip'})
- delivery_person(delivery_person_id INT PK, user_name VARCHAR, region VARCHAR, email VARCHAR, password VARCHAR, current_delivery_count INT)
- restaurant(restaurant_id INT PK, client_id INT FK, region VARCHAR, category VARCHAR, approval_status ENUM{'pending', 'accepted'}, restaurant_name VARCHAR, restuarant_address VARCHAR)
- menu(menu_id INT PK, restaurant_id INT FK, menu_name VARCHAR, price INT)
- cart(cart_id INT PK, user_id INT FK, menu_id INT FK, restaurant_id INT FK, quantity INT)
- order(order_id INT PK, user_id INT FK, restaurant_id INT FK, order_date DATE, destination_address VARCHAR)
- order_detail(cart_id INT FK, order_id INT FK)
- delivery_request(request_id INT PK, delivery_person_id INT FK, order_id INT FK, request_date DATE, delivery_status ENUM{'pending', 'accepted', 'completed'})

<br>

## ERD

<img width="1000" alt="스크린샷 2023-12-05 오전 1 51 30" src="https://github.com/kimchanho97/2023-db-project/assets/104095041/7f50ad13-b51f-4a58-b713-db6e23751776">

<br>

## 기능 구현

### 초기설정

- [x] DB 연결
- [x] relation 생성 & attribute 추가

<br>

### 로그인

- [ ] 유저 구분
- [ ] 유저 data 저장

<br>

### **Rebase 과정**

1. 같이 작업하고 있는 base에서 팀원의 PR이 머지됨
2. 현재 나의 branch(로컬)에서 작업한 것 → 커밋(커밋이 있을 경우)
3. `git switch base` (base 브랜치로 이동)
4. `git pull origin base` (머지된 변경사항을 base로 가져옴)
5. `git switch stem` (본인 브랜치로 이동)
6. `git rebase base` (base와 rebase 실시)
7. conflict 수정(만약 상대방의 코드 수정시 DM)
8. conflict 해결
9. `git add <file>`
10. `git rebase —continue`
11. 작업을 계속 수행한 뒤 → PR
