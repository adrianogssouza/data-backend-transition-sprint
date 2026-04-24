print("Ola seja bem vindo!") # exibe texto fixo na tela

while True: # loop infinito — repete até encontrar um break
    nome_usuario = input("Digite seu nome: ") # input() espera o usuário digitar e retorna sempre str
    if any(char.isdigit() for char in nome_usuario): # percorre cada caractere do nome — se qualquer um for dígito, retorna True
        print("Digite um nome que contenha apenas letras.") # informa o erro — sem break, o loop repete
    else:
        break # nenhum dígito encontrado — nome válido, encerra o loop

while True: # novo loop infinito — agora para o salário
    try: # tenta executar o bloco abaixo — se der erro, vai para o except
        salario_usuario = float(input("Digite seu salario: ")) # input() retorna str — float() converte para número decimal, lança ValueError se não conseguir
        break # conversão funcionou — salário válido, encerra o loop
    except ValueError: # captura o erro do float() quando o usuário digita texto
        print("Erro: Digite um numero valido") # informa o erro — loop repete

while True: # loop para o bônus — mesma estrutura do salário com validação extra
    try:
        bonus_usuario = float(input("Digite o Valor do Bonus: ")) # mesma lógica — converte para float, lança ValueError se não conseguir
        if bonus_usuario < 0 or bonus_usuario > 1: # verifica se o valor está fora do intervalo — or significa que basta uma condição ser verdadeira
            print("Digite um valor entre 0 e 1") # informa erro de intervalo — sem break, loop repete
        else:
            break # valor dentro do intervalo — bônus válido, encerra o loop
    except ValueError:
        print("Erro: Digite um numero valido") # captura texto no lugar de número

bonus_calculado = 1000 + salario_usuario * bonus_usuario # calcula o bônus — ambas variáveis já são float, convertidas nos loops acima

print(f"Ola {nome_usuario}, o seu bonus foi de R$ {bonus_calculado:.2f}") # f-string permite inserir variáveis com {} — :.2f formata o número com duas casas decimais