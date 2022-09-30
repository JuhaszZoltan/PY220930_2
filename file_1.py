nev = input('hogy hívnak? ')
print(f'Milyen szép név az, hogy {nev}!')
print(f'amúgy 2 + 3 = {2 + 3}')

szam = int(input('hányszor írjam ki a neved? '))

for x in range(szam):
    print(f'{x}. {nev}', end='\n')