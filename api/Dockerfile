# 1. Usa especificamente a versão 'bullseye' (Debian 11) que é super estável para WeasyPrint
FROM python:3.10-bullseye

# 2. Configurações de ambiente para evitar erros de interação
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 3. Instala as dependências do sistema
# No Bullseye, esses nomes de pacotes são garantidos de existir
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    python3-dev \
    python3-pip \
    python3-cffi \
    libcairo2 \
    libpango-1.0-0 \
    libpangocairo-1.0-0 \
    libgdk-pixbuf2.0-0 \
    libffi-dev \
    shared-mime-info \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# 4. Define a pasta de trabalho
WORKDIR /app

# 5. Copia os arquivos (Como seu repo é isolado, copia da raiz)
COPY . .

# 6. Atualiza o pip e instala os requirements
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# 7. Expõe a porta
EXPOSE 5000

# 8. Comando de inicialização
ENV FLASK_APP=run.py
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "run:app"]