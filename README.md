#  🛍️ E-Commerce Microservices Platform

Bu proje, mikroservis mimarisiyle inşa edilmiş bir e-ticaret platformunun temel yapısını oluşturmaktadır. Her servis bağımsız olarak geliştirilmiş olup, kullanıcı yönetimi, ürün işlemleri, kimlik doğrulama, alışveriş ve admin paneli gibi işlevleri hedeflemektedir.

> 🚧 **Proje geliştirme aşamasındadır.** Yeni özellikler eklenmekte ve sistem test edilmektedir.

---

## 🔧 Proje Yapısı

```
FinAI-E-Marketting/
│
├── gateway/                     # Tüm isteklerin geçtiği merkezi yönlendirici (API Gateway)
│   ├── app/
│   │   ├── middlewares/         # JWT doğrulama, hata yönetimi gibi ara yazılımlar
│   │   ├── routes/              # Servislere yönlendiren route dosyaları
│   │   └── utils/               # Yardımcı fonksiyonlar
│   ├── main.py                  # Gateway uygulama giriş noktası
│   ├── config.py                # Ayar ve yapılandırmalar
│   └── Dockerfile               # Docker yapılandırması
│
├── user_service/                # Kullanıcı servisi
│   ├── app/
│   │   ├── controllers/         # FastAPI endpoint tanımları
│   │   ├── services/            # İş mantığı
│   │   ├── repositories/        # Veritabanı işlemleri
│   │   ├── models/              # SQLAlchemy modelleri
│   │   ├── schemas/             # Pydantic şemaları (request/response için)
│   │   └── core/                # config.py, database.py, security.py vb. yapılandırmalar
│   ├── main.py                  # FastAPI uygulama başlatıcısı
│   └── Dockerfile               # Docker yapılandırması
│
├── product_service/             # Ürün, sepet, sipariş işlemleri (devam ediyor)
│   └── app/                     # Yapısı user_service ile paralel olacak
│
├── frontend/                    # React tabanlı kullanıcı arayüzü (devam ediyor)
│   └── src/                     # Sayfalar, bileşenler, stiller vs.
│
├── docker-compose.yml           # Tüm servisleri bir araya getiren Docker Compose dosyası
└── README.md                    # Proje tanıtım ve dokümantasyonu
```

## 🧩 Kullanılan Teknolojiler

-   **Backend (FastAPI)** – Mikroservislerin hızlı geliştirilmesi
-   **Frontend (React.js)** – Modern SPA yapısı
-   **Docker & Docker Compose** – Ortam bağımsız servis orkestrasyonu
-   **PostgreSQL** – Veritabanı
-   **SQLAlchemy** – ORM katmanı
-   **JWT Authentication** – Güvenli kullanıcı doğrulama
-   **Pydantic** – Veri doğrulama ve şema tanımları
-   **Nginx (opsiyonel)** – Ters proxy ve frontend sunumu (planlanıyor)

---

## ✅ Şu Ana Kadar Yapılanlar

### 🧍‍♂️ `user_service`

-   [x] Kullanıcı oluşturma
-   [x] Giriş / çıkış
-   [x] JWT ile kimlik doğrulama
-   [x] Roller ve yetkilendirme
-   [x] Adres yönetimi
-   [x] Token doğrulama endpoint’i

### 📦 `product_service`

-   [x] Ürün CRUD işlemleri
-   [x] Kategori yönetimi
-   [x] Stok ve fiyat yönetimi
-   [ ] Sepet işlemleri (devam ediyor)
-   [ ] Sipariş geçmişi (planlanıyor)

### 🌐 `gateway`

-   [x] Gelen istekleri doğru servise yönlendirme
-   [x] JWT kontrolü (doğrulama ve rol kontrolü)
-   [ ] Hata yönetimi ve loglama (planlanıyor)

### 🖥️ `frontend`

-   [x] Kullanıcı girişi/kayıt ekranı
-   [x] Ürün listeleme
-   [ ] Sepet ve ödeme sayfası (geliştiriliyor)
-   [ ] Admin panel (planlanıyor)

---

## 🚀 Kurulum

> Docker yüklü olmalıdır.

```bash
git clone https://github.com/ugurkaymaz-hub/finAI.git
cd ecommerce-microservices
docker-compose up --build
```

## 👤 Test Kullanıcısı

username : superuser  
password : superuser12345

---

