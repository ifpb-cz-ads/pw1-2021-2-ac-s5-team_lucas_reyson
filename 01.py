velo = float(input('Infome a velocidade do seu caro: '))
if velo > 80:
    multa = (velo - 80) * 5
    print('Sua multa é de {}'.format(multa))
else: 
    print('Sua velocidade esta normal')
