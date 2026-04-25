# Análise de transações financeiras

transacoes = [
    {"id": 1, "valor": 250.00,   "hora": 10, "categoria": "alimentação"},
    {"id": 2, "valor": 15200.00, "hora": 14, "categoria": "eletrônicos"},
    {"id": 3, "valor": 89.90,    "hora": 8,  "categoria": "transporte"},
    {"id": 4, "valor": 430.00,   "hora": 20, "categoria": "saúde"},
    {"id": 5, "valor": 12.50,    "hora": 7,  "categoria": "alimentação"},
    {"id": 6, "valor": 9800.00,  "hora": 16, "categoria": "eletrônicos"},
    {"id": 7, "valor": 75.00,    "hora": 22, "categoria": "entretenimento"},
    {"id": 8, "valor": 300.00,   "hora": 12, "categoria": "saúde"},
]

def classificar_transacao(transacao): 
    if transacao["valor"] > 10000 or transacao["hora"] <9 or transacao["hora"]>18:
     return "suspeita" 
    return "normal"

for transacao in transacoes:
   resultado = classificar_transacao(transacao)
   print(f"{transacao['id']}->{resultado}")


