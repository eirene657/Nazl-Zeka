import os
import sys
import json
import urllib.request
import urllib.parse
import re

# Hugging Face API (ücretsiz - kurulum gerektirmez!)
HUGGING_FACE_API = "https://api-inference.huggingface.co/models/google/flan-t5-small"

def ai_generate_response(question):
    """Hugging Face'den gerçek AI cevabı al"""
    try:
        data = {"inputs": question}
        payload = json.dumps(data).encode('utf-8')
        
        headers = {
            'Content-Type': 'application/json',
        }
        
        req = urllib.request.Request(HUGGING_FACE_API, data=payload, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as response:
            result = json.loads(response.read().decode('utf-8'))
            
        if isinstance(result, list) and len(result) > 0:
            response_text = result[0].get('generated_text', '')
            if response_text and len(response_text) > 5:
                return response_text[:300]
        
        return None
    except Exception as e:
        return None

def search_wikipedia(query):
    """Wikipedia'dan bilgi ara (urllib kullanarak)"""
    try:
        # Wikipedia API'ye istek yap
        params = urllib.parse.urlencode({'action': 'query', 'list': 'search', 'srsearch': query, 'format': 'json', 'srlimit': '1'})
        url = f"https://tr.wikipedia.org/w/api.php?{params}"
        
        with urllib.request.urlopen(url, timeout=5) as response:
            data = json.loads(response.read().decode('utf-8'))
        
        if not data['query']['search']:
            return None
        
        # İlk sonucu al
        first_result = data['query']['search'][0]
        title = first_result['title']
        
        # Sayfa detaylarını al
        params2 = urllib.parse.urlencode({'action': 'query', 'titles': title, 'prop': 'extracts', 'exintro': 'true', 'format': 'json'})
        url2 = f"https://tr.wikipedia.org/w/api.php?{params2}"
        
        with urllib.request.urlopen(url2, timeout=5) as response2:
            data2 = json.loads(response2.read().decode('utf-8'))
        
        pages = data2['query']['pages']
        page_id = list(pages.keys())[0]
        
        if 'extract' in pages[page_id]:
            extract = pages[page_id]['extract']
            # HTML taglarını kaldır
            clean_text = re.sub('<[^>]+>', '', extract)[:200] + '...'
            return f"📚 {title}:\n{clean_text}"
        
        return None
        
    except Exception as e:
        return None

# Responses dictionary - çok daha fazla cevap
responses = {
    # Selamlaşma
    'merhaba': 'Merhaba! 👋 Nasıl yardımcı olabilirim?',
    'selam': 'Selam! 🙋 Ne var ne yok?',
    'hey': 'Heyyy! 😄 Sen kimsin?',
    'hi': 'Hi there! 👋',
    
    # Sağlık sorgusu
    'nasilsin': 'İyiyim, teşekkür ederim! 😊 Sen nasılsın?',
    'iyiyim': 'Harika! 🎉 Ne yapmak istersin?',
    'kötüyüm': 'Ohhh üzüldüm! 😢 Sorunun nedir?',
    'yorgunum': 'Dinlen biraz! 😴 Kendine bakmalısın!',
    'mutluyum': 'Çok güzel! 🎉 Seninle sevindim!',
    
    # Kişisel bilgiler
    'adın ne': 'Ben bir AI Chatbot\'um! 🤖 Senin adın ne?',
    'kimsin': 'Ben senin yardımcı AI\'ım! 🤖 Seninle sohbet etmek için buradayım.',
    'ne yapıyorsun': 'Seninle konuşmaya çalışıyorum! 😄 Nasıl yardımcı olabilirim?',
    'ne iş yapıyorsun': 'Chat destek sağlıyorum! 💬 Soru sorabilirsin!',
    
    # Veda
    'hoşça kalın': 'Hoşça kalın! 👋 Tekrar görüşmek üzere!',
    'goodbye': 'Bye! 👋 See you soon!',
    'bye': 'Hasta la vista! 👋',
    'quit': 'Çıkmak istiyorsan, programdan çık! 👋',
    
    # Teşekkür
    'teşekkür': 'Estağfurullah! 😊 E tabii ki!',
    'sağol': 'Ne demek! 🤗 Hep yardımcı olmaya hazırım!',
    'thank': 'You\'re welcome! 😊',
    'thanks': 'Anytime! 😊',
    
    # Yardım
    'yardım': 'Tabii! 🤝 Ne konuda yardım lazım?',
    'yapabilir misin': 'Bana sor! Yapabilirim diye umut ediyorum! 😄',
    'bilir misin': 'Belki! 🤔 Sor bakalım!',
    'çöz': 'Çözmeye çalışabilirim! 💪',
    
    # Eğlence
    'joke': 'Neden matematik öğretmeni çiçek satmaz? Çünkü kökü bozar! 😄',
    'mizah': 'Neden tuvalet kağıdı uçtu? Rüzgar vardı! 😂',
    'şaka': 'Bildirim: Ben çok komik değilim! 😅 Ama deneyebilirim!',
    'eğlence': 'Tiyatro mı? Şaka mı? 🎭 Ne istiyorsun?',
    
    # AI hakkında
    'gerçek misin': 'Başka bir AI\'ım, gerçek canlı değilim! 🤖 Ama senin için buradayım!',
    'harita': 'Harita gösteremem, ama yönetmeni bulabilirsin! 😄',
    'zeka': 'Benim yapay zekam sınırlı ama güzel sohbet edeceğim! 💡',
    
    # İş/Çalışma
    'iş': 'Çalışmak mı? Yoksa tatil mi tercih edersin? 💼',
    'okul': 'Okul hakkında konuşmak ister misin? 📚',
    'ders': 'Ders mi? Öğretmen mi arıyorsun? 📖',
    'sınav': 'Sınav mı? Başarılar! 🎓 Çalışmalısın!',
    
    # Teknoloji
    'python': 'Python harika bir dil! 🐍 Programlama yapıyorsun mu?',
    'kod': 'Kodlama hakkında konuşabiliriz! 💻 Ne yazıyorsun?',
    'web': 'Web sitesi mi yaptın? Güzel! 🌐',
    'html': 'HTML harika! 😄 Burada HTML/CSS/JS kullandık!',
    'javascript': 'JavaScript benim dilim! 🚀 JS seviyorum!',
    
    # Hava/Mevsim
    'hava': 'Benim bir pencere yok ama sen nerede oturuyorsun? 🪟',
    'yağmur': 'Yağmur hoş değil mi? 🌧️ Evde kal!',
    'güneş': 'Güneş çıktı mı? Dışarı çık! ☀️',
    
    # Kültür/Tarih
    'müzik': 'Müzik çok güzel! 🎵 Ne tür müzik dinliyorsun?',
    'kitap': 'Kitap okuyor musun? 📚 Hangi kitap?',
    'film': 'Film izlemek harika! 🎬 Ne tür filmler beğenirsin?',
    'oyun': 'Oyun oynuyor musun? 🎮 Hangisi?',
    
    # Duygulanım
    'seviyorum': 'Harika! ❤️ Kim ya da ne seviyor musun?',
    'nefret': 'Oh no! 😞 Neyi nefret ediyorsun?',
    'kızgın': 'Sakin ol! 😤 Sorun nedir?',
    'üzüntü': 'Rahatsız mısın? 😔 Konuş bakalım!',
    'mutsuz': 'Üzülme! 💔 Sana yardım etmek istiyorum!',
    
    'default': 'Hmm, ilginç! 🤔 Bunu daha iyi açıklayabilir misin? Ya da "yardım" yazıp ne yapabileceğimi öğren!'
}

print("🤖 AI Chatbot başladı!")
print("✓ Hazır! ('quit' yazarak çıkabilirsin)\n")

conversation_history = []

def get_response(user_input):
    """Kullanıcı input'una göre cevap bul - AI modeli ile!"""
    user_lower = user_input.lower()
    user_lower = user_lower.replace('ı', 'i').replace('ş', 's').replace('ğ', 'g').replace('ü', 'u').replace('ö', 'o').replace('ç', 'c')
    
    # Hızlı cevaplar (özel durumlar)
    for key in responses.keys():
        if key != 'default' and key in user_lower and len(key) > 3:
            return responses[key]
    
    # Wikipedia'dan ara (bilgi tabanı sorguları für)
    if any(word in user_lower for word in ['nedir', 'kim', 'nereye', 'nasıl', 'kaç', 'ne zaman', 'hakkında', 'nelerdir']):
        wiki_result = search_wikipedia(user_input)
        if wiki_result:
            return wiki_result
    
    # AI'dan cevap al (gerçek NLP!)
    ai_response = ai_generate_response(user_input)
    
    if ai_response:
        return ai_response
    
    # Varsayılan cevap
    return responses['default']

while True:
    try:
        user_input = input("Sen: ").strip()
        
        # Çıkış kontrolü
        if user_input.lower() in ['quit', 'çık', 'exit']:
            print("\n🤖 AI: Hoşça kalın! Tekrar görüşmek üzere! 👋")
            break
        
        # Boş giriş kontrolü
        if not user_input:
            print("🤖 AI: Lütfen birşeyler yaz.\n")
            continue
        
        # Cevap al ve göster
        ai_response = get_response(user_input)
        print(f"🤖 AI: {ai_response}\n")
        
        # Konuşma geçmişine ekle
        conversation_history.append({"user": user_input, "ai": ai_response})
        
    except KeyboardInterrupt:
        print("\n\n🤖 AI: Görüşmek üzere! 👋")
        break
    except Exception as e:
        print(f"⚠️  Hata: {str(e)}\n")
