vc=float(input("Digite o valor da casa em R$: "))
sal=float(input("Digite seu salario em R$: "))
aparc=int(input("Digite a quantidade de anos a pagar: "))
meses=aparc*12
prest=vc/meses
if prest<(sal*30)/100:
    print("Empréstimo aprovado!")
    print(f"O valor da prestação é de R${prest:.2f}")
else:
    print("Empréstimo negado, a prestação exede o valor de 30% referente seu salário!")