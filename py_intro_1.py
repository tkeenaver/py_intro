'''score = int(input('성적을 입력하세요: '))
grade = 'F'
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 80:
    grade = 'C'
elif score >= 80:
    grade = 'D'
print('당신의 학점은',grade,'입니다.')
'''
import math
def gr(score):
    if score>=100:
        gap = 1
    elif score<60:
        gap = 6
    else:
        gap = math.ceil((100-score)/10)
    return chr(ord('A')-1+gap)
score = int(input('성적을 입력하세요: '))
print('당신의 학점은',gr(score),'입니다.')
