import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
basedir = os.path.dirname(os.path.abspath(__file__))

from app.services.calculator import CalculatorService
from app.services.user import UserService
from app.services.grade import GradeService
from app.services.pandas_quiz import PandasQuiz
from app.services.titanic import TitanicService
def print_menu():
    print('0. 전체프로그램 종료')
    print('1. 계산기 프로그램')
    print('2. 로그인 프로그램') 
    print('3. 성적표 프로그램') 
    print('4. 판다스 퀴즈풀기') 
    print('5. 타이타닉 프로그램') 
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
            korean = int(input('국어'))
            english = int(input('영어'))
            math = int(input('수학'))
            # grade = scoreService.score(name, korean, english, math)
            grade = gradeService.get_grade(name, korean, english, math)
            print(f'이름: {name} 학점: {grade}')
            
        elif menu == '4':
            quiz = PandasQuiz()
            while 1:
                quiz_number = input('퀴즈번호 선택. 종료는 0 : ')
                if quiz_number == '0':
                    break
                elif quiz_number == '1':
                    quiz.quiz_01()
        elif menu == '5':
            titanicService = TitanicService()
            titanicService.submit(
                path='data/titanic/',train='train.csv', test='test.csv')

if __name__ == '__main__' :
    main()
    