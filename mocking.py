from db_config import con, cur
from datetime import datetime


def createAdminData():
    cur.execute("""
        INSERT INTO admin(user_name, email, password)
        VALUES 
        ('관리자', 'admin@example.com', 'password');
    """)
    con.commit()


def createUsersData():
    cur.execute("""
        INSERT INTO users(user_name, email, password, user_type)
        VALUES 
        ('김우주', 'user1@example.com', 'password1', 'normal'),
        ('김사랑', 'user2@example.com', 'password2', 'vip'),
        ('김지구', 'user3@example.com', 'password3', 'normal'),
        ('김은하', 'user4@example.com', 'password4', 'normal');
    """)
    con.commit()


def createClientsData():
    # 세글자 한글 이름 리스트. 실제 사용을 원하시면 더 많은 이름을 추가하셔야 합니다.
    names = ['김철수', '이영희', '박준형', '최은미', '홍길동',
             '김민지', '이지현', '박지훈', '최현우', '홍성희',
             '김민수', '이지훈', '박지우', '최현수', '홍성민',
             '박찬호', '이승엽', '김현수', '류현진', '오승환',
             '박세리', '이민아', '김연아', '김연경', '박태환',
             '박지성', '이청용', '손흥민', '이강인', '황의조',
             '유재석', '박명수', '정준하', '하하', '노홍철',
             '유인나', '박나래', '정은지', '하니', '하동훈']

    for i in range(1, 41):  # 40개의 데이터 생성
        name = names[i % len(names)]  # 이름 리스트에서 이름 선택
        email = f'client{i}@example.com'  # 이메일 생성
        password = f'password{i}'  # 비밀번호 생성

        cur.execute("""
            INSERT INTO clients(restaurant_id, user_name, email, password)
            VALUES (null, %s, %s, %s);
        """, (name, email, password))
        con.commit()


def createRidersData():
    # 세글자 한글 이름 리스트. 실제 사용을 원하시면 더 많은 이름을 추가하셔야 합니다.
    names = ['김철수', '이영희', '박준형', '최은미', '홍길동',
             '김민지', '이지현', '박지훈', '최현우', '홍성희']

    # 지역 리스트(1, 2, 3, 4, 5)
    regions = ['두구동', '노포동', '청룡동', '남산동', '선동']

    for i in range(1, 11):  # 10개의 데이터 생성
        name = names[i % len(names)]  # 이름 리스트에서 이름 선택
        region = regions[i % len(regions)]  # 지역 리스트에서 지역 선택
        email = f'rider{i}@example.com'  # 이메일 생성
        password = f'password{i}'  # 비밀번호 생성

        cur.execute("""
            INSERT INTO riders(user_name, region, current_delivery_count, email, password)
            VALUES (%s, %s, %s, %s, %s);
        """, (name, region, 0, email, password))
        con.commit()

    cur.execute("""
        UPDATE riders
        SET current_delivery_count = 1
        WHERE rider_id = 5;
    """)
    con.commit()


def createRestaurantData():
    # 세글자 한글 이름 리스트. 실제 사용을 원하시면 더 많은 이름을 추가하셔야 합니다.
    restaurant_names = ['재석보쌈', '철수돈까스', '승엽피자', '현수중식', '현진족발',
                        '승환보쌈', '세리돈까스', '민아피자', '연아중식', '연경족발',
                        '태환보쌈', '지성돈까스', '청용피자', '흥민중식', '강인족발',
                        '의조보쌈', '재석돈까스', '명수피자', '준하중식', '하하족발',
                        '홍철보쌈', '인나돈까스', '나래피자', '은지중식', '하니족발',
                        '동훈보쌈', '철수돈까스', '영희피자', '준형중식', '은미족발',
                        '길동보쌈', '민지돈까스', '지현피자', '지훈중식', '현우족발',
                        '성희보쌈', '민수돈까스', '지훈피자', '현수중식', '성민족발']

    # 지역 리스트
    regions = ['두구동', '노포동', '청룡동', '남산동', '선동']

    # 카테고리 리스트
    categories = ['족발·보쌈', '돈까스·회', '피자', '중식', '치킨']

    for i in range(1, 41):  # 40개의 데이터 생성
        name = restaurant_names[i % len(restaurant_names)]  # 이름 리스트에서 이름 선택
        region = regions[i % len(regions)]  # 지역 리스트에서 지역 선택
        category = categories[i % len(categories)]  # 카테고리 리스트에서 카테고리 선택
        address = f'{region} {i}번지'  # 주소 생성

        cur.execute("""
            INSERT INTO restaurant(client_id, region, category, approval_status, restaurant_name, restaurant_address)
            VALUES (%s, %s, %s, 'accepted', %s, %s);
        """, (i, region, category, name, address))
        con.commit()

    # restaurant_id 참조하는 clients 테이블의 restaurant_id 업데이트
    for i in range(1, 41):
        cur.execute("""
            UPDATE clients
            SET restaurant_id = %s
            WHERE client_id = %s;
        """, (i, i))
        con.commit()


def createMenuData():
    # 메뉴 이름 리스트
    menu_names = ['김치찌개', '된장찌개', '비빔밥', '김밥', '라면',
                  '돈까스', '피자', '스파게티', '불고기', '삼겹살',
                  '치킨', '햄버거', '샌드위치', '콜라', '사이다',
                  '아메리카노', '카페라떼', '프라페', '아이스크림', '초코케이크']

    for i in range(20):  # 20개의 데이터 생성
        menu_name = menu_names[i]  # 메뉴 이름 리스트에서 메뉴 이름 선택
        price = (i + 1) * 1000  # 가격 설정 (1000 ~ 20000)

        cur.execute("""
            INSERT INTO menu(restaurant_id, menu_name, price)
            VALUES (%s, %s, %s);
        """, ((i % 5) + 1, menu_name, price))
        con.commit()


def createCartData():
    # cart 테이블에 데이터 삽입
    data = [
        (14, 2, 15, 5, 1, 'accepted'),
        (15, 2, 10, 5, 1, 'accepted'),
        (16, 2, 20, 5, 1, 'accepted'),
        (1, 1, 5, 5, 2, 'accepted'),
        (2, 1, 10, 5, 2, 'accepted'),
        (3, 1, 15, 5, 3, 'accepted'),
        (4, 1, 20, 5, 4, 'accepted'),
        (5, 1, 5, 5, 10, 'accepted'),
        (6, 1, 10, 5, 3, 'accepted'),
        (7, 1, 20, 5, 1, 'accepted'),
        (8, 1, 15, 5, 1, 'accepted'),
        (9, 1, 15, 5, 5, 'accepted'),
        (10, 1, 10, 5, 4, 'accepted'),
        (11, 1, 15, 5, 1, 'accepted'),
        (12, 1, 10, 5, 1, 'accepted'),
        (13, 1, 20, 5, 1, 'accepted')
    ]

    for entry in data:
        cur.execute("""
            INSERT INTO cart(cart_id, user_id, menu_id, restaurant_id, quantity, cart_status)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, entry)
        con.commit()


def createOrdersData():
    # order 테이블에 데이터 삽입
    data = [
        (6, 1, 5, '부산대학교 도서관', datetime(2023, 12, 12, 18, 33, 21), 'pending'),
        (7, 1, 5, '부산대학교 대운동장', datetime(2023, 12, 12, 18, 33, 38), 'pending'),
        (8, 1, 5, '부산대학교 기계관', datetime(2023, 12, 12, 18, 33, 49), 'pending'),
        (2, 1, 5, '부산대학교 정문', datetime(2023, 12, 12, 18, 31, 2), 'accepted'),
        (3, 1, 5, '부산대학교 본관', datetime(2023, 12, 12, 18, 31, 15), 'accepted'),
        (4, 1, 5, '부산대학교 넉터', datetime(2023, 12, 12, 18, 31, 27), 'accepted'),
        (5, 1, 5, '부산대학교 약학관', datetime(2023, 12, 12, 18, 31, 40), 'accepted'),
        (9, 1, 5, '부산대학교 6408', datetime(2023, 12, 12, 18, 42, 58), 'pending'),
        (10, 1, 5, '부산대학교 6514', datetime(2023, 12, 12, 18, 43, 10), 'pending'),
        (11, 1, 5, '부산대학교 6516', datetime(2023, 12, 12, 18, 43, 20), 'pending'),
        (13, 2, 5, '부산대학교 6203', datetime(2023, 12, 12, 18, 44, 21), 'pending'),
        (12, 2, 5, '부산대학교 6202', datetime(2023, 12, 12, 18, 44, 11), 'accepted'),
        (14, 2, 5, '부산대학교 6514', datetime(2023, 12, 12, 18, 44, 37), 'accepted'),
        (1, 1, 5, '부산대학교 1공학관', datetime(2023, 12, 12, 18, 29, 45), 'completed')
    ]

    for entry in data:
        cur.execute("""
            INSERT INTO orders(order_id, user_id, restaurant_id, destination_address, order_date, order_status)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, entry)
        con.commit()


def createOrderDetailData():
    # order_detail 테이블에 데이터 삽입
    data = [
        (1, 1),
        (1, 2),
        (2, 3),
        (3, 4),
        (4, 5),
        (5, 6),
        (6, 7),
        (6, 8),
        (7, 9),
        (8, 10),
        (9, 11),
        (10, 12),
        (11, 13),
        (12, 14),
        (13, 15),
        (14, 16)
    ]

    for entry in data:
        cur.execute("""
            INSERT INTO order_detail(order_id, cart_id)
            VALUES (%s, %s)
        """, entry)
        con.commit()


def createDeliveryRequestData():
    # delivery_request 테이블에 데이터 삽입
    data = [
        (4, 3, None, datetime(2023, 12, 12, 18, 38, 31), 'pending'),
        (5, 4, None, datetime(2023, 12, 12, 18, 38, 34), 'pending'),
        (6, 5, None, datetime(2023, 12, 12, 18, 38, 37), 'pending'),
        (7, 12, None, datetime(2023, 12, 12, 18, 45, 4), 'pending'),
        (8, 14, None, datetime(2023, 12, 12, 18, 45, 7), 'pending'),
        (1, 1, 5, datetime(2023, 12, 12, 18, 34, 10), 'completed'),
        (3, 2, 5, datetime(2023, 12, 12, 18, 38, 27), 'accepted')
    ]

    for entry in data:
        cur.execute("""
            INSERT INTO delivery_request(request_id, order_id, rider_id, request_date, delivery_status)
            VALUES (%s, %s, %s, %s, %s)
        """, entry)
        con.commit()


def mockUp():
    createAdminData()
    createUsersData()
    createClientsData()
    createRidersData()
    createRestaurantData()

    createMenuData()
    createCartData()
    createOrdersData()
    createOrderDetailData()
    createDeliveryRequestData()


mockUp()
