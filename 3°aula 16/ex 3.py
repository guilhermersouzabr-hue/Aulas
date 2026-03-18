sal = float(input("Digite o salário do funcionário R$ "))
if sal>1250:
    nsal = (sal*10)/100+sal
else:
    nsal = (sal*15)/100+sal
print(f"O novo salário é de R${nsal:.2f}")
