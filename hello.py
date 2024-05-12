import sys
if __name__ == '__main__':
    for i, arg in enumerate(sys.argv):
        print(f"Argument {i:>6}: {arg}")

import os
if __name__ == '__main__':
    cwd = os.getcwd()
    print(f'cwd = {cwd}')
    print(f"Arguments count: {len(sys.argv)}")

b1 = True
i1 = 10
f1 = 3.14
s1 = 'Hello'

l1 = [ b1, i1, f1, s1 ]
t1 = ( b1, i1, f1, s1 )
d1 = { b1:i1, f1:s1, i1:b1, s1:f1}
s2 = { b1, i1, f1, s1 }
