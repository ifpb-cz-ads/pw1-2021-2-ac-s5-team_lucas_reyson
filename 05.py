n1 = float(input('Informe um número: '))
op = str(input('Informe um operador lógico: '))
n2 = float(input('Informe um número: '))
total = float

if op == '+':
    total = n1 + n2

elif op == '-':
    total = n1 - n2

elif op == '/':
    total == n1 / n2

elif op == '*':
    total = n1 * n2

print('Resultado {}'.format(total))