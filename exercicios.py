print("=========================================================")
print("                   Seja Bem Vindo                        ")
print("                         a                               ")
print("                InforTicoMaticaTeco                      ")
print("=========================================================")

print("------------------------")
print("| Tipo do Empregado    |")
print("------------------------")
print("|    Gerente           |")
print("|    Supervisor        |")
print("|    Servente          |")
print("------------------------")

cargo = input("Informe seu cargo: ").strip().lower()
horas_extras = float(input("Horas extras trabalhadas: "))
faltas = float(input("Faltas: "))
filhos = int(input("Filhos: ")) 


salarioB = 0.0  
if cargo == "gerente":
    salarioB = 2000.00
elif cargo == "supervisor":
    salarioB = 1500.00
elif cargo == "servente":
    salarioB = 1000.00
else:
    print("Cargo inválido!")
    exit()

valor_hora = salarioB / 240
valor_he = valor_hora * 2 * horas_extras  
beneficio_filhos = filhos * (0.03 * salarioB) 

desconto_faltas = (salarioB / 30) * faltas 

proventos = salarioB + valor_he + beneficio_filhos
imposto = proventos * 0.10 
descontos = desconto_faltas + imposto

salarioL = proventos - descontos


print("\n--- Resultado ---")
print(f"Salário Base: R$ {salarioB:.2f}")
print(f"Horas Extras: R$ {valor_he:.2f}")
print(f"Benefício Filhos: R$ {beneficio_filhos:.2f}")
print(f"Desconto Faltas: R$ {desconto_faltas:.2f}")
print(f"Imposto: R$ {imposto:.2f}")
print(f"Salário Líquido: R$ {salarioL:.2f}")