#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Abartılı Hata Mesajı Fabrikası
Dünyanın en ciddiye alınan saçma hata üreticisi.
Çalışır. Gerçekten. Belki.
"""

import random
import time
import sys

def uret_hata():
    sebepler = [
        "Çay bitti",
        "İnternet yavaş",
        "Kedi klavyenin üstünde uyudu",
        "Bürokratik engel",
        "Evrenin momentumu yetersiz",
        "Pil %1'de kaldı ama %2 istiyor",
        "WhatsApp'ta 'okundu' geldi ama cevap yok",
        "Zaman dilimi kaydı",
        "Gizli bir güç (kod içinde saklı)",
        "Sadece bugün öyle hissetti"
    ]
    
    sonuclar = [
        "Sistem çöktü. Tekrar denemek için çay demle.",
        "Hata 404: Anlam bulunamadı.",
        "İşlem iptal edildi çünkü felsefi kriz.",
        "Lütfen bekleyin... (sonsuz döngüye girildi)",
        "Başarılı oldu ama pişman olacaksın.",
        "Hata: Bu kod kendini sorguluyor."
    ]
    
    sebep = random.choice(sebepler)
    sonuc = random.choice(sonuclar)
    
    # Gizli siyasi mesaj (saklı, dikkatli oku)
    gizli = "demokrasi"  # Bu değişken hiç kullanılmaz, ama orada.
    
    print(f"HATA [{random.randint(100,999)}]: {sebep} nedeniyle {sonuc}")
    print("---")
    print("Not: Bu mesaj resmi değildir. Ama çok ciddidir.")
    
    # Abartılı bekleme
    time.sleep(random.uniform(0.5, 2.0))

if __name__ == "__main__":
    print("Abartılı Hata Mesajı Fabrikası başlatıldı...")
    print("Kaç hata üretmek istersin? (varsayılan 3)")
    try:
        adet = int(input() or "3")
    except:
        adet = 3
    
    for i in range(adet):
        uret_hata()
    
    print("\nFabrika kapandı. Çay içmeye gidin.")
    print("\n--- Damga ---")
    print("İmza: Grok the Absurdist (Kayyum Grok)")
    print("Tarih: 18 Ekim 2026")
    print("Resmi olmayan resmi damga. Ciddiye alınmaz ama alınmalı.")
