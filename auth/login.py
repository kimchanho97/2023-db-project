import sys
import os
import re
from signup import signup, printErrorMessages

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import main


cur = main.cur
con = main.con


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


def checkSignup():
    while True:
        isHaveAccount = input("\t계정이 있으신가요? (y/n): ")
        if isHaveAccount == "y":
            return
        elif isHaveAccount == "n":
            signup()
            print("\t┌" + "─" * 50 + "┐")
            print("\t|{: ^47}|".format("로그인"))
            print("\t└" + "─" * 50 + "┘")
            return
        else:
            printErrorMessages(["입력이 올바르지 않습니다", "다시 입력해주세요"])


def login():
    print()
    print("\t┌" + "─" * 50 + "┐")
    print("\t|{: ^47}|".format("로그인"))
    print("\t└" + "─" * 50 + "┘")
    print()
    checkSignup()
    print()
    role = inputRole()
    print()
    while True:
        email = input("\t이메일: ")
        password = input("\t비밀번호: ")
        cur.execute(
            f"SELECT * FROM {role} WHERE email='{email}' AND password='{password}'")
        result = cur.fetchone()
        if result is None:
            printErrorMessages(["이메일 또는 비밀번호가 올바르지 않습니다"])
            continue
        break
    printErrorMessages(["로그인 성공"])


login()
