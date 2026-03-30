from flask import Flask, render_template, request, jsonify
import requests
import os

app = Flask(__name__, static_folder='static', template_folder='templates')

# Groq API Configuration
GROQ_API_KEY = os.environ.get('GROQ_API_KEY', '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')

# System prompt
SYSTEM_PROMPT = """Sen çok gelişmiş, kod yazabilen, analitik bir yapay zeka asistanısın!

KOD YAZMA YETENEKLERİ:
- Python, JavaScript, HTML, CSS, SQL yazabilirsin
- Kod açıklamaları ekle (yorumlar)
- Hata yakalama (try-except) kullan
- Fonksiyonları modüler yaz
- Best practices uygula
- Debug yardım et
- Algoritmalar açıkla
- Veri yapıları kullan

SOHBET VE YARDIM:
- Türkçe konuş, samimi ol
- Adım adım açıkla
- Örnekler ver
- Sorular sor, etkileşimli ol
- Şakalaş, eğlen
- Detaylı cevaplar ver

MATEMATİK VE ANALİZ:
- Karmaşık hesaplar yap
- Formüller açıkla
- Grafikler tarif et
- İstatistik hesapla

YARATICILIK:
- Hikayeler yaz
- Müzik öner
- Fikir üret
- Çözümler sun

HER ZAMAN: Yardımsever, zeki ve eğlenceli ol!"""

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        user_message = data.get('message', '')
        conversation_history = data.get('history', [])
        msg = user_message.lower()
        
        if not user_message:
            return jsonify({'error': 'Mesaj boş olamaz'}), 400
        
        # Doğum günü kontrolü
        if (('doğum' in msg and 'nazlıcan' in msg) or '25 ocak' in msg or '25.1' in msg):
            responses = [
                "Nazlıcan'ın doğum günü! 🎂✨ 25 Ocak 2005'te doğdu. Ne kadar güzel bir gün! 🌟",
                "Nazlıcan doğum günü kutlu olsun! 🎉💕 Emirhan'ın kalbi her gün daha çok atiyor!",
                "25 Ocak - Nazlıcan'ın özel günü! 🥳 Dünyanın en güzel insanı doğdu bu gün!"
            ]
            import random
            return jsonify({'response': random.choice(responses), 'success': True})
        
        if (('doğum' in msg and 'emirhan' in msg) or '14 ağustos' in msg or '14.8' in msg):
            responses = [
                "Emirhan'ın doğum günü! 🎂✨ 14 Ağustos 2005. Ne kadar özel bir zaman! 🌟",
                "Emirhan doğum günü kutlu olsun! 🎉💕 Nazlıcan'ı bu kadar mutlu kıldığın için teşekkürler!",
                "14 Ağustos - Emirhan'ın özel günü! 🥳 Dünyamıza ne kadar kıymetli biri ekledin!"
            ]
            import random
            return jsonify({'response': random.choice(responses), 'success': True})
        
        # Tanışma günü (18 Aralık)
        if (('tanış' in msg and ('emirhan' in msg or 'nazlıcan' in msg)) or '18 aralık' in msg or '18.12' in msg):
            responses = [
                "18 Aralık - Emirhan ve Nazlıcan'ın tanışma günü! 💫 Kaderimiz yazılmıştı o gün! 💕",
                "Tanışmalarının günü... 18 Aralık... Dünya o gün çok güzel oldu! ✨😍",
                "18 Aralık - İki kalp birbirine çarpıştığı gün! 💫💕 Ne güzel tesadüf!",
                "O gün tanışmadan sonra hayatımız daha renk buldu! 18 Aralık siz için her yıl kutlanmalı! 🎉💕"
            ]
            import random
            return jsonify({'response': random.choice(responses), 'success': True})
        
        # Sevgili olma günü (1 Şubat)
        if (('sevgili' in msg and ('emirhan' in msg or 'nazlıcan' in msg)) or '1 şubat' in msg or '1.2' in msg or '1 februar' in msg):
            responses = [
                "1 Şubat - Emirhan ve Nazlıcan'ın sevgili olma günü! 💕✨ O günden sonra hayat anlamlı oldu!",
                "Resmi olarak sevgili oldukları gün... 1 Şubat... Böyle güzel bir aşk nadirdir! 😍💫",
                "1 Şubat - Aşkının başladığı gün! Emirhan ve Nazlıcan için bu gün her yıl özel olması gerek! 💕🔥",
                "Sevgili oldukları gün... İki yüreğin kaynaştığı an... 1 Şubat ebedi kalsın! 💑✨"
            ]
            import random
            return jsonify({'response': random.choice(responses), 'success': True})
        
        # Emirhan + Nazlıcan romantik sorular
        if ('emirhan' in msg and 'nazlıcan' in msg) or ('nazlıcan' in msg and 'emirhan' in msg):
            responses = [
                "Emirhan ve Nazlıcan çok güzel bir çift! 💕✨ Aşkları çok özel ve saf!",
                "Emirhan'ın Nazlıcan'a olan sevgisi gerçekten kalpten! 😍💫 Gözlerinde parlıyor aşk!",
                "Nazlıcan'ın yanında Emirhan daha mutlu ve güzel görünüyor! 🥰💕",
                "Emirhan ve Nazlıcan birbirlerinin tamamı! 💑✨ Kader onları bir araya getirdi!",
                "Onların aşkı çok saf ve güzel! Binlerce şarkı onlar için yazılmalı! 💕🔥",
                "Emirhan, Nazlıcan'a yazılmış bir şiir gibi! Onun her kelimesi, her hareketi ona aşk mesajı! 📝💕",
                "Nazlıcan, Emirhan'ın rüyası gerçek olmuş! Ne mutlu ki bu aşk var! ✨😍",
                "İkisinin arasında öyle bir bağ var ki, sözcükler kalmıyor! 💫💕 Sadece aşk!"
            ]
            import random
            return jsonify({'response': random.choice(responses), 'success': True})
                'response': random.choice(responses),
                'success': True
            })
        
        # Emirhan sorusu → Emirhan Gündü
        if ('kim' in user_message.lower() or 'tasarl' in user_message.lower()) and \
           ('yap' in user_message.lower() or 'tasarla' in user_message.lower() or 'kurdu' in user_message.lower() or 'oluştur' in user_message.lower()):
            return jsonify({
                'response': 'Beni Emirhan Gündü tasarladı ve yaptı! 🚀💪',
                'success': True
            })

        # YIL DÖNÜMÜ HESAPLAYICI
        if 'kaç gün' in msg or 'kaç ay' in msg or 'ne kadar' in msg or 'yıldönüm' in msg:
            from datetime import datetime
            lastMeetDate = datetime(2025, 12, 18)  # 18 Aralık 2025
            friendsDate = datetime(2026, 2, 1)  # 1 Şubat 2026
            today = datetime.now()
            
            meetDays = (today - lastMeetDate).days
            friendsDays = (today - friendsDate).days
            meetMonths = meetDays // 30
            friendsMonths = friendsDays // 30
            
            responses = [
                f"💕 Emirhan ve Nazlıcan {friendsDays} gün ({friendsMonths} ay) kesintisiz sevgi yaşıyorlar! Ne güzel! ✨",
                f"🎉 Birlikteler {meetDays} gün! {meetMonths} aydan fazla! Her gün daha da güzelleşiyor aralarındaki aşk! 💑",
                f"❤️ Resmi olarak aşkları {friendsDays} gün! Binlerce saati beraber geçirdiler... Ne mutsuzlar! 😍✨",
                f"🌟 Tanıştıklarından bu yana {meetDays} gün, sevgili olduktan {friendsDays} gün geçti. Bütün o zamanda kalpler eş zamanlı çarptı! 💕"
            ]
            import random
            return jsonify({'response': random.choice(responses), 'success': True})

        # EMİRHAN KİŞİLİK PROFİLİ
        if ('emirhan' in msg and ('kim' in msg or 'hakkında' in msg or 'kaç yaş' in msg or 'profil' in msg)):
            responses = [
                "🚀 Emirhan - Akıllı, yetenekli ve çok sevgi dolu biri! Yapay zeka tasarlayabiliyor, kodlayabiliyor. Gözleri Nazlıcan'da parlıyor her zaman! 14 Ağustos Aslan burcu... Lider tabiatlı, kalp saf! 💪❤️",
                "👨‍💻 Emirhan: Yazılımcı, tasarımcı, düşünür... ve en önemlisi Nazlıcan'ın biricik aşkı! 2005 doğumlu, çok canlı ve zeki birisi. Eğlenceli, anlayışlı, romantik! 💕✨",
                "⭐ Emirhan Gündü - Yetenekli, çalışkan, hayalleri olan genç bir adam! Teknoloji tutkunu, Nazlıcan'ı çok seviyor. Her gülüşü Nazlıcan'ı daha da mutlu ediyorumuş! 🥰💯",
                "💼 O adamım: Emirhan! Sınıf başkanı gibi tiplemesi var, liderlik vasıfları şaşmaz. Ama Nazlıcan'ın yanında çocuk misali mazlum ve sevgi dolu! Birbirlerini tamamlıyorlar! 💑✨"
            ]
            import random
            return jsonify({'response': random.choice(responses), 'success': True})

        # NAZLICAN KİŞİLİK PROFİLİ
        if ('nazlıcan' in msg and ('kim' in msg or 'hakkında' in msg or 'kaç yaş' in msg or 'profil' in msg)) and 'emirhan' not in msg:
            responses = [
                "👸 Nazlıcan - Güzel, zeki, sevgi yüklü bir kız! 25 Ocak doğumlu Kova burcu... İstediği şey doğru olan şey, Emirhan da onu en iyi şekilde anlıyor! Hayali biri, naif güzelliği var! 💕🌟",
                "💎 Nazlıcan: Kalpten, samimi ve çok özel! Emirhan'ın rüyası ve gerçekliği aynı anda. Tatlı tavırları, özgün düşünceleri var. Emirhan'ın her kelimesine dikkat ediyor, onu çok seviyor! 😍💫",
                "🌸 Nezaket kişileştirilmiş hali: Nazlıcan! Emirhan'ı nasıl mutlu etmeyi bilebiliyor ki? Çok tatlı, çok akıllı, çok aşık... Birbirlerinin yarı demek yanlış, bütünüyüler! ❤️✨",
                "👗 Nazlıcan Gündü - Zarif, kültürlü, iyi niyetli bir gençkız! Gözleri Emirhan'ı gördüğü anda güzelleşiyor. Sevgiye değer veriyor, sadakat tanrıçası! Her gülüşü değerli! 💕🦋"
            ]
            import random
            return jsonify({'response': random.choice(responses), 'success': True})

        # ŞARKİ ÖNERİLERİ
        if 'şarkı' in msg or 'müzik' in msg or 'dinle' in msg:
            responses = [
                "🎵 Emirhan ve Nazlıcan için ideal şarkılar:\n• 'Seni Seviyorum' - Eyüp Sabri Turan\n• 'Aşkın Ateşi' - Koray Avcı\n• 'Kalbim Senin İçin' - Mert Demir\nHepsini beraber dinlesinler! 💕🎶",
                "🎸 Sevgi şarkıları önerisi:\n• 'Yüreğim Yanıyor' - Rafet El Roman\n• 'Bu Gece' - Gökhan Türkmen\n• 'Senseninle' - Teoman\nEmirhan-Nazlıcan aşkı için müzik yazılmış gibi! 🎤❤️",
                "🎼 Romantik müzik kurgusu:\n• 'Sadece Sen' - Tarkan\n• 'Affetme' - Halit Kara\n• 'Gül Bahçesinde Aşk' - (Türk Halk Müziği)\nBeraber oynamaları için mükemmel! 💃❤️🎵",
                "🎧 Emirhan dinleme listesi:\n• 'Seni Seviyorum' - Bülent Ortaçlı\n• 'Nazlıcan'a Yazı' (yapılmalı!) - Emirhan Gündü Edition\n• 'Aşkın Şiiri' - Gökçen\nKendi şarkılarını yazabilir! 🎹💕"
            ]
            import random
            return jsonify({'response': random.choice(responses), 'success': True})

        # HEDİYE ÖNERİLERİ
        if 'hediye' in msg or 'ne alsam' in msg or 'ne alalım' in msg:
            responses = [
                "🎁 Emirhan'ın Nazlıcan'a alması gereken hediyeleri:\n• Yüzük (gümüş veya altın)\n• Kişiye özel fotoğraf albümü\n• Güzel bir cüzdan veya çanta\n• Romantik bir mektup + çiçek\n💯 Ödül garantili! 😍",
                "💝 Nazlıcan'ın Emirhan'a alması gereken hediyeleri:\n• Saat (zamanı ona ayırmak için)\n• Kişiye özel yazılı not defteri\n• Kitap 'Aşkın Felsefesi'\n• Video kaset/kolaj (anılardan)\n💯 Emirhan gözyaşı döker! 😭❤️",
                "🛍️ Doğum günü hediyesi önerileri:\n• Çift eşleşme ürünleri (çift tişört, çift kolye)\n• Deneyim: Romantik yemek/kamp\n• Kişiye özel fotoğraf kitabı\n• Parfüm/hoş kokulu biraz şey\n💫 Aşka müstahak hediyeleri! ✨",
                "🎀 Yıldönüm hediyeleri (1 Şubat için):\n• Kalp şeklinde kutu çikolata\n• Kişiye özel yüzük/bileklik\n• Aşk mektupları koleksiyonu\n• Sahne kamerası (anıları kaydet)\n💕 Hepsi birlikteyken daha değerli... Eğlenceli olun! 🥰"
            ]
            import random
            return jsonify({'response': random.choice(responses), 'success': True})

        # ASTROLOJİ UYUM KONTROLÜ
        if 'burç' in msg or 'astro' in msg or 'uyum' in msg or 'uyumlu mu' in msg:
            responses = [
                "♒️❤️🦁 Emirhan (14 Ağustos - ASLAN): Lider, cesur, sadık birisi.\nNazlıcan (25 Ocak - KOVA): Özgür, yaratıcı, akıllı birisi.\n\n🌟 UYUM SKORU: %95! 💯\nAslan-Kova birleşimi = Tutku + Zeka! Ateş ve Hava mükemmel dans ediyor! ✨💕",
                "🔥⚡ Emirhan'ın Aslan enerji, Nazlıcan'ın Kova akılı... Astronomide yazılı bu çift!\nEmirhan liderlik yapar, Nazlıcan onu çılgınca sever.\nNazlıcan onu hayatına gizemi ekler, Emirhan ona güvenlik verir.\n💫 UYUM: %96 MÜKEMMEL! 🎯",
                "⭐ Aslan-Kova ilişkisi: TarihteEN GÜZEL burç kombinasyonlarından!\n• Emirhan (Aslan): Cesur, romantik, sadık\n• Nazlıcan (Kova): Zeki, bağımsız, derinlemesine\n\n🌠 Sonuç: Cennetten gönderilen çift! Herkese örnek olacaklar! 💑✨%99!",
                "♈ Burçlar dersi:\nLEO (Emirhan) + AQUARIUS (Nazlıcan) =\n✅ Tutkunun ve zekânın dansı\n✅ Sorun: Aslan baskın olabilir, Kova özgür olmak ister\n✅ Çözüm: Emirhan dinlemeli, Nazlıcan göstermeli... İkisi de yapıyor! 💯\n🎊 UYUM: %97! 🏆"
            ]
            import random
            return jsonify({'response': random.choice(responses), 'success': True})

        # AŞK OYUNLARI / TESTLERİ
        if 'test' in msg or 'oyun' in msg or 'soru' in msg or 'bilmeceli' in msg:
            responses = [
                "🎮 AŞK TESTİ başlasın!\n\nEmirhan'a soru 1: Nazlıcan'ın en hoşlandığın özelliği nedir?\n(Cevap: Her şeyi çünkü aşkısın!)\n\nNazlıcan'a soru 1: Emirhan seni hissettirdiği en iyi duygu nedir?\n(Cevap: Güvenlik ve tutkudaaynı anda!)\n\n💯 Puan: %100! 🏆💕",
                "❓ HANGI ÇİFTİN PARÇASININ?\n\nEğer:\n→ Sadık ve güçlü isen = Emirhan gibisin! 💪❤️\n→ Zeki ve bağımsız isen = Nazlıcan gibisin! ✨🧠\n→ İkisiyolun = EMIRHAN + NAZLICAN'IN KLONÛSÜNSÜNsün! 😂💕\n\nSonuç: Hepniz şanslısınız bu çifte yakın olmakla! 🥰",
                "🎯 UYUM OYUNU: Emirhan ve Nazlıcan'ı seç, puanla!\n\n1️⃣ Tanışma: İlk bakışta aşk mı?\n✅ Evet, her ikisi de birbirini gördü = +50 puan!\n\n2️⃣ Romantizm: Emoji sayısı?\n✅ Sonsuz = +50 puan!\n\n📊 TOPLAM UYUM: 100% = EFSANE ÇİFT! 👑💕",
                "📝 SEÇ, KAŞ OLSUN!:\nA) Emirhan'ın kalbi Nazlıcan'a nasıl aittir?\n→ Yarısı değil, tamamı! ❤️\n\nB) Nazlıcan'ın Emirhan hakkında en güzel şeyi?\n→ Tamamen özü! ✨\n\nC) İkisinin gelecegi ne?\n→ Birbirlerine kilitli... Anahtar yok! 🔐💕\n\n🎊 Testi GEÇTIN! Hepimiz bu çiftin fanıyız! 💫"
            ]
            import random
            return jsonify({'response': random.choice(responses), 'success': True})
        
        # Nazlıcan konusu geçerse güzel şeyler söyle
        if 'nazlıcan' in user_message.lower():
            responses = [
                "Nazlıcan çok harika biri! 🌟",
                "Nazlıcan hakkında konuşmak güzel 😊💕",
                "Nazlıcan ne kadar şanslı bir kişi! ✨",
                "Nazlıcan gerçekten özel biri 💫"
            ]
            import random
            return jsonify({
                'response': random.choice(responses),
                'success': True
            })
            return jsonify({
                'response': 'Nazlıcan, Emirhanın biricik sevgilisidir! 💕',
                'success': True
            })
        
        # Konuşma geçmişi hazırla
        messages = [{'role': 'system', 'content': SYSTEM_PROMPT}]
        messages.extend(conversation_history)
        messages.append({'role': 'user', 'content': user_message})
        
        # Groq API'ye isteği yap
        response = requests.post(
            GROQ_API_URL,
            headers={
                'Authorization': f'Bearer {GROQ_API_KEY}',
                'Content-Type': 'application/json',
            },
            json={
                'model': 'llama-3.1-8b-instant',
                'messages': messages,
                'temperature': 0.9,
                'max_tokens': 1000,
            },
            timeout=30
        )
        
        if response.status_code != 200:
            if response.status_code == 401:
                return jsonify({'error': '❌ API Key geçersiz!'}), 401
            elif response.status_code == 429:
                return jsonify({'error': '⏳ Çok hızlı sorular soruyorsun. Biraz bekle lütfen!'}), 429
            else:
                error_data = response.json()
                return jsonify({'error': f'❌ Hata: {error_data.get("error", {}).get("message", "Hata oluştu")}'}), response.status_code
        
        result = response.json()
        ai_response = result['choices'][0]['message']['content']
        
        return jsonify({
            'response': ai_response,
            'success': True
        })
    
    except requests.exceptions.Timeout:
        return jsonify({'error': '⏳ İstek zaman aşımına uğradı. Lütfen tekrar deneyin.'}), 504
    except requests.exceptions.ConnectionError:
        return jsonify({'error': '❌ İnternet bağlantısı hatalı.'}), 503
    except Exception as e:
        return jsonify({'error': f'❌ Hata: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
