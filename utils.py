# unils 함수 정리모음
"""코드작성일자 : 2024년 06월 10일
코드 작성자 : 민수홍
코드 이름 : util.py
코드 목적 : 유용한 함수를 따로 저장하여 두고 나중에 불러와 사용하기 위함
"""


def factorial(x):
    if x <= 1:
        return 1
    return x*factorial(x-1)

def gugudan(x):
    for i in range(9):
        print((i+1)*x)

