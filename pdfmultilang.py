import subprocess
import PyPDF2
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import io
import os
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# DejaVuSans fontunu kaydet
if os.name == 'nt':
    pdfmetrics.registerFont(TTFont('DejaVuSans', str(os.getcwd()) + '\\DejaVuSans.ttf')) # Windows için
else:
    pdfmetrics.registerFont(TTFont('DejaVuSans', str(os.getcwd()) + '/DejaVuSans.ttf')) # Linux için
    

def translate_text(text, dest_lang='tr'):
    translation = subprocess.run(['trans', '-b', f':{dest_lang}', text], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if translation.stderr:
        print(f"Error during translation: {translation.stderr}")
    return translation.stdout.strip()

def text_to_pdf(text):
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    text_object = c.beginText(40, 750)
    text_object.setFont("DejaVuSans", 10)  # Fontu DejaVuSans olarak değiştir

    lines = text.split('\n')
    for line in lines:
        text_object.textLine(line)

    c.drawText(text_object)
    c.showPage()
    c.save()
    buffer.seek(0)
    return buffer

def translate_pdf(pdf_path, dest_lang='tr'):
    translated_pages = []
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        for page_number, page in enumerate(pdf_reader.pages):
            text = page.extract_text()
            print(f"Extracting text from page {page_number}...")
            if text:
                translated_text = translate_text(text, dest_lang=dest_lang)
                translated_pages.append(translated_text)
                print(f"Page {page_number} translated.")
            else:
                print(f"No text found on page {page_number}.")
                translated_pages.append('')
    return translated_pages

def create_translated_pdf(translated_pages, output_path):
    pdf_writer = PyPDF2.PdfWriter()
    for page_text in translated_pages:
        page_buffer = text_to_pdf(page_text)
        page_pdf = PyPDF2.PdfReader(page_buffer)
        pdf_writer.add_page(page_pdf.pages[0])

    with open(output_path, 'wb') as output_pdf:
        pdf_writer.write(output_pdf)

    print(f"Translation complete. Check the PDF at '{output_path}'.")

def main():
    pdf_path = input("Enter the path of the PDF to be translated: ")
    dest_lang = input("Enter the destination language (e.g., 'fr' for French): ")
    output_path = input("Enter the name for the translated PDF file (including .pdf extension): ")
    translated_pages = translate_pdf(pdf_path, dest_lang)
    create_translated_pdf(translated_pages, output_path)

if __name__ == "__main__":
    main()
