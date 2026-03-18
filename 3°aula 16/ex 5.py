n1=float(input("Digite um número: "))
n2=float(input("Digite outro número: "))
op=input("Qual operação você deseja realizar, +, -, * ou /?: ")
if op=="+":
    result=n1+n2
elif op=="-":
     result=n1-n2
elif op=="*":
    result=n1*n2
elif op=="/":
    result=n1/n2
print(f"O resultado da operação é {result:.2f}")