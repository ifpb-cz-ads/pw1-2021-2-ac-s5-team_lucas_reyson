num01 = int(input('Informe o primeiro número: '))
num02 = int(input('Informe o segundo número: '))
num03 = int(input('Informe o terceiro número: '))

maior = num01
if num02 > num01 and num02 > num03:
    maior = num02

if num03 > num01 and num03 > num02:
    maior = num03

menor = num01
if num02 < num03 and num02 < num01:
    menor = num02

if num03 < num02 and num03 < num01:
    menor = num03

print('O maior numero é {}'.format(maior))
print('O menor numero é {}'.format(menor))