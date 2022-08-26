import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
basedir = os.path.dirname(os.path.abspath(__file__))

from app.services.calculator import CalculatorService
from app.services.user import UserService
from app.services.score import ScoreService
from app.services.grade import GradeService
def print_menu():
    print('0. 전체프로그램 종료')
    print('1. 계산기 프로그램')
    print('2. 로그인 프로그램') # 입력받은 아이디와 비번 콘솔에 출력하기
    print('3. 성적표 프로그램') # 입력받은 아이디와 비번 콘솔에 출력하기
    menu = input('메뉴 선택')
    return menu
    
def main():
    
    while 1:
        menu = print_menu()
        if menu == '0':
            print('전체 프로그램을 종료합니다')
            break
        elif menu == '1':
            calculatorService = CalculatorService()
            first = int(input('첫번째 값 입력: '))
            second = int(input('두번째 값 입력: '))
            calculatorService.calculate(first, second)
        elif menu == '2':
            userService = UserService()
            id = input('id')
            password = input('password')
            userService.login(id, password)
        elif menu == '3':
            # scoreService = ScoreService()
            gradeService = GradeService()
            name = input('이름')
            korean = input('국어')
            english = input('영어')
            math = input('수학')
            # grade = scoreService.score(name, korean, english, math)
            grade = gradeService.score(name, korean, english, math)
            print(grade)
            
if __name__ == '__main__' :
    main()
    