print(1)
print(2)
print(3)

x=1
print(x)
x=x+1
print(x)
x=x+1
print(f"{x}\n")

x=1
while x<=3:
    print(x)
    x=x+1
print()

#exercício1
x=1
while x<=100:
    print(x)
    x=x+1
print()

#exercicio2
x=50
while x<=100:
    print(x)
    x=x+1
print()

#exercicio3
from time import sleep
x=10
while x>=0:
    print(x)
    sleep(0.1)
    x=x-1
print("Fogo!")
print()

#pares
fim=int(input("Digite o número de parada: "))
x=0
print("Os números pares são:")
while x<=fim:
    print(x)
    x=x+2
print()

#exercicio4
fim=int(input("Digite o número de parada: "))
x=1
print("Os números ímpares são:")
while x<=fim:
    print(x)
    x=x+2
print()

#exercicio5
x=3
print("Os Múltiplos de três são:")
while x<=30:
    print(x)
    x=x+3
print()

#Tabuada
n=int(input("Tabuada de qual número?: "))
x=1
while x<=10:
    print(f"{n}x{x}={n*x}")
    x=x+1
print()

#exercicio7
n=int(input("Tabuada de qual número?: "))
ini=int(input("Digite o ínicio da tabuada?: "))
fim=int(input("Digite o fim da tabuada?: "))
x=ini
while x<=fim:
    print(f"{n}x{x}={n*x}")
    x=x+1
print()

#exercicio8
soma = 0
cp = 1
while cp <= 3:
    ncp = float(input(f"Digite a nota do Checkpoint {cp}: "))
    soma = soma + ncp
    cp = cp + 1
print(f"A média das notas do Checkpoint é {soma/3:.2f}")