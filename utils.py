import re
from constant import GEUMJEONGGU_MAP, FOOD_CATEGORY


def printMessages(messages):
    print()
    print("\t┌" + "─" * 50 + "┐")
    for message in messages:
        # 문자열 내 공백 제거
        noSpaceMsg = re.sub(r"\s+", "", message)
        print("\t|{: ^{}}|".format(message, 50 - len(noSpaceMsg)))
    print("\t└" + "─" * 50 + "┘")
    print()


def inputRegion():
    print()
    for key, value in GEUMJEONGGU_MAP.items():
        print("\t" + key + ". " + value)
    print()
    while True:
        region = input("\t배달 지역(번호 입력): ")
        if region in GEUMJEONGGU_MAP.keys():
            break
        else:
            printMessages(["입력이 올바르지 않습니다", "다시 입력해주세요"])
            continue
    return GEUMJEONGGU_MAP[region]


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


def inputNumber(minNum, maxNum):
    while True:
        number = input("\t번호를 입력하세요: ")
        if number.isdigit() and minNum <= int(number) <= maxNum:
            break
        else:
            printMessages(["입력이 올바르지 않습니다", "다시 입력해주세요"])
            continue
    return int(number)
