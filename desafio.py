# Cálculo de Bônus com Entrada do Usuário

nome_usr = input("Digite seu nome: ")
salario_usr = int(input("Digite o valor do seu salário: "))
bonus_usr = float(input("Digite o valor do seu bônus: "))
constante_bonus = int(1000)
calculo_bonus = int(constante_bonus + salario_usr * bonus_usr)

print(f"Olá {nome_usr} o seu bônus foi de {calculo_bonus}")