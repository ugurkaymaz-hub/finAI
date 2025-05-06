# React için Node tabanlı bir imaj
FROM node:18

# Uygulama dizinini ayarla
WORKDIR /app

# package.json ve package-lock.json dosyalarını kopyala
COPY package*.json ./

# Bağımlılıkları yükle
RUN npm install

# Tüm projeyi kopyala
COPY . .

# Uygulama portunu dışa aç
EXPOSE 3000

# Uygulamayı başlat
CMD ["npm", "run", "dev"]