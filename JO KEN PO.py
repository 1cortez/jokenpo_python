from random import randint
itens = ["Pedra","Papel","Tesoura"]
comput = randint(0,2)

print(""" Suas opções ->
      [0] Pedra
      [1] Papel
      [2] Tesoura""")
player = int(input("Insira sua opção -> "))
print("-=" * 11)
print(f"Vc escolheu -> {itens[player]}")
print(f"O PC escolheu -> {itens[comput]}")
print("-=" * 11)

if player == comput:
    print("EMPATE :(")
else:
    if player == 0 and comput == 1:
        print("O PC venceu!")
    elif player == 1 and comput == 0:
        print("O player venceu!")
    if player == 1 and comput == 2:
        print("O PC venceu!")
    elif player == 2 and comput == 1:
        print("O player venceu!")
    if player == 2 and comput == 0:
        print("O PC venceu!")
    elif player == 0 and comput == 2:
        print("O player venceu!")

 


