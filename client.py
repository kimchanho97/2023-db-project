from db_config import con, cur
from constant import FOOD_CATEGORY, GEUMJEONGGU_MAP
import utils
from datetime import datetime


def enrollRestaurant(userId):
    utils.printMessages(["음식점 등록"])
    name = input("\t음식점 이름: ")
    region = utils.inputRegion()
    address = input("\t음식점 상세주소: ")
    category = utils.inputCategory()
    cur.execute("INSERT INTO restaurant (restaurant_name, region, restaurant_address, category, client_id) VALUES (%s, %s, %s, %s, %s) RETURNING restaurant_id",
                (name, region, address, category, userId))
    restaurantId = cur.fetchone()[0]
    cur.execute("UPDATE clients SET restaurant_id = %s WHERE client_id = %s",
                (restaurantId, userId))
    utils.printMessages(["음식점 등록 완료"])
    con.commit()


def inputPrice():
    while True:
        price = input("\t가격: ")
        if price.isdigit():
            break
        else:
            utils.printMessages(["입력이 올바르지 않습니다", "다시 입력해주세요"])
            continue
    return price


def addMenu(restaurantId):
    utils.printMessages(["메뉴 추가"])
    name = input("\t메뉴 이름: ")
    price = inputPrice()
    cur.execute("INSERT INTO menu (menu_name, price, restaurant_id) VALUES (%s, %s, %s)",
                (name, price, restaurantId))
    utils.printMessages(["메뉴 추가 완료"])
    con.commit()


def removeMenu(restaurantId):
    cur.execute("SELECT * FROM menu WHERE restaurant_id = %s", (restaurantId,))
    result = cur.fetchall()
    if not result:
        utils.printMessages(["등록된 메뉴가 없습니다"])
        return
    while True:
        number = input("\t삭제할 메뉴 번호: ")
        if number.isdigit():
            if int(number) < 1 or int(number) > len(result):
                utils.printMessages(["입력이 올바르지 않습니다", "다시 입력해주세요"])
                continue
            cur.execute("DELETE FROM menu WHERE menu_id = %s",
                        (result[int(number) - 1][0],))
            utils.printMessages(["메뉴 삭제 완료"])
            con.commit()
            break
        else:
            utils.printMessages(["입력이 올바르지 않습니다", "다시 입력해주세요"])
            continue


def readMyRestaurant(userId):
    cur.execute("SELECT * FROM restaurant WHERE client_id = %s", (userId,))
    row = cur.fetchone()
    utils.printMessages(["나의 음식점 조회"])
    print("\t음식점 이름: " + row[5])
    print("\t음식점 배달 지역: " + row[2])
    print("\t음식점 상세 주소: " + row[6])
    print("\t음식점 카테고리: " + row[3])
    print("\t음식점 승인 상태: " + ('승인완료' if row[4] == 'accepted' else '승인 미완료'))
    print()
    while True:
        cur.execute("SELECT * FROM menu WHERE restaurant_id = %s", (row[0],))
        result = cur.fetchall()
        if result:
            print("\t메뉴")
            for i in range(len(result)):
                print("\t" + str(i + 1) + ". " +
                      result[i][2] + " - " + str(result[i][3]) + "원")
            print()
        else:
            utils.printMessages(["등록된 메뉴가 없습니다"])
        print("\t1) 메뉴 추가")
        print("\t2) 메뉴 삭제")
        print("\t3) 뒤로가기")
        print()
        function = utils.inputNumber(1, 3)
        if function == 1:
            addMenu(row[0])
            continue
        elif function == 2:
            removeMenu(row[0])
            continue
        elif function == 3:
            break


def checkRestaurant(userId):
    cur.execute("SELECT * FROM restaurant WHERE client_id = %s", (userId,))
    result = cur.fetchone()
    if result:
        return result[0]
    else:
        return False


def requestDelivery(orderId):
    cur.execute("UPDATE orders SET order_status = 'accepted' WHERE order_id = %s",
                (orderId,))
    requestDate = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cur.execute("INSERT INTO delivery_request (order_id, delivery_status, request_date) VALUES (%s, 'pending', %s)",
                (orderId, requestDate))
    con.commit()
    utils.printMessages(["배달 요청 완료"])


def readOrder(restaurantId):
    cur.execute("SELECT * FROM orders WHERE restaurant_id = %s",
                (restaurantId,))
    result = cur.fetchall()
    if result:
        print("\t----- 주문 내역 -----")
        cur.execute(
            """
            SELECT 
                o.order_id,
                m.menu_name,
                m.price,
                c.quantity,
                o.destination_address,
                o.order_date
            FROM 
                orders o
            JOIN 
                order_detail od ON o.order_id = od.order_id
            JOIN 
                cart c ON od.cart_id = c.cart_id AND c.cart_status = 'accepted'
            JOIN 
                menu m ON c.menu_id = m.menu_id
            WHERE 
                o.restaurant_id = %s AND o.order_status = 'pending'
            ORDER BY 
                o.order_id;
            """, (restaurantId,))
        result = cur.fetchall()
        if not result:
            utils.printMessages(["주문 내역이 없습니다"])
            return
        beforeOrderId = 0
        for i in range(len(result)):
            if result[i][0] != beforeOrderId:
                if beforeOrderId != 0:
                    print()
                print("\t주문 번호: " + str(result[i][0]))
                print("\t주문 일시: " + str(result[i][5]))
                print("\t배달 주소: " + str(result[i][4]))
                beforeOrderId = result[i][0]
            print("\t\t{} - {}개: {}원".format(
                result[i][1], result[i][3], result[i][2] * result[i][3]))
        print()
        print("\t0. 뒤로가기")
        print()
        print("\t----- 배달 요청 -----")
        while True:
            orderId = input("\t주문 번호 입력: ")
            orderIds = [result[i][0] for i in range(len(result))]
            if orderId == "0":
                return
            if orderId.isdigit() and int(orderId) in orderIds:
                requestDelivery(orderId)
                break
            else:
                utils.printMessages(["입력이 올바르지 않습니다", "다시 입력해주세요"])
                continue
    else:
        utils.printMessages(["주문 내역이 없습니다"])


def inputFunction(userId):
    while True:
        restaurantId = checkRestaurant(userId)
        utils.printMessages(["메인 기능"])
        print("\t1. 음식점 등록")
        print("\t2. 나의 음식점 조회")
        print("\t3. 주문 조회")
        print("\t4. 로그아웃")
        print()
        function = input("\t번호를 입력하세요: ")
        print()
        if function == "1":
            if restaurantId:
                utils.printMessages(["이미 등록된 음식점이 있습니다"])
                continue
            enrollRestaurant(userId)
        elif function == "2":
            if not restaurantId:
                utils.printMessages(["등록된 음식점이 없습니다"])
                continue
            readMyRestaurant(userId)
        elif function == "3":
            if not restaurantId:
                utils.printMessages(["등록된 음식점이 없습니다"])
                continue
            readOrder(restaurantId)
        elif function == "4":
            utils.printMessages(["로그아웃 완료"])
            break
        else:
            utils.printMessages(["입력이 올바르지 않습니다", "다시 입력해주세요"])
            continue


# inputFunction(5)
