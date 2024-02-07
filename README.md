# PDF Translator

Bu Python betiği, belirtilen bir PDF dosyasındaki metni çevirmek için kullanılır. Metin çevirisi için Google Translate veya benzeri bir hizmet kullanılır. Çevirilen metinler, orijinal PDF dosyasındaki sayfa düzenine sadık kalarak yeni bir PDF dosyasına yazılır. Yalnizca Ingilizceden Turkceye ceviri yapmaktadir En azindan simdilik :) 

## Kurulum

1. Python yüklü olmalıdır. [Python'un resmi web sitesinden](https://www.python.org/downloads/) indirebilirsiniz.

2. translate-shell yuklu olmalidir. (apt reposundan "sudo apt install translate-shell" komutuyla indirebilirsiniz)

3. Ayrica ceviriden sonra Turkce karakterlarin okunabilir olmasi icin scripti bir duzenleyici ile acin

#DejaVuSans fontunu kaydet
pdfmetrics.registerFont(TTFont('DejaVuSans', '/home/opt/pdftrans/DejaVuSans.ttf')) 
#Fontun yolunu güncelle 

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




## English

# PDFtrans
# PDF Translator

This Python script is used to translate the text in a specified PDF file. Text translation is performed using Google Translate or a similar service. The translated texts are written to a new PDF file while preserving the original layout of the pages. Currently, it only translates from English to Turkish, at least for now :)

## Installation

1. Python must be installed. You can download it from the [official Python website](https://www.python.org/downloads/).

2. `translate-shell` must be installed. (You can install it from the apt repository using the command `sudo apt install translate-shell`)

3. Additionally, to make Turkish characters readable after translation, open the script with an editor.

```
# Register the DejaVuSans font
pdfmetrics.registerFont(TTFont('DejaVuSans', '/home/opt/pdftrans/DejaVuSans.ttf')) 
# Update the path of the font
```

4. To install the required libraries, run the following command in the terminal or command prompt:

   ```
   pip install -r requirements.txt
   ```

## Usage

1. Prepare the PDF file to be translated.

2. Run the `pdftrans.py` script in the terminal or command prompt.

3. Answer the relevant questions to start the translation process.

## Example

```
python translator.py
```

## Requirements

- PyPDF2==1.26.0
- reportlab==3.6.1

## Contributing

If you would like to contribute to this project, please open a new issue or send a pull request.


