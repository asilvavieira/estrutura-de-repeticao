# 13. Faça um programa que peça dois números, base e
# expoente, calcule e mostre o primeiro número elevado
# ao segundo número. Não utilize a função de potência
# da linguagem.

print("Vamos calcular potenciação")
base = int(input("Digite o número da base: "))
expoente = int(input("Digite o número do expoente: "))
potencia = 1

for i in (range(expoente)):
    potencia *= base
    print(potencia)