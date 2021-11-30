valor = float(input("Infome o valor da casa: "))
salario = float(input("Informe seu salário salário: "))
anos = int(input("Informe a quantidade de anos a pagar: "))

meses = anos * 12
prest = valor / meses

if prest < salario * 0.3:
    print('Você não pode fazer um emprestimo ')
else:
    print('Você pode fazer o emprestimo, o valor da prestação é R$ {}'.format(prest))