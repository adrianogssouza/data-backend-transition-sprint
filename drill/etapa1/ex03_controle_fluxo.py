# Análise de transações financeiras

transacoes = [  # lista de dicionários — cada dicionário é uma transação com 4 chaves
    {"id": 1, "valor": 250.00,   "hora": 10, "categoria": "alimentação"},
    {"id": 2, "valor": 15200.00, "hora": 14, "categoria": "eletrônicos"},
    {"id": 3, "valor": 89.90,    "hora": 8,  "categoria": "transporte"},
    {"id": 4, "valor": 430.00,   "hora": 20, "categoria": "saúde"},
    {"id": 5, "valor": 12.50,    "hora": 7,  "categoria": "alimentação"},
    {"id": 6, "valor": 9800.00,  "hora": 16, "categoria": "eletrônicos"},
    {"id": 7, "valor": 75.00,    "hora": 22, "categoria": "entretenimento"},
    {"id": 8, "valor": 300.00,   "hora": 12, "categoria": "saúde"},
]

def classificar_transacao(transacao):  # def cria uma função — transacao é o parâmetro que recebe o dicionário passado na chamada
    if transacao["valor"] > 10000 or transacao["hora"] < 9 or transacao["hora"] > 18:  # acessa o valor da chave no dicionário — or significa que basta uma condição ser verdadeira
        return "suspeita"  # Python sai da função imediatamente ao encontrar return — não executa mais nada abaixo
    return "normal"  # só chega aqui se nenhuma condição do if foi verdadeira

total_por_categoria = {}  # dicionário vazio — vai acumular o total gasto por categoria ao longo do loop
suspeitas = 0  # contador zerado — vai ser incrementado a cada transação suspeita
normais = 0  # contador zerado — vai ser incrementado a cada transação normal

for transacao in transacoes:  # for percorre a lista um elemento por vez — a cada volta, transacao recebe um dicionário diferente
    categoria = transacao["categoria"]  # extrai a categoria do dicionário atual — armazena na variável para usar abaixo
    valor = transacao["valor"]  # extrai o valor do dicionário atual — armazena na variável para usar abaixo

    if categoria in total_por_categoria:  # verifica se a chave já existe no dicionário acumulador
        total_por_categoria[categoria] += valor  # chave já existe — soma o valor ao total acumulado
    else:
        total_por_categoria[categoria] = valor  # chave não existe ainda — cria a chave com o valor inicial

    resultado = classificar_transacao(transacao)  # chama a função passando o dicionário atual — retorna "suspeita" ou "normal"

    if resultado == "suspeita":  # == compara o conteúdo das strings — verifica se são iguais
        suspeitas += 1  # incrementa o contador — equivale a suspeitas = suspeitas + 1
    else:
        normais += 1  # mesma lógica para o contador de normais

    print(f"{transacao['id']}->{resultado}")  # f-string monta a string com os valores das variáveis dentro de {} — imprime id e classificação de cada transação

print(f"Suspeitas: {suspeitas}")  # fora do for — imprime o total acumulado após todas as 8 iterações
print(f"Normais: {normais}")  # mesma lógica
print(total_por_categoria)  # exibe o dicionário completo com o total por categoria



