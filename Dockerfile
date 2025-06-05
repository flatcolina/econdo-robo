FROM python:3.10-slim

# Instala dependências do sistema
RUN apt-get update && apt-get install -y \
    wget unzip curl gnupg2 default-jdk xvfb \
    chromium chromium-driver

ENV PATH="/usr/lib/chromium/:$PATH"

WORKDIR /app
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]