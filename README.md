# 📄 CV Craft - AI Powered Resume Builder

![Project Status](https://img.shields.io/badge/status-active-green)
![License](https://img.shields.io/badge/license-MIT-blue)

> **Nota:** Este é um projeto de uso pessoal desenvolvido para automatizar a personalização do meu próprio currículo. Embora o código seja aberto, a aplicação foi arquitetada para atender aos meus dados específicos (JSON).

## 🎯 O Problema
Como desenvolvedor, aplicar para múltiplas vagas exige adaptar o currículo para cada Job Description (JD) para passar pelos filtros de ATS (Applicant Tracking Systems). Fazer isso manualmente no Word/Docs é lento e propenso a erros de formatação.

## 💡 A Solução
O **CV Craft** é uma aplicação Full Stack que utiliza Inteligência Artificial (Google Gemini) para reescrever seções estratégicas do currículo (Resumo e Skills) com base na descrição da vaga, gerando um PDF formatado profissionalmente em segundos.

## 🛠️ Tech Stack

### Front-End (Vercel)
- **React + Vite:** Performance e desenvolvimento rápido.
- **TypeScript:** Tipagem estática para evitar erros de runtime.
- **ShadCn UI + Tailwind CSS:** Interface minimalista, acessível e Mobile-First.
- **Axios:** Comunicação com a API e manipulação de Blobs (PDF).

### Back-End (Render)
- **Python + Flask:** API RESTful leve e eficiente.
- **WeasyPrint:** Engine de renderização de PDF de alta fidelidade (HTML/CSS -> PDF).
- **Google Gemini API (1.5 Flash):** LLM para análise semântica e reescrita de texto.
- **Docker:** Containerização necessária para gerenciar as dependências de sistema do WeasyPrint (GTK3, Pango) no ambiente de produção.

## 🚀 Funcionalidades

- **Otimização via IA:** Analisa a vaga e adapta o "Resumo" e as "Habilidades" para dar match com as palavras-chave.
- **Merge de Segurança:** Garante que a IA nunca alucine ou remova seções críticas (Experiência, Educação) se elas não forem o foco da edição.
- **Geração de PDF em Tempo Real:** O Backend renderiza um PDF limpo, pronto para impressão ou upload.
- **Mobile First:** Interface pensada para ser usada no celular enquanto navega pelo LinkedIn.
- **Preview Instantâneo:** Visualização do PDF gerado antes do download.

## 📐 Arquitetura

O projeto utiliza uma arquitetura híbrida para lidar com a complexidade da geração de PDFs:

1.  **Frontend (Vercel):** Envia o JSON atual do currículo + Instruções da vaga.
2.  **API (Render/Docker):**
    * Recebe o payload.
    * Consulta o **Google Gemini** para reescrever os textos.
    * Valida e sanitiza o JSON de retorno (Regex + Fallbacks).
    * Injeta os dados em um template Jinja2.
    * Usa **WeasyPrint** para gerar o binário do PDF.
3.  **Client:** Recebe o Blob e força o download ou preview.

## 📦 Como Rodar Localmente

### Pré-requisitos
- Node.js & npm
- Python 3.10+
- GTK3 (necessário para o WeasyPrint no Windows/Mac)

### 1. Back-End
```bash
cd api
python -m venv .venv
source .venv/bin/activate # ou .venv\Scripts\activate no Windows
pip install -r requirements.txt

# Crie um arquivo .env com:
# GOOGLE_GENERATIVE_AI_API_KEY=sua_chave_aqui

python run.py
```
2. Front-End
```Bash

cd web
npm install

# Crie um arquivo .env com:
# VITE_API_URL=http://localhost:5000/api

npm run dev
```
## ⚠️ Disclaimer
Este projeto foi desenhado para uso pessoal. O sistema espera uma estrutura JSON específica (resume.json) que contém meus dados de carreira. O objetivo deste repositório é demonstrar minhas habilidades em:

Integração de LLMs em aplicações reais.

Manipulação de arquivos binários e geração de documentos.

DevOps básico (Docker, CI/CD manual via Render/Vercel).

## 📬 Contato

Se você gostou deste projeto ou quer trocar uma ideia sobre desenvolvimento Full Stack, IA ou DevOps, pode me encontrar aqui:

**Flávio Oliveira Silva Júnior** 📍 Parnamirim, RN  
📧 **Email:** [flavinhoolvs@gmail.com](mailto:flavinhoolvs@gmail.com)  
🌐 **Portfólio:** [flavinho-personal-dev.vercel.app](https://flavinho-personal-dev.vercel.app/)  
🔗 **LinkedIn:** [linkedin.com/in/flaviojrz](https://www.linkedin.com/in/flavinhojr/) 

---
Feito com ☕ e Python por **Flávio Oliveira**.
