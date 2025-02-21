nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    print(f"Aluno aprovado! {media:.2f}")
elif media < 5:
    print(f"Aluno reprovado! {media:.2f}")
elif media <= 7:
    print(f"Aluno em recuperação. {media:.2f}")