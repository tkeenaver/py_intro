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


s1 = {1, 2, 3}
s0 = set()
print(s0,s1)

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a & b, a.intersection(b))
print(a | b, a.union(b))
print(a - b, a.difference(b))
print(a ^ b, a.symmetric_difference(b))


