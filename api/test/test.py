import requests
import json
import os

with open('../data/resume.json', 'r', encoding='utf-8') as f:
    meu_cv = json.load(f)

payload = {
    "data": meu_cv,
    "instructions": "Otimize o curriculo para Suporte de primeiro nível (N 1) aos clientes externos solucionando problemas Realizar atendimento aos clientes internos (colaboradores) e externos Utilizar os canais de abertura de tickets Fornecer status de demandas em evolução para o cliente (via telefone, e-mail, sistemas) Manter sistemas operacionais: Windows, Linux Contato com scripts e banco de dados",
    
    "sections": ["summary", "skills"] 
}

print("Enviando requisição...")
response = requests.post('http://localhost:5000/api/optimize-resume', json=payload)

if response.status_code == 200:
    novo_json = response.json()
    
    print("\n--- 1. RESUMO (Esperado: MUDOU ✅) ---")
    print(f"Original: {meu_cv['basics']['summary'][:50]}...")
    print(f"Novo:     {novo_json['basics']['summary'][:50]}...")
    
    print("\n--- 2. SKILLS (Esperado: MUDOU ✅) ---")
    skills_iguais = novo_json['skills'] == meu_cv['skills']
    print(f"Skills idênticas? {'SIM (Erro)' if skills_iguais else 'NÃO (Certo, a IA otimizou)'}")

    print("\n--- 3. EXPERIÊNCIA (Esperado: IGUAL ✅) ---")
    exp_iguais = novo_json['experience'] == meu_cv['experience']
    print(f"Experience foi preservada? {'SIM ✅ (Perfeito)' if exp_iguais else 'NÃO ❌ (Erro, a IA mexeu onde não devia)'}")
    
else:
    print("Erro:", response.text)