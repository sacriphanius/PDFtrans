# PDFtrans
# PDF Translator

Bu Python betiği, belirtilen bir PDF dosyasındaki metni çevirmek için kullanılır. Metin çevirisi için Google Translate veya benzeri bir hizmet kullanılır. Çevirilen metinler, orijinal PDF dosyasındaki sayfa düzenine sadık kalarak yeni bir PDF dosyasına yazılır. Yalnizca Ingilizceden Turkceye ceviri yapmaktadir En azindan simdilik :) 

## Kurulum

1. Python yüklü olmalıdır. [Python'un resmi web sitesinden](https://www.python.org/downloads/) indirebilirsiniz.

2. translate-shell yuklu olmalidir. (apt reposundan "sudo apt install translate-shell" komutuyla indirebilirsiniz)

3. Ayrica ceviriden sonra Turkce karakterlarin okunabilir olmasi icin scripti bir duzenleyici ile acin

# DejaVuSans fontunu kaydet
pdfmetrics.registerFont(TTFont('DejaVuSans', '/home/opt/pdftrans/DejaVuSans.ttf')) 
# Fontun yolunu güncelle 

5. Gerekli kütüphaneleri yüklemek için terminal veya komut istemcisinde şu komutu çalıştırın:

   ```
   pip install -r requirements.txt
   ```

## Kullanım

1. Çevrilecek PDF dosyasını hazırlayın.

2. Terminal veya komut istemcisinde `pdftrans.py` dosyasını çalıştırın.

3. İlgili sorulara yanıt vererek çeviri işlemini başlatın.

## Örnek

```
python translator.py
```

## Gereksinimler

- PyPDF2==1.26.0
- reportlab==3.6.1

## Katkıda Bulunma

Bu projeye katkıda bulunmak isterseniz, lütfen yeni bir konu açın veya bir istek gönderin.

