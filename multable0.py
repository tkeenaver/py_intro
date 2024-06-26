mmin = 2
mmax = 9
nmin = 1
nmax = 9

ss = '-'*29
print(f'\n{ss}구구단{ss}')

for i in range(mmin,mmax+1):
    print(f'  {i}단  ', end=' ')
print()

for j in range(nmin,nmax+1):
    for i in range(mmin,mmax+1):
        print(f'{i:>2}x{j}={i*j:<2}', end=' ')
    print()
ss = '-'*64
print(ss)
