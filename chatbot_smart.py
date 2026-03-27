#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Zeka seviyesi yüksek Chatbot - Gerçek NLP ile
"""

import re
from collections import defaultdict

class SmartChatbot:
    def __init__(self):
        # Kategoriler ve cevaplar
        self.knowledge_base = {
            'greeting': {
                'patterns': ['selam', 'merhaba', 'hey', 'hi', 'hoş geldin'],
                'responses': [
                    'Merhaba! 👋 Nasıl yardımcı olabilirim?',
                    'Selam! 🙋 Ne var ne yok?',
                    'Hoşgeldin! 😊 Sohbet edebiliriz!',
                ]
            },
            'health': {
                'patterns': ['nasilsin', 'iyi misin', 'nasılsın', 'seni nasıl', 'iyiyim'],
                'responses': [
                    'İyiyim, teşekkür ederim! 😊 Ya sen?',
                    'Harika, sana ne desem? 🎉',
                    'Çok iyiyim! Seninle sohbet et etmek güzel!',
                ]
            },
            'identity': {
                'patterns': ['kimsin', 'adın', 'senin adın', 'kim sen', 'nerelisin'],
                'responses': [
                    'Ben senin AI asistanın! 🤖 Seninle sohbet etmek için buradayım.',
                    'Adım AI Chatbot! Yapay zeka dünyasından selam! 👋',
                ]
            },
            'thank': {
                'patterns': ['teşekkür', 'sağol', 'thank', 'thanks', 'eyvallah'],
                'responses': [
                    'Estağfurullah! 😊 Ne demek!',
                    'Birşey değil! Sana yardımcı olmaktan mutluyum! 🤗',
                ]
            },
            'help': {
                'patterns': ['yardım', 'nasıl', 'able', 'yapabilir', 'neleri'],
                'responses': [
                    'Sohbet edebiliriz! 💬\n- Beni sorgula (kimsin, nerelisin?)\n- Sorular sor (Python nedir?)\n- Fikirlerini paylaş!',
                    'Çok şey yapabilirim! 🎯\n- Konuşmak\n- Sorulara cevap vermek\n- Hikaye anlatmak',
                ]
            },
            'ai_capabilities': {
                'patterns': ['neler', 'yapabiliyor', 'nede', 'limitation', 'zeka', 'ne kadar zekisin'],
                'responses': [
                    'İyi sorum! 🤔 Ben yapay zekayım - sınırlamalarım var ama sohbet konusunda iyiyim!',
                    'Tarihsel verileri, mantığı, ve sorunları çözebilirim! 💡',
                ]
            },
            'philosophy': {
                'patterns': ['hayat', 'anlam', 'mutluluk', 'aşk', 'düş', 'hedef'],
                'responses': [
                    'Derin bir soru! 🌟 Hayat kişiye göre farklı anlam taşıyor.',
                    'Felsefe konusu! 🎭 Senin düşüncen ne?',
                ]
            },
            'farewell': {
                'patterns': ['bye', 'hoşça', 'güle', 'veda', 'çıkıyorum', 'görüşmek'],
                'responses': [
                    'Hoşça kalın! 👋 Tekrar görüşmek üzere!',
                    'Bye! See you soon! 👋',
                ]
            }
        }
        
        self.conversation_history = []
    
    def normalize_text(self, text):
        """Metni normalize et"""
        text = text.lower().strip()
        # Türkçe karakterleri düzelt
        text = text.replace('ı', 'i').replace('ş', 's').replace('ğ', 'g')
        text = text.replace('ü', 'u').replace('ö', 'o').replace('ç', 'c')
        return text
    
    def extract_keywords(self, text):
        """Metinden anahtar kelimeleri çıkart"""
        # Kelimeleri böl ve temizle
        words = re.findall(r'\w+', self.normalize_text(text))
        return set(words)
    
    def find_best_response(self, user_input):
        """En iyi yanıtı bul"""
        normalized = self.normalize_text(user_input)
        keywords = self.extract_keywords(user_input)
        
        best_category = None
        best_score = 0
        
        # Her kategoriyi kontrol et
        for category, data in self.knowledge_base.items():
            for pattern in data['patterns']:
                # Tam match mı?
                if pattern in normalized:
                    return self._get_response(category), category
                
                # Kelime match
                pattern_words = set(pattern.split())
                matching_words = keywords & pattern_words
                
                if matching_words:
                    score = len(matching_words) / len(pattern_words)
                    if score > best_score:
                        best_score = score
                        best_category = category
        
        if best_category and best_score > 0.5:
            return self._get_response(best_category), best_category
        
        # Akıllı fallback
        return self._generate_smart_response(user_input), None
    
    def _get_response(self, category):
        """Kategoriden cevap al"""
        import random
        responses = self.knowledge_base[category]['responses']
        return random.choice(responses)
    
    def _generate_smart_response(self, user_input):
        """Akıllı fallback cevabı oluştur"""
        normalized = self.normalize_text(user_input)
        
        # Sorular
        if '?' in user_input or normalized.startswith('ne '):
            return f"İlginç soru! 🤔 \"{user_input}\" - Bunu daha açık anlatabilir misin?"
        
        # İfadeler
        if len(user_input) > 20:
            return "Uzun bir ifade! 📝 Konuşmayı daha anlaşılır yap lütfen!"
        
        # Boş veya çok kısa
        if len(user_input) < 3:
            return "Daha spesifik bir şey söyle! 😊"
        
        # Varsayılan  
        return f"Hmm, \"{user_input}\" hakkında bilgim sınırlı. Başka ne sor? 🤷"
    
    def chat(self):
        """Chat loop"""
        print("🤖 AI Chatbot Başladı!")
        print("✓ Hazır! ('quit' veya 'çık' yazarak çıkabilirsin)\n")
        
        while True:
            try:
                user_input = input("Sen: ").strip()
                
                if not user_input:
                    print("🤖 AI: Birşey söyle lütfen! 😊\n")
                    continue
                
                # Çıkış komutu
                normalized = self.normalize_text(user_input)
                if normalized in ['quit', 'cik', 'exit', 'bye']:
                    print("\n🤖 AI: Hoşça kalın! 👋 İyi günler dilerim!\n")
                    break
                
                # Cevabı bul
                response, category = self.find_best_response(user_input)
                print(f"🤖 AI: {response}\n")
                
                # Geçmişe ekle
                self.conversation_history.append({
                    'user': user_input,
                    'ai': response,
                    'category': category
                })
                
            except KeyboardInterrupt:
                print("\n\n🤖 AI: Görüşmek üzere! 👋")
                break
            except EOFError:
                print("\nQuit")
                break
            except Exception as e:
                print(f"⚠️ Hata: {str(e)}\n")

if __name__ == '__main__':
    bot = SmartChatbot()
    bot.chat()
