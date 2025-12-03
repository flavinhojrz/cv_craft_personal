import requests
import json
import os
import time
# Configurações
API_URL = "http://localhost:5000/api"
INPUT_JSON = "../data/resume.json"
OUTPUT_PDF = "curriculo.pdf"

def main():
    if not os.path.exists(INPUT_JSON):
        print(f"❌ Erro: Arquivo {INPUT_JSON} não encontrado.")
        return

    with open(INPUT_JSON, 'r', encoding='utf-8') as f:
        original_data = json.load(f)

    print("="*50)
    print("🚀 INICIANDO TESTE (COM CRONÔMETRO)")
    print("="*50)

    # --- MEDINDO A IA ---
    instruction = "Otimize o curriculo para Suporte de primeiro nível (N 1) aos clientes externos solucionando problemas Realizar atendimento aos clientes internos (colaboradores) e externos Utilizar os canais de abertura de tickets Fornecer status de demandas em evolução para o cliente (via telefone, e-mail, sistemas) Manter sistemas operacionais: Windows, Linux Contato com scripts e banco de dados"
    print(f"\n🧠 1. Enviando para a IA...")
    
    start_ai = time.time() 
    
    try:
        response_ai = requests.post(f"{API_URL}/optimize-resume", json={
            "data": original_data,
            "instructions": instruction,
            "sections": ["summary", "skills"]
        })
        
        end_ai = time.time() 
        print(f"⏱️  Tempo da IA: {end_ai - start_ai:.2f} segundos") 

        if response_ai.status_code != 200:
            print(f"❌ Erro na IA: {response_ai.text}")
            return
        
        optimized_data = response_ai.json()
        print("✅ IA OK!")

    except Exception as e:
        print(f"❌ Erro IA: {e}")
        return

    # --- MEDINDO O PDF ---
    print("\n🎨 2. Gerando PDF...")
    start_pdf = time.time() 

    try:
        response_pdf = requests.post(f"{API_URL}/generate-resume", json=optimized_data)
        
        end_pdf = time.time() 
        print(f"⏱️  Tempo do PDF: {end_pdf - start_pdf:.2f} segundos") 
        
        if response_pdf.status_code == 200:
            with open(OUTPUT_PDF, "wb") as f:
                f.write(response_pdf.content)
            print(f"🎉 PDF Gerado!")
        else:
            print(f"❌ Erro PDF: {response_pdf.text}")

    except Exception as e:
        print(f"❌ Erro PDF: {e}")

if __name__ == "__main__":
    main()