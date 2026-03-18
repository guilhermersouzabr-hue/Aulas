vel=int(input("Digite sua velocidade em km/h: "))
if vel>80:
    print("Você foi multado")
    multa = (vel - 80)*5
    print(f"O valor da multa é R${multa:.2f}")
else:
    print("Você não foi multado")
