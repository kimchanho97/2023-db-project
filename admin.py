from db_config import con, cur
import utils


def approveRestaurant():
    print()
    print("\t┌" + "─" * 50 + "┐")
    print("\t|{: ^42}|".format("미승인 음식점 조회"))
    print("\t└" + "─" * 50 + "┘")
    print()
    while True:
        cur.execute(
            "SELECT * FROM restaurant WHERE approval_status = 'pending'")
        rows = cur.fetchall()
        if rows:
            print()
            for row in rows:
                print("\t{}. {} | {} | {} | {} ".format(
                    row[0], row[5], row[3], row[2], row[6]))
            print("\t0. 뒤로가기")
            print()
            restaurantId = input("\t승인할 음식점 번호: ")
            if restaurantId == "0":
                break
            if restaurantId.isdigit():
                cur.execute(
                    f"UPDATE restaurant SET approval_status = 'accepted' WHERE restaurant_id = {restaurantId}")
                con.commit()
                utils.printMessages(["승인이 완료되었습니다."])
            else:
                utils.printMessages(["입력이 올바르지 않습니다."])
                continue
        else:
            utils.printMessages(["승인 대기중인 음식점이 없습니다."])
            break


def inputFunction(userId):
    while True:
        utils.printMessages(["메인 기능"])
        print("\t1. 미승인 음식점 조회")
        print("\t2. 로그아웃")
        print()
        function = input("\t번호를 입력하세요: ")
        print()
        if function == "1":
            approveRestaurant()
            continue
        elif function == "2":
            utils.printMessages(["로그아웃 완료"])
            break
        else:
            utils.printMessages(["입력이 올바르지 않습니다", "다시 입력해주세요"])
            continue
