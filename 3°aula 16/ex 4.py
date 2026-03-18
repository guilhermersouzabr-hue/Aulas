d=int(input("Digite a distância que deseja percorrer: "))
if d<=200:
    pp=d*0.50
else:
    pp=d*0.45
print(f"O preço da passagem é R${pp:.2f}")