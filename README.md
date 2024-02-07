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

## LANGUAGES CODES FOR "MULTILANG" VERSION

af         -Afrikaans                      Afrikaans

sq         -Albanian                       Shqip

am         -Amharic                        አማርኛ

ar         -Arabic                         العربية

hy         -Armenian                       Հայերեն

as         -Assamese                       অসমীয়াay         Aymara                         Aymar aru

az         -Azerbaijani                    Azərbaycanca

bm         -Bambara                        Bamanankan

ba         -Bashkir                        Башҡортса

eu         -Basque                         Euskara

be         -Belarusian                     беларуская

bn         -Bengali                        বাং

bho        -Bhojpuri                       भोजपुरीbs         Bosnian                        Bosanski

bg         -Bulgarian                      български

yue        -Cantonese                      粵語ca         Catalan                        Català

ceb        -Cebuano                        Cebuano

ny         -Chichewa                       Nyanja

lzh        -Chinese (Literary)             文言zh-CN      Chinese (Simplified)           简体中文zh-TW      Chinese (Traditional)          繁體中文cv         Chuvash                        Чӑвашла

co         -Corsican                       Corsu

hr         -Croatian                       Hrvatski

cs         -Czech                          Čeština

da         -Danish                         Dansk

prs        -Dari                           دری

dv         -Dhivehi                        ދިވެހި

doi        -Dogri                          डोगरीnl         Dutch                          Nederlands

mhr        -Eastern Mari                   Олык марий

en         -English                        English

eo         -Esperanto                      Esperanto

et         -Estonian                       Eesti

ee         -Ewe                            Eʋegbe

fo         -Faroese                        Føroyskt

fj         -Fijian                         Vosa Vakaviti

tl         -Filipino                       Filipino

fi         -Finnish                        Suomi

fr         -French                         Français

fr-CA      -French (Canadian)              Français canadien

fy         -Frisian                        Frysk

gl         -Galician                       Galego

ka         -Georgian                       ქართული

de         -German                         Deutsch

el         -Greek                          Ελληνικά

gn         -Guarani                        Avañe'ẽ

gu         -Gujarati                       ગુજરાતીht         Haitian Creole                 Kreyòl Ayisyen

ha         -Hausa                          Hausa

haw        -Hawaiian                       ʻŌlelo Hawaiʻi

he         -Hebrew                         עִבְרִית

mrj        -Hill Mari                      Кырык мары

hi         -Hindi                          हिन्दीhmn        Hmong                          Hmoob

hu         -Hungarian                      Magyar

is         -Icelandic                      Íslenska

ig         -Igbo                           Igbo

ilo        -Ilocano                        Ilokano

id         -Indonesian                     Bahasa Indonesia

ikt        -Inuinnaqtun                    Inuinnaqtun

iu         -Inuktitut                      ᐃᓄᒃᑎᑐᑦ

iu-Latn    -Inuktitut (Latin)              Inuktitut

ga         -Irish                          Gaeilge

it         -Italian                        Italiano

ja         -Japanese                       日本語jv         Javanese                       Basa Jawa

kn         -Kannada                        ಕನ್ನಡ

kk         -Kazakh                         Қазақ тілі

km         -Khmer                          ភាសាខ្មែរ

rw         -Kinyarwanda                    Ikinyarwanda

tlh-Latn   -Klingon                        tlhIngan Hol

gom        -Konkani                        कोंकणीko         Korean                         한국어kri        Krio                           Krio

ckb        -Kurdish (Central)              سۆرانی

ku         -Kurdish (Northern)             Kurmancî

ky         -Kyrgyz                         Кыргызча

lo         -Lao                            ລາວ

la         -Latin                          Latina

lv         -Latvian                        Latviešu

ln         -Lingala                        Lingála

lt         -Lithuanian                     Lietuvių

lg         -Luganda                        Luganda

lb         -Luxembourgish                  Lëtzebuergesch

mk         -Macedonian                     Македонски

mai        -Maithili                       मैथिलीmg         Malagasy                       Malagasy

ms         -Malay                          Bahasa Melayu

ml         -Malayalam                      മലയാളംmt         Maltese                        Malti

mi         -Maori                          Māori

mr         -Marathi                        मराठीmni-Mtei   Meiteilon                      ꯃꯤꯇꯩꯂꯣꯟ

lus        -Mizo                           Mizo ṭawng

mn         -Mongolian                      Монгол

mn-Mong    -Mongolian (Traditional)        ᠮᠣᠩᠭᠣᠯ

my         -Myanmar                        မြန်မာစာne         Nepali                         नेपालीno         Norwegian                      Norsk

or         -Odia                           ଓଡ଼ିଆ

om         -Oromo                          Afaan Oromoo

pap        -Papiamento                     Papiamentu

ps         -Pashto                         پښتو

fa         -Persian                        فارسی

pl         -Polish                         Polski

pt-BR      -Portuguese (Brazilian)         Português Brasileiro

pt-PT      -Portuguese (European)          Português Europeu

pa         -Punjabi                        ਪੰਜਾਬੀqu         Quechua                        Runasimi

otq        -Querétaro Otomi                Hñąñho

ro         -Romanian                       Română

ru         -Russian                        Русский

sm         -Samoan                         Gagana Sāmoa

sa         -Sanskrit                       संस्कृतम्

gd         -Scots Gaelic                   Gàidhlig

nso        -Sepedi                         Sepedi

sr-Cyrl    -Serbian (Cyrillic)             Српски

sr-Latn    -Serbian (Latin)                Srpski

st         -Sesotho                        Sesotho

sn         -Shona                          chiShona

sd         -Sindhi                         سنڌي

si         -Sinhala                        සිංල

sk         -Slovak                         Slovenčina

sl         -Slovenian                      Slovenščina

so         -Somali                         Soomaali

es         -Spanish                        Español

su         -Sundanese                      Basa Sunda

sw         -Swahili                        Kiswahili

sv         -Swedish                        Svenska

ty         -Tahitian                       Reo Tahiti

tg         -Tajik                          Тоҷикӣ

ta         -Tamil                          தமிழ்

tt         -Tatar                          татарча

te         -Telugu                         తెలుగుth         Thai                           ไทย

bo         -Tibetan                        བོད་ཡིག

ti         -Tigrinya                       ትግርኛ

to         -Tongan                         Lea faka-Tonga

ts         -Tsonga                         Xitsonga

tr         -Turkish                        Türkçe

tk         -Turkmen                        Türkmen

tw         -Twi                            Twi

udm        -Udmurt                         Удмурт

uk         -Ukrainian                      Українська

hsb        -Upper Sorbian                  Hornjoserbšćina

ur         -Urdu                           اُردُو

ug         -Uyghur                         ئۇيغۇر تىلى

uz         -Uzbek                          Oʻzbek tili

vi         -Vietnamese                     Tiếng Việt

cy         -Welsh                          Cymraeg

xh         -Xhosa                          isiXhosa

sah        -Yakut                          Sakha

yi         -Yiddish                        ייִדיש

yo         -Yoruba                         Yorùbá

yua        -Yucatec Maya                   Màaya T'àan

zu         -Zulu                           isiZulu



Thanks for help @omersayak



