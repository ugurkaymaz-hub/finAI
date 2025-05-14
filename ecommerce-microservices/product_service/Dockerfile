# Temel image (Python 3.11 kullanılıyor, senin versiyonuna göre değiştirebilirsin)
FROM python:3.11-slim

# Ortam değişkenleri
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Çalışma dizini oluştur
WORKDIR /app

# Gerekli dosyaları kopyala
COPY ./src /app

# Gereksinimleri yükle
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Uygulama çalıştırma
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]