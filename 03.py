salario = float(input('Infome seu salário: '))

if salario > 1250:
    val_aul = 0.10
else:
    val_aul = 0.15

aumento = salario * val_aul

print('Seu almento é de {}'.format(aumento))