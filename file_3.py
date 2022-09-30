x = 1
c = 0
while x < 10000000:
    print(f'2^{c} = {x}')
    x = x * 2
    c += 1 # c=c+1
print(f'2 hatványainak száma 10M-ig: {c} db')