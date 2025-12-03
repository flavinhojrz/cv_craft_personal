from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GOOGLE_GENERATIVE_AI_API_KEY") 

if not api_key:
    print("❌ Erro: Chave API não encontrada no .env.")
    exit()

try:
    client = genai.Client(api_key=api_key)
    print("🔎 Buscando modelos disponíveis para chave...")
    
    pager = client.models.list()
    
    encontrou = False
    for model in pager:
        if "generateContent" in model.supported_actions:
            print(f"✅ Modelo disponível: {model.name}")
            encontrou = True
            
    if not encontrou:
        print("⚠️ Nenhum modelo de geração de texto encontrado")

except Exception as e:
    print(f"❌ Erro de conexão: {e}")