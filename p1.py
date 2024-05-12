import math

def gr(score):
    if score>=100: gap = 1
    elif score<60: gap = 6
    else: gap = math.ceil((100-score)/10)
    return chr(ord('A')-1+gap)

while True:
    score = int(input('성적을 입력하세요 (0=종료): '))
    if score == 0:
        break
    print('당신의 학점은',gr(score),'입니다.')
