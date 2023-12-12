from db_config import con, cur
import utils


def acceptDeliveryRequest(requestId, userId, userType):
    if userType == "vip":
        cur.execute("""
                    SELECT current_delivery_count FROM riders WHERE rider_id = %s;
                    """, (userId,))
        currentDeliveryCount = cur.fetchone()[0]
        if currentDeliveryCount != 0:
            utils.printMessages(["현재 배달중인 주문이 있습니다"])
            return

    cur.execute("""
        UPDATE delivery_request SET delivery_status = 'accepted', rider_id = %s WHERE request_id = %s;
    """, (userId, requestId))
    cur.execute("""
        UPDATE riders SET current_delivery_count = current_delivery_count + 1 WHERE rider_id = %s;
    """, (userId,))
    con.commit()
    utils.printMessages(["배달 요청 수락 완료"])


def readOrder(userId):
    cur.execute("""
        SELECT region FROM riders WHERE rider_id = %s;
    """, (userId,))
    region = cur.fetchone()[0]
    cur.execute("""
        SELECT 
            dr.request_id,
            r.restaurant_name,
            r.restaurant_address,
            o.destination_address,
            dr.request_date,
            u.user_type
        FROM 
            delivery_request dr
        JOIN 
            orders o ON dr.order_id = o.order_id
        JOIn 
            users u ON o.user_id = u.user_id
        JOIN 
            restaurant r ON o.restaurant_id = r.restaurant_id
        WHERE 
            dr.delivery_status = 'pending' AND r.region = %s;
    """, (region,))
    rows = cur.fetchall()
    if not rows:
        utils.printMessages(["배달 가능한 주문이 없습니다"])
        return
    print(rows)
    print("\t|{:^6}|{:^8}|{:^12}|{:^12}|{:^16}|{:^6}|".format(
        "요청번호", "음식점명", "음식점 주소", "배달 주소", "배달 요청 일시", "한집배달"))
    print("\t"'+' + '-' * 10 + '+' + '-' * 12 + '+' + '-' * 17 + '+' +
          '-' * 16 + '+' + '-' * 22 + '+' + '-' * 10 + '+')
    print()
    for i in range(len(rows)):
        print("\t|{:^6}|{:^8}|{:^12}|{:^12}|{:^30}|{:^6}|".format(
            i + 1, rows[i][1], rows[i][2], rows[i][3], str(rows[i][4]), ("O" if rows[i][5] == "vip" else "X")))
    print()
    print("\t0. 뒤로가기")
    print()
    print("\t배달 요청 수락")
    number = utils.inputNumber(0, len(rows))
    if number == 0:
        return
    print()
    acceptDeliveryRequest(rows[number - 1][0], userId, rows[number - 1][5])


def doneDeliveryRequest(requestId, userId):
    cur.execute("""
        UPDATE delivery_request SET delivery_status = 'completed' WHERE request_id = %s;
    """, (requestId,))
    cur.execute("""
        UPDATE riders SET current_delivery_count = current_delivery_count - 1 WHERE rider_id = %s;
    """, (userId,))
    con.commit()
    utils.printMessages(["배달 완료 처리 완료"])


def readMyOrder(userId):
    cur.execute("""
        SELECT 
            dr.request_id,
            r.restaurant_name,
            r.restaurant_address,
            o.destination_address,
            dr.request_date,
            u.user_type
        FROM 
            delivery_request dr
        JOIN 
            orders o ON dr.order_id = o.order_id
        JOIn 
            users u ON o.user_id = u.user_id
        JOIN 
            restaurant r ON o.restaurant_id = r.restaurant_id
        WHERE 
            dr.delivery_status = 'accepted' AND dr.rider_id = %s;
    """, (userId,))
    rows = cur.fetchall()
    if not rows:
        utils.printMessages(["배달 주문 내역이 없습니다"])
        return
    print("\t|{:^6}|{:^8}|{:^12}|{:^12}|{:^16}|{:^6}|".format(
        "요청번호", "음식점명", "음식점 주소", "배달 주소", "배달 요청 일시", "한집배달"))
    print("\t"'+' + '-' * 10 + '+' + '-' * 12 + '+' + '-' * 17 + '+' +
          '-' * 16 + '+' + '-' * 22 + '+' + '-' * 10 + '+')
    print()
    for i in range(len(rows)):
        print("\t|{:^6}|{:^8}|{:^12}|{:^12}|{:^30}|{:^6}|".format(
            i + 1, rows[i][1], rows[i][2], rows[i][3], str(rows[i][4]), ("O" if rows[i][5] == "vip" else "X")))
    print()
    print("\t0. 뒤로가기")
    print()
    print("\t배달 완료 처리")
    number = utils.inputNumber(0, len(rows))
    if number == 0:
        return
    doneDeliveryRequest(rows[number - 1][0], userId)
    return


def inputFunction(userId):
    while True:
        print()
        print("\t1. 가능한 배달 주문 조회")
        print("\t2. 나의 배달 주문 조회")
        print("\t3. 로그아웃")
        print()
        function = input("\t번호를 입력하세요: ")
        print()
        if function == "1":
            readOrder(userId)
        elif function == "2":
            readMyOrder(userId)
        elif function == "3":
            utils.printMessages(["로그아웃 완료"])
            break
        else:
            utils.printMessages(["입력이 올바르지 않습니다", "다시 입력해주세요"])
            continue


# inputFunction(5)
