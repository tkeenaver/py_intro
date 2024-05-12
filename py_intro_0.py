sfx0 = '1.79769313486231580793728971405303415079934132710037e+308'
print(f'max float = {float(sfx0)}')
sfn0 = '2.47032822920623272088284396434110686182529901307163e-324'
print(f'min float = {float(sfn0)}')

sfx1 = '1.79769313486231570814527423731704356798070567525845e+308'
print(f'max float = {float(sfx1):<.50e}')
sfn1 = '4.94065645841246544176568792868221372365059802614325e-324'
print(f'min float = {float(sfn1):<.50e}')

from mpmath import mp
mp.dps=100
print(mp.nstr(mp.pi,n=100))

from decimal import Decimal, getcontext
getcontext().prec = 5000
d5 = Decimal(5)
d555 = d5**d5**d5
f1 = d555 / Decimal(3.141592)
print(f1)

sfx1 = '1.7976931348623157081452742e+308'
print(f'max float = {float(sfx1):<.25e}')
sfn1 = '4.9406564584124654417656879e-324'
print(f'min float = {float(sfn1):<.25e}')

d555 = 5**5**5
d444 = 4**4**4
dd54 = d555 // d444
#fd54 = d555 / d444 # OverflowError: integer division result too large for a float

i1 = 10
i2 = 0b10110011
i3 = 0o7141
i4 = 0x1f7d
i5 = 1_234_000_000
print( i1, i2, i3, i4, i5)
print(f'{i1} 0b{i2:b} 0o{i3:o} 0x{i4:x} {i5:,}')

import scipy
scipy.constants.N_A
scipy.constants.m_e

s1 = 'Hello'
s2 = "Korea"
s3 = '''여러 줄에 
걸쳐져 있는 
문자열입니다.'''
print(f's1={s1},s2={s2},s3={s3}')

s3.split('\n')
'*'.join(s1)

b1 = True
b2 = False
i = 1; j = 2
b3 = i>0 and j<3
b3
if b2 or b3:
	print('적어도 둘중 하나는 참')

l1 = [ True, 12, 3.14, '안녕?' ]
l2 = [ 1, [ 2.1, 3.4], 'Hello' ]
print(l1,l2)

l3 = [[1,2,3,4,5],[2,3,4,5,6],[3,4,5,6,7]]
from pprint import pprint
pprint(l3,width=20)

l4 = [1,2,3,4,5,6,7,8,9]
list1 = [i for i in range(1,101)]
list1[::-1]

t1 = (1,2,3,4,5,6,7,8,9)
t1[3]
t1[1:7:2]
t1[5] = 3

t2 = (3,4,5)
a,b,c = t2
print(a,b,c)

d1 = {1:2,3:4,5:6,'k1':'v1',5:7}
d1[1]
d1['k1']
d1[5]
d1[2]
d1[100] = 'Hello'
d1


l1 = [2,5,3,7,1]
l2 = sorted(l1)
l1.sort()
l1
l1.append(3.14)
l1.insert(2, 0.001)
l1
l1.remove(2)
l1.pop()

l1.extend([7,8,9])
l1.index(0.001)
l1.count(7)

l0 = [1,2,3]
list(map(lambda x:x**2,l0))


d2 = {1:2,3:4,5:6}
d2.get(1)
d2.get(2,100)
d2.setdefault(10, 3.14)
d2[10]
d3={11:12,13:14,15:16}
d3
d2.update(d3)
d2

d2.keys()
list(d2.keys())
list(d2.values())
list(d2.items())
dict.fromkeys(d2.keys(),0)


i1,i2,i3,i4,i5 = 1,2,3,4,5
i6 = (i1 % i2) + (i3*i4) // i5
i6
i3 >= i6
i3 > i6
(i3>=i6) and (i2<i4)
1 in [1,2,3]
0 in [1,2,3]
l1 = [1,2,3,4,5,6,7,8,9]
l1[2:8:2]
i4 in [1,2,3]