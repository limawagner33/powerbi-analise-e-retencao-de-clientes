import pandas as pd
import random

# Configuração: gerar 1.000 clientes
num_clientes = 1000
dados = []

print("🔄 Gerando massa de dados simulada...")

for i in range(num_clientes):
    # 1. ID do Cliente
    customer_id = f"{random.randint(1000,9999)}-{''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=5))}"
    
    # 2. Perfil Demográfico
    genero = random.choice(['Masculino', 'Feminino'])
    idoso = random.choice([0, 0, 0, 1]) # 25% de chance de ser idoso
    parceiro = random.choice(['Sim', 'Não'])
    
    # 3. Contrato e Serviços
    # Lógica: Se for contrato mensal, a chance de cancelar (Churn) é maior
    contrato = random.choices(['Mensal', '1 Ano', '2 Anos'], weights=[50, 25, 25])[0]
    
    internet = random.choices(['Fibra Ótica', 'DSL', 'Não'], weights=[40, 40, 20])[0]
    
    # 4. Tempo de Casa (Tenure)
    # Se contrato é 2 anos, tempo de casa tende a ser maior
    if contrato == '2 Anos':
        meses_cliente = random.randint(24, 72)
    elif contrato == '1 Ano':
        meses_cliente = random.randint(12, 24)
    else:
        meses_cliente = random.randint(1, 12)
        
    # 5. Financeiro
    mensalidade = round(random.uniform(29.90, 119.90), 2)
    total_gasto = round(mensalidade * meses_cliente, 2)
    
    # 6. O Fator Churn (A "inteligência" do dado)
    # Criamos uma regra: Contrato mensal + Fibra Ótica = Alto Risco
    pontos_risco = 0
    if contrato == 'Mensal': pontos_risco += 3
    if internet == 'Fibra Ótica': pontos_risco += 1
    if meses_cliente < 6: pontos_risco += 2
    
    # Se tiver muitos pontos de risco, chance alta de cancelar
    if pontos_risco >= 4:
        churn = random.choices(['Sim', 'Não'], weights=[70, 30])[0]
    else:
        churn = random.choices(['Sim', 'Não'], weights=[10, 90])[0]

    # Adiciona na lista
    dados.append([customer_id, genero, idoso, parceiro, meses_cliente, internet, contrato, mensalidade, total_gasto, churn])

# Cria o DataFrame e salva em CSV
df = pd.DataFrame(dados, columns=[
    'ID_Cliente', 'Genero', 'Idoso', 'Parceiro', 'Meses_Contrato', 
    'Tipo_Internet', 'Tipo_Contrato', 'Valor_Mensal', 'Valor_Total', 'Cancelou_Churn'
])

# Salva o arquivo que o Power BI vai ler
df.to_csv('base_telecom_techconnect.csv', index=False, encoding='utf-8-sig')

print(f"✅ Sucesso! Arquivo 'base_telecom_techconnect.csv' criado com {num_clientes} linhas.")