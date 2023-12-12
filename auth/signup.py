import sys
import os
import re

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from db_config import con, cur


GEUMJEONGGU_MAP = {
    "1": "두구동",
    "2": "노포동",
    "3": "청룡동",
    "4": "남산동",
    "5": "선동",
    "6": "오륜동",
    "7": "구서동",
    "8": "장전동",
    "9": "부곡동",
    "10": "서동",
    "11": "금사동",
    "12": "회동동",
    "13": "금성동",
    "14": "서1동",
    "15": "서2동",
    "16": "서3동",
    "17": "금사회동동",
    "18": "부곡1동",
    "19": "부곡2동",
    "20": "부곡3동",
    "21": "부곡4동",
    "22": "장전1동",
    "23": "장전2동",
    "24": "선두구동",
    "25": "청룡노포동",
    "26": "구서1동",
    "27": "구서2동"
}


def printErrorMessages(messages):
    print()
    print("\t┌" + "─" * 50 + "┐")
    for message in messages:
        # 문자열 내 공백 제거
        noSpaceMsg = re.sub(r"\s+", "", message)
        print("\t|{: ^{}}|".format(message, 50 - len(noSpaceMsg)))
    print("\t└" + "─" * 50 + "┘")
    print()


def inputRole():
    while True:
        print("\t역할구분")
        print("\t1. 소비자")
        print("\t2. 음식점 사장님")
        print("\t3. 배달원")
        print()
        role = input("\t번호를 입력하세요: ")
        if role == "1":
            role = "users"
            break
        elif role == "2":
            role = "clients"
            break
        elif role == "3":
            role = "riders"
            break
        else:
            printErrorMessages(["입력이 올바르지 않습니다", "번호를 다시 입력해주세요"])
            continue
    return role


def inputName():
    while True:
        name = input("\t이름: ")
        if len(name) == 0:
            printErrorMessages(["이름을 입력해주세요"])
            continue
        break
    return name


def validateEmail(email):
    emailRegex = re.compile(
        r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    if re.match(emailRegex, email):
        return True
    else:
        return False


def inputEmail():
    while True:
        email = input("\t이메일: ")
        # 이메일이 비어있는지 확인
        if len(email) == 0:
            printErrorMessages(["이메일을 입력해주세요"])
            continue
        # 이메일 형식이 올바른지 확인
        if validateEmail(email) == False:
            printErrorMessages(["이메일 형식이 올바르지 않습니다"])
            continue
        break
    return email


def getEmail():
    while True:
        email = inputEmail()
        print()
        input("\t이메일 중복 확인 >> Enter")
        result = []
        # users, clients, riders 테이블에서 이메일 중복 확인
        cur.execute(
            f"SELECT * FROM users WHERE email='{email}';")
        result.extend(cur.fetchall())
        cur.execute(
            f"SELECT * FROM clients WHERE email='{email}';")
        result.extend(cur.fetchall())
        cur.execute(
            f"SELECT * FROM riders WHERE email='{email}';")
        result.extend(cur.fetchall())
        if len(result) != 0:
            printErrorMessages(["이미 사용중인 이메일입니다"])
            continue
        printErrorMessages(["사용 가능한 이메일입니다"])
        break
    return email


def inputPassword():
    while True:
        password = input("\t비밀번호: ")
        if len(password) == 0:
            printErrorMessages(["비밀번호를 입력해주세요"])
            continue
        if len(password) < 8:
            print()
            print("\t┌" + "─" * 50 + "┐")
            print("\t|{: ^34}|".format("비밀번호는 8자 이상으로 설정해주세요"))
            print("\t└" + "─" * 50 + "┘")
            print()
            continue
        break
    return password


def getPassword():
    while True:
        password = inputPassword()
        passwordConfirm = input("\t비밀번호 확인: ")
        if password != passwordConfirm:
            printErrorMessages(["비밀번호가 일치하지 않습니다", "비밀번호를 다시 입력해주세요"])
            continue
        break
    return password


def inputRegion():
    while True:
        print()
        print("\t배달 가능 지역")
        print("\t1. 두구동")
        print("\t2. 노포동")
        print("\t3. 청룡동")
        print("\t4. 남산동")
        print("\t5. 선동")
        print("\t6. 오륜동")
        print("\t7. 구서동")
        print("\t8. 장전동")
        print("\t9. 부곡동")
        print("\t10. 서동")
        print("\t11. 금사동")
        print("\t12. 회동동")
        print("\t13. 금성동")
        print("\t14. 서1동")
        print("\t15. 서2동")
        print("\t16. 서3동")
        print("\t17. 금사회동동")
        print("\t18. 부곡1동")
        print("\t19. 부곡2동")
        print("\t20. 부곡3동")
        print("\t21. 부곡4동")
        print("\t22. 장전1동")
        print("\t23. 장전2동")
        print("\t24. 선두구동")
        print("\t25. 청룡노포동")
        print("\t26. 구서1동")
        print("\t27. 구서2동")
        print()
        region = input("\t번호를 입력하세요: ")
        if region not in GEUMJEONGGU_MAP.keys():
            printErrorMessages(["입력이 올바르지 않습니다", "번호를 다시 입력해주세요"])
            continue
        break
    return GEUMJEONGGU_MAP[region]


def storeUserInDB(role, name, email, password, region):
    if role == "riders":
        cur.execute(
            f"insert into {role} (user_name, region, email, password) values ('{name}', '{region}', '{email}', '{password}');")
    else:
        cur.execute(
            f"insert into {role} (user_name, email, password) values ('{name}', '{email}', '{password}');")


def register():
    print()
    print("\t┌" + "─" * 50 + "┐")
    print("\t|{: ^46}|".format("회원가입"))
    print("\t└" + "─" * 50 + "┘")
    print()
    role = inputRole()
    print()
    name = inputName()
    email = getEmail()
    password = getPassword()
    region = ""
    if role == "riders":
        region = inputRegion()
    storeUserInDB(role, name, email, password, region)
    print()
    printErrorMessages(["회원가입이 완료되었습니다"])
    print()
    con.commit()
