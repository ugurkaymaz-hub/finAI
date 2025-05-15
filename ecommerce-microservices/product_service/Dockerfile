# Temel image 
FROM python:3.11-slim

# Ortam değişkenleri
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Çalışma dizini oluştur
WORKDIR /src

# Gereksinimleri yükle
COPY requirements.txt .

RUN pip install -r requirements.txt

# Gerekli dosyaları kopyala
COPY . /src 

# Uygulama çalıştırma
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]