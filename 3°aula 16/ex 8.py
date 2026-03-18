nota1=float(input("Digite a primeira nota: "))
nota2=float(input("Digite a segunda nota: "))
media=(nota1+nota2)/2
if media>=6:
    print(f"Média {media:.2f}, Aluno aprovado!")
elif media>=4 and media<6:
    print(f"Média {media:.2f}, Aluno de exame!")
elif media<4:
    print(f"Média {media:.2f}, Aluno Reprovado!")
