dist = float(input('Quantos KM você pretende percorrer? '))
preco = float

if dist <= 200:
    preco = dist * 0.50

elif dist > 200:
    preco = dist * 0.45

print('A viagem custou {}'.format(preco))