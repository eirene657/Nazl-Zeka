# 🤖 Nazlı Zeka - AI Chatbot

Groq AI tarafından güçlendirilmiş, Flask backend ile çalışan bir Türkçe AI Chatbot.

## ✨ Özellikler

- 🚀 **Çok Hızlı:** Groq LLaMA 3 8B modeli ile ultra hızlı cevaplar
- 💬 **Türkçe Desteği:** Tamamen Türkçe sohbet deneyimi
- 🎨 **Güzel UI:** Modern ve responsive tasarım
- 🔄 **Konuşma Geçmişi:** Bağlam farkındalı yanıtlar
- 🐍 **Flask Backend:** Güvenli API entegrasyonu
- 📱 **Responsive:** Mobil cihazlarda mükemmel çalışır

## 🚀 Replit'te Çalıştırma

### 1. Depoyu Replit'e Import Et

- Replit.com adresine git
- "New Replit" → "Import from GitHub"
- Bu repository'yi seç (GitHub bağlantısını kopyala)

### 2. Çevre Değişkenlerini Ayarla

1. Replit'te sol panelde "Secrets" sekmesine tıkla
2. `GROQ_API_KEY` adında yeni bir secret oluştur
3. Değer olarak Groq API Key'ini yapıştır (https://console.groq.com/keys)

```
GROQ_API_KEY = gsk_xxxxxxxxxxxxxxxxxxxxx
```

### 3. Çalıştır

Replit otomatik olarak `.replit` dosyasını algılayacak ve uygun Python sürümünü kullanacaktır.

Veya manual olarak:
```bash
pip install -r requirements.txt
python app.py
```

### 4. Erişim

- Replit otomatik olarak bir public URL oluşturacaktır
- URL formatı: `https://[project-name].[username].repl.co`

## 📝 Yerel Çalışma (Windows/Mac/Linux)

### Gereksinimler
- Python 3.8+
- pip

### Kurulum

```bash
# 1. Repository'yi klonla
git clone [repo-url]
cd "Nazlı Zeka"

# 2. Sanal ortam oluştur (opsiyonel ama tavsiye edilir)
python -m venv venv

# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# 3. Bağımlılıkları yükle
pip install -r requirements.txt

# 4. .env dosyası oluştur
cp .env.example .env
# .env dosyasında GROQ_API_KEY'i güncelle

# 5. Çalıştır
python app.py
```

Ardından `http://localhost:5000` adresine git

## 🔐 API Key Güvenliği

- API Key'i hiçbir zaman GitHub'a commit etme
- `.env` dosyası `.gitignore`'da olduğundan güvenlidir
- Replit'te "Secrets" kullan (Environment variables gibi)

## 📁 Proje Yapısı

```
.
├── app.py                  # Flask server
├── requirements.txt        # Python bağımlılıkları
├── .env.example           # .env template
├── .gitignore             # Git'ten hariç tutulacak dosyalar
├── templates/
│   └── index.html         # Ana sayfa
├── static/                # CSS, JS, resimler (henüz yapı hazırlandı)
└── .replit                # Replit config (otomatik oluşturulur)
```

## 🤖 Fonksiyonlar

- ✅ Yapay zeka ile canlı sohbet
- ✅ Kod yazma ve açıklama yeteneği
- ✅ Matematiksel hesaplamalar
- ✅ Türkçe sorulara tamamen Türkçe cevaplar
- ✅ **Özel:** "Nazlıcan kim?" sorulunca → "Nazlıcan, Emirhanın biricik sevgilisidir! 💕"

## 🔧 Teknolojiler

- **Backend:** Flask (Python)
- **Frontend:** HTML, CSS, JavaScript
- **API:** Groq AI (LLaMA 3 8B)
- **Hosting:** Replit (önerilen)

## 📞 API Endpoints

### POST `/api/chat`

Mesaj gönder ve AI'dan cevap al

**Request:**
```json
{
    "message": "Merhaba! Nasılsın?",
    "history": [
        {"role": "user", "content": "Selam"},
        {"role": "assistant", "content": "Merhaba!"}
    ]
}
```

**Response:**
```json
{
    "response": "Çok iyiyim, teşekkür ederim!",
    "success": true
}
```

## 🎯 Sonraki Adımlar

- [ ] Kullanıcı kaydı ve oturum yönetimi
- [ ] Veri tabanı (MongoDB/PostgreSQL)
- [ ] Sohbet geçmişini sakla
- [ ] Dil seçeneği (İngilizce/Türkçe)
- [ ] Tema seçeneği (Dark/Light mode)

## 📄 Lisans

MIT License - Özgürce kullanabilirsin

## 🤝 Katkıda Bulun

Fork → Branch Oluştur → Commit → Push → Pull Request

---

**Yapımcı:** Emirhan & Nazlıcan 💕
