from db_config import con, cur
from datetime import datetime
import utils


def addCart(rows, restaurantId, userId):
    print()
    number = int(input("\t메뉴를 선택하세요(번호 입력): "))
    quantity = int(input("\t수량을 입력하세요: "))
    cur.execute("INSERT INTO cart (user_id, menu_id, restaurant_id, quantity) VALUES (%s, %s, %s, %s)",
                (userId, rows[number - 1][0], restaurantId, quantity))
    utils.printMessages(["장바구니 담기 완료"])
    con.commit()


def readCart(userId, restaurantId):
    print()
    cur.execute("""
        SELECT cart.*, menu.menu_name, menu.price
        FROM cart
        INNER JOIN menu ON cart.menu_id = menu.menu_id
        WHERE cart.user_id = %s AND cart.restaurant_id = %s AND cart.cart_status = 'pending'
    """, (userId, restaurantId))
    rows = cur.fetchall()
    print("\t장바구니")
    if rows:
        totalPrice = 0
        for i in range(len(rows)):
            print("\t{}. {} - {}개: {}원".format(
                i + 1, rows[i][6], rows[i][4], rows[i][4] * rows[i][7]))
            totalPrice += rows[i][7] * rows[i][4]
        print()
        print("\t총 가격: " + str(totalPrice) + "원")
    else:
        utils.printMessages(["장바구니가 비어있습니다"])


def orderCart(userId, restaurantId):
    cur.execute("SELECT * FROM cart WHERE user_id = %s AND restaurant_id = %s AND cart_status = 'pending'",
                (userId, restaurantId))
    rows = cur.fetchall()
    if not rows:
        utils.printMessages(["장바구니가 비어있습니다"])
        return
    print()
    print("\t주문하기")
    destination = input("\t배달지 주소: ")
    orderDate = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cartIds = [row[0] for row in rows]
    cur.execute("""
        INSERT INTO orders (user_id, restaurant_id, destination_address, order_date)
        VALUES (%s, %s, %s, %s)
        RETURNING order_id;
    """, (userId, restaurantId, destination, orderDate))
    orderId = cur.fetchone()[0]
    con.commit()
    for cartId in cartIds:
        cur.execute("""
            INSERT INTO order_detail (order_id, cart_id)
            VALUES (%s, %s)
        """, (orderId, cartId))
        con.commit()
    cur.execute("UPDATE cart SET cart_status = 'accepted' WHERE user_id = %s AND restaurant_id = %s",
                (userId, restaurantId))
    con.commit()
    utils.printMessages(["주문 완료"])


def selectMenus(restaurantId, userId):
    cur.execute("SELECT * FROM menu WHERE restaurant_id = %s", (restaurantId,))
    rows = cur.fetchall()
    if rows:
        while True:
            print()
            print("\t메뉴")
            for i in range(len(rows)):
                print("\t" + str(i + 1) + ". " +
                      rows[i][2] + " - " + str(rows[i][3]) + "원")
            print()
            print("\t1. 장바구니 담기")
            print("\t2. 장바구니 조회")
            print("\t3. 장바구니 주문하기")
            print("\t4. 음식점 나가기")
            print()
            number = utils.inputNumber(1, 4)
            if number == 1:
                addCart(rows, restaurantId, userId)
            elif number == 2:
                readCart(userId, restaurantId)
            elif number == 3:
                orderCart(userId, restaurantId)
            elif number == 4:
                utils.printMessages(["로그아웃 완료"])
                break
    else:
        utils.printMessages(["등록된 메뉴가 없습니다"])


def selectRestaurant(rows, userId):
    print("\t|{:^10}|{:^15}|{:^8}|{:^8}|{:^20}|".format(
        "음식점 번호", "음식점 이름", "카테고리", "배달지역", "상세주소"))
    print("\t"'+' + '-' * 15 + '+' + '-' * 20 + '+' +
          '-' * 12 + '+' + '-' * 12 + '+' + '-' * 24 + '+')
    print()
    for i in range(len(rows)):
        print("\t{}. {} | {} | {} | {}".format(
            i + 1, rows[i][5], rows[i][3], rows[i][2], rows[i][6]))
    utils.printMessages(["음식점 선택"])
    selectedNumber = utils.inputNumber(1, len(rows))
    restaurantId = rows[selectedNumber - 1][0]
    cur.execute(
        "SELECT * FROM restaurant WHERE restaurant_id = %s", (restaurantId,))
    row = cur.fetchone()
    utils.printMessages(["{}".format(row[5])])
    # 메뉴 출력
    selectMenus(restaurantId, userId)


def searchRestaurant(userId):
    utils.printMessages(["음식점 검색"])
    name = input("\t음식점 이름: ")
    print()
    cur.execute(
        "SELECT * FROM restaurant WHERE restaurant_name = %s and approval_status = 'accepted'", (name,))
    rows = cur.fetchall()
    if rows:
        selectRestaurant(rows, userId)
    else:
        utils.printMessages(["검색 결과가 없습니다"])


def searchRestaurantByRegion(userId):
    utils.printMessages(["음식점 검색"])
    region = utils.inputRegion()
    cur.execute(
        "SELECT * FROM restaurant WHERE region = %s and approval_status = 'accepted'", (region,))
    rows = cur.fetchall()
    if rows:
        selectRestaurant(rows, userId)
    else:
        utils.printMessages(["검색 결과가 없습니다"])


def searchRestaurantByCategory(userId):
    utils.printMessages(["음식점 검색"])
    category = utils.inputCategory()
    cur.execute(
        "SELECT * FROM restaurant WHERE category = %s and approval_status = 'accepted'", (category,))
    rows = cur.fetchall()
    if rows:
        selectRestaurant(rows, userId)
    else:
        utils.printMessages(["검색 결과가 없습니다"])


def inputFunction(userId):
    while True:
        print()
        print("\t1. 음식점 검색")
        print("\t2. 동네별로 음식점 조회")
        print("\t3. 카테고리별로 음식점 조회")
        print("\t4. 로그아웃")
        print()
        function = input("\t번호를 입력하세요: ")
        print()
        if function == "1":
            searchRestaurant(userId)
            continue
        elif function == "2":
            searchRestaurantByRegion(userId)
            continue
        elif function == "3":
            searchRestaurantByCategory(userId)
            continue
        elif function == "4":
            utils.printMessages(["로그아웃 완료"])
            break
        else:
            utils.printMessages(["입력이 올바르지 않습니다", "다시 입력해주세요"])
            continue


# inputFunction(1)
