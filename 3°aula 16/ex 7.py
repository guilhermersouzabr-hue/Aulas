kwh=int(input("Digite a quantidade de kwh consumidos: "))
ti=input("Qual o tipo de instalação? Digite R para residências, C para comércios e I para indústrias: ")
if ti=="R" and kwh<=500:
    print("O preço a pagar pelo fornecimento de energia é R$0.40")
elif ti=="R" and kwh>500:
    print("O preço a pagar pelo fornecimento de energia é R$0.65")
elif ti=="C" and kwh<=1000:
    print("O preço a pagar pelo fornecimento de energia é R$0.55")
elif ti=="C" and kwh>1000:
    print("O preço a pagar pelo fornecimento de energia é R$0.60")
elif ti=="I" and kwh<=5000:
    print("O preço a pagar pelo fornecimento de energia é R$0.55")
elif ti=="I" and kwh>5000:
    print("O preço a pagar pelo fornecimento de energia é R$0.60")