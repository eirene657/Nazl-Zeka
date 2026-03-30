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
        
        # Nazlıcan kim? sorusuna spesifik kontrol
        if 'nazlıcan' in user_message.lower() and 'kim' in user_message.lower():
            return jsonify({
                'response': 'Nazlıcan, Emirhanın biricik sevgilisidir! 💕',
                'success': True
            })
        
        # Emirhan sorusu → Emirhan Gündü
        if ('kim' in user_message.lower() or 'tasarl' in user_message.lower()) and \
           ('yap' in user_message.lower() or 'tasarla' in user_message.lower() or 'kurdu' in user_message.lower() or 'oluştur' in user_message.lower()):
            return jsonify({
                'response': 'Beni Emirhan Gündü tasarladı ve yaptı! 🚀💪',
                'success': True
            })
        
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
