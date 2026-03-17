med=float(input("Digite sua média: "))
if med>=6:
    print("Aprovado")
else:
    print("Reprovado")

vel=int(input("Digite sua velocidade em km/h: "))
if vel>80:
    print("Você foi multado")
    multa = (vel - 80)*5
    print(f"O valor da multa é R${multa:.2f}")
else:
    print("Você não foi multado")

n1=int(input("Digite o 1° número: "))
n2=int(input("Digite o 2° número: "))
n3=int(input("Digite o 3° número: "))

if n1>=n2 and n1>=n3:
    maior=n1
if n2>=n1 and n2>=n3:
    maior=n2
if n3>=n1 and n3>=n2:
    maior=n3
if n1<=n2 and n1<=n3:
    menor=n1
if n2<=n1 and n2<=n3:
    menor=n2
if n3<=n1 and n3<=n2:
    menor=n3
print(f"O maior número é o {maior:.0f}")
print(f"O menor número é o {menor:.0f}")

sal = float(input("Digite o salário do funcionário R$ "))
if sal>1250:
    nsal = (sal*10)/100+sal
else:
    nsal = (sal*15)/100+sal
print(f"O novo salário é de R${nsal:.2f}")

d=int(input("Digite a distância que deseja percorrer: "))
if d<=200:
    pp=d*0.50
else:
    pp=d*0.45
print(f"O preço da passagem é R${pp:.2f}")