numero = int(input("Digite um número para calcular o fatorial: "))

resultado = 1
n = numero

while n > 1:
    resultado *= n
    n -= 1

print(f"O fatorial de {numero} é: {resultado}")
