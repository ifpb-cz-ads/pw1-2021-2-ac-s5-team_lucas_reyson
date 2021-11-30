faixa = float(input('Quantos kWh são consumidos? '))
resid = str(input('Qual tipo de intalação desejada?\n I para Industrial;\n C para Comercial;\n R para Residencial.\n'))
pag = str

if resid == 'R':
    if faixa <= 500:
        pag = 'R$0.40'
    elif faixa > 500:
        pag = 'R$0.65'
    print('O valor pago será de {}'.format(pag))

elif resid == 'C':
    if faixa <= 1000:
        pag = 'R$0.55'
    elif faixa > 1000:
        pag = 'R$0.60'
    print('O valor pago será de {}'.format(pag))

elif resid == 'I':
    if faixa <=5000:
        pag = 'R$0.55'
    elif faixa > 5000:
        pag = 'R$0.60'
    print('O valor pago será de {}'.format(pag))

else:
    print('Informe um caractere válido')