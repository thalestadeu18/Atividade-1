while True:
    nome = input("Digite o nome (maior que 3 caracteres): ")
    if len(nome) > 3:
        break  # Sai do loop se o nome for válido
    else:
        print("ERRO: O nome deve ter mais de 3 caracteres.")
while True:
        idade = int(input("Digite a idade (entre 0 e 150): "))
        if 0 <= idade <= 150:
            break
        else:
            print("ERRO: A idade deve estar entre 0 e 150.")
while True:
        salario = float(input("Digite o salário: R$ "))
        if salario >= 0:
            break
        else:
            print("ERRO: O salário deve ser maior que zero.")
while True:
    genero = input("digite seu genero 'f' para feminino ou 'm' para masculino: ")
    if genero == 'f' or genero == 'm':
        break
    else:
        print(f"ERRO: genero invalido")
while True:
    estado_civil = input("digite seu estado civil ('s', 'c', 'v', 'd'): ")
    if estado_civil in('s', 'c', 'v', 'd'):
        break
    else:
        print(f"ERRO: estado civil invalido. Digite 's', 'c', 'v' ou 'd'")

print(f"cadastro concluido")
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Salário: R$ {salario:.2f}")
print(f"Gênero: {genero}")
print(f"Estado Civil: {estado_civil}")


while True:
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    if num1 > num2:
        print(f"O maior número é: {num1}")
    elif num2 > num1:
        print(f"O maior número é: {num2}")
        break
    else:
        print("Os números são iguais.")

while True:
    valor = int(input("Digite um valor: "))
    if valor > 0:
        print("O valor é positivo.")
    elif valor < 0:
        print("O valor é negativo.")
        break
    else:
        print("valor neutro.")