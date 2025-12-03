from google import genai
from google.genai import types
import os
import json
import re

def resume_content_prompt(data, instructions, sec_to_use):
    """
    Create a prompt for generating resume content.
    """
    api_key = os.getenv("GOOGLE_GENERATIVE_AI_API_KEY")
    if not api_key:
        raise ValueError("GOOGLE_GENERATIVE_AI_API_KEY is not set in environment variables.")  
    
    client = genai.Client(api_key=api_key)
    section_string = ", ".join(sec_to_use).upper()
    
    sys_structions = f"""
        Você é um especialista em currículos de TI e sistemas ATS (Applicant Tracking Systems).
        Sua tarefa é adaptar currículos baseado em instruções do usuário.
        REGRAS RÍGIDAS:
        1. Você receberá um JSON de currículo e uma instrução.
        2. Você deve alterar APENAS as seções permitidas: [{section_string}].
        3. Para seções NÃO listadas, mantenha o conteúdo IDÊNTICO ao original.
        4. Responda ESTRITAMENTE com um JSON válido.
    """
    user_data = f"""
        Currículo Original (JSON):
        {json.dumps(data, ensure_ascii=False)}
        
        INSTRUÇÕES DO USUÁRIO:
        {instructions}
        
        GERE UM NOVO CURRÍCULO (JSON) MODIFICADO.
    """

    try:
        resume_content_prompt = client.models.generate_content(
            model="gemini-2.0-flash",
            config=types.GenerateContentConfig(
                system_instruction=sys_structions,
                response_mime_type="application/json",
                temperature=0.7,
            ),
            contents=user_data
        )
        
        raw_text = resume_content_prompt.text
        if "```" in raw_text:
            raw_text = raw_text.replace("```json", "").replace("```", "")
        raw_text = re.sub(r',(\s*[}\]])', r'\1', raw_text)
        
        ai_data = json.loads(raw_text) 
        for key in data.keys():
            if key not in ai_data:
                print(f"⚠️ A IA esqueceu a seção '{key}'. Restaurando original...")
                ai_data[key] = data[key]
            if key == 'skills' and not ai_data[key]:
                 ai_data[key] = data[key]

        return ai_data
    
    except json.JSONDecodeError as e:
        print(f"Error JSON whit IA: {e}")
        print(f"Text: {resume_content_prompt.text}")
        raise RuntimeError(f"Invalid JSON: {e}")
    except Exception as e:
        raise RuntimeError(f"Error generating resume content: {e}")
    
    
    
    