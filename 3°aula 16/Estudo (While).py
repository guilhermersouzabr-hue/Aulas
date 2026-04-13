from time import sleep
x=0
while x<=100:
    print(x)
    x+=1
    sleep(0.01)

x=1
fim=int(input("Digite até qual número é para contar: "))
print("Os números ímpares são:")
while x<=fim:
    print(x)
    x+=2

x=3
while x<=30:
    print(x)
    x+=3

n=2
x=1
while x<=10:
    result=n*x
    print(f"2 X {x} = {result}")
    x+=1

n=int(input("Qual número você quer a tabuada?: "))
i=int(input("Qual o início da tabuada?: "))
f=int(input("Qual o fim da tabuada?: "))
x=i
while x<=f:
    result=n*x
    print(f"{n} X {x} = {result}")
    x+=1

di=float(input("Digite o depósito inicial: "))
tj=float(input("Digite a taxa de juros: "))
meses=1
while meses<=24:
    di=di+(di*(tj/100))
    print(f"Mês {meses} - R${di:.2f}")
    meses+=1
print(f"O ganho obtido em juros foi de R${di:.2f}")

di=float(input("Digite o depósito inicial: R$ "))
tj=float(input("Digite a taxa de juros: "))
investimento=float(input("Digite o investimento mensal: R$ "))
meses=1
while meses<=24:
    di=di+(di*(tj/100)) + investimento
    print(f"Mês {meses} - R${di:.2f}")
    meses+=1
print(f"O ganho obtido em juros foi de R${di:.2f}")

soma=0
quantidade=0
print("Digite 0 para parar a execução")
while True:
    numero=int(input("Digite um número inteiro: "))
    if numero==0:
        break
    soma=soma+numero
    quantidade=quantidade+1
print(f"Quantidade de números digitados: {quantidade}")
print(f"A soma dos números é: {soma}")
print(f"Média dos números: {soma/quantidade:.2f}")

print("=================================")
print("------Máquina Registradora-------")
print("=================================")
total=0
print("Para sair digite o 0")
while True:
    cód=int(input("Digite o código do produto: "))
    preço = 0
    if cód==0:
        print("Fim da execução")
        break
    elif cód==1:
        preço=0,50
    elif cód ==2:
        preço = 1
    elif cód ==3:
        preço = 4
    elif cód ==5:
        preço = 7
    elif cód ==5:
        preço = 8
    else:
        print("Código Inválido")
    if preço!=0:
        qtd=int(input("Digite a quantidade do produto: "))
        total=total+(qtd*preço)
    print(f"O total da compra foi R${total:.2f}")