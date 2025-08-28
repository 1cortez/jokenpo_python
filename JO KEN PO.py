#  [DESAFIO] Crie um jogo de JoKenPo (Pedra-Papel-Tesoura)

from random import randint
lista = ["pedra", "papel", "tesoura"]
pc = randint(0,2)

print("""JO-KEN-PO

[0] = PEDRA
[1] = PAPEL
[2] = TESOURA
""")
user = int(input("Insira sua escolha : "))

if user == pc:
    print(f"O PC escolheu {lista[pc].upper()}")
    print(f"Você escolheu {lista[user].upper()}")
    print("===== Empate ======")
elif (pc == 0 and user == 1) or (pc == 1 and user == 2) or (pc == 2 and user == 0):
    print(f"O PC escolheu {lista[pc].upper()}")
    print(f"Você escolheu {lista[user].upper()}")
    print("Você venceu!")
else:
    print(f"O PC escolheu {lista[pc].upper()}")
    print(f"Você escolheu {lista[user].upper()}")
    print("O PC venceu!")



