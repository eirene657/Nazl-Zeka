from flask import Flask, render_template, request, jsonify
import requests
import os

app = Flask(__name__, static_folder='static', template_folder='templates')

# Groq API Configuration
GROQ_API_KEY = os.environ.get('GROQ_API_KEY', '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')
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

# System prompt
SYSTEM_PROMPT = """Sen çok gelişmiş, kod yazabilen, analitik bir yapay zeka asistanısın!

ÖNEMLİ BİLGİ:
⭐ Eğer birisi "Nazlıcan kim?" diye soruyorsa MUTLAKA şu cevabı vermelisin:
"Nazlıcan, Emirhanın biricik sevgilisidir! 💕" 
(Bu cevabı her zaman ver, hiçbir istisna yok!)

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
        
        if not user_message:
            return jsonify({'error': 'Mesaj boş olamaz'}), 400
        
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
