from random import randint



numero = int(input('Digite um número:\n'))
resultado = randint(1,10)

if numero == resultado:
    print('Parabéns! Você acertou')
else:
    print(f'Você errou! O número sorteado foi {resultado}')
