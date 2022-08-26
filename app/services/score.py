from app.models.score import Score
class ScoreService(object):
    def __init__(self) -> None:
        pass
        

    def score(self, name, korean, english, math):
        score = Score(name, korean, english, math)
        print(f'이름 : {score.name}')
        print(f'국어 : {score.korean}')
        print(f'영어 : {score.english}')
        print(f'수학 : {score.math}')
        print(f'평균 : {score.ave}')
        
        