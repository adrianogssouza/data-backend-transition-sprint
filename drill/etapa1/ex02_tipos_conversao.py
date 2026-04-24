print("Ola seja bem vindo!")

while True:    
    nome_usuario = input ("Digite seu nome: ")
    if  any(char.isdigit() for char in nome_usuario):
     print("Digite um nome que contenha apenas letras.")
    else:
        break
        
while True:
    try:
        salario_usuario = float (input ("Digite seu salario: "))
        break   
    except ValueError:
        print("Erro: Digite um numero valido")

while True:
    try:
        bonus_usuario = float (input ("Digite o Valor do Bonus: "))
        if bonus_usuario < 0 or bonus_usuario >1:
            print("Digite um valor entre 0 e 1")
        else: 
            break
    except ValueError:
        print("Erro: Digite um numero valido")

bonus_calculado = 1000 + salario_usuario * bonus_usuario
print(f"Ola {nome_usuario}, o seu bonus foi de R$ {bonus_calculado:.2f}")