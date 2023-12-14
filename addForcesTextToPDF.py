import io
from reportlab.pdfgen import canvas
from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# The path of your font type that is you wanna use in edit in your pdf file

# laptop font path
# font_path = r"C:\Program Files\Adobe\Acrobat DC\Acrobat\WebResources\Resource3\OWP\default\fonts\CaviarDreams_Bold.ttf"

# workstation font path
font_path = (
    r"C:\Program Files (x86)\Adobe\Acrobat DC\Resource\Font\CaviarDreams_Bold.ttf"
)

# Add your font into the pdf file
pdfmetrics.registerFont(TTFont("CaviarDreamsBold", font_path))

# Input and output pdf file paths
input_pdf_path = r"C:\Users\[YOUR USERNAME]\Desktop\41060Diagrams.pdf"
output_pdf_path = r"C:\Users\[YOUR USERNAME]\Desktop\41060Diagrams_new.pdf"

#  "Temel M22 Max Eðilme Momenti Diyagramý (Köprü Enine Yön)",
#   "Temel M22 Min Eðilme Momenti Diyagramý (Köprü Enine Yön)",
#  "Temel M11 Max Eðilme Momenti Diyagramý (Köprü Boyuna Yön)",
# "Temel M11 Min Eðilme Momenti Diyagramý (Köprü Boyuna Yön)",
# Her sayfa için eklemek istediðiniz metin

page_contents = [
    "           - 3D Analiz Modeli (Katı Model)",
    "           - 3D Analiz Modeli",
    "(DC)       - Ölü Yük Yüklemesi",
    "(DW)       - ilave Ölü Yük Yüklemesi",
    "(TU+)      - Isı ve Rötre Yükü Yüklemesi",
    "(BR)       - Fren Yükü Yüklemesi",
    "(LL)       - Hareketli Yük Yüklemesi",
    "(EQ1)      - EQ1 Deprem Yükü Yüklemesi",
    "(EQ2)      - EQ2 Deprem Yükü Yüklemesi",
    "(EH)       - Sükunet Durumu Yatay Zemin Basıncı Yüklemesi",
    "(EH_A)     - Aktif Durum Yatay Zemin Basıncı Yüklemesi",
    "(LS)       - Sürşarj Durumu Yüklemesi",
    "(EH_Q)     - Sismik Durumu Yatay Zemin Basıncı Yüklemesi",
]

# Her sayfaya metni ekleyerek yeni bir PDF oluþtur
input_pdf = PdfReader(open(input_pdf_path, "rb"))
output_pdf = PdfWriter()

for page_num in range(len(input_pdf.pages)):
    page = input_pdf.pages[page_num]

    packet = io.BytesIO()
    c = canvas.Canvas(packet)

    # Orjinal sayfanýn içeriðini çiz
    # c.drawString(100, 750, "Orjinal Sayfa %s" % page_num)

    # Eklemek istediðimiz metni ekleyin
    c.setFont("CaviarDreamsBold", 14)  # Yeni fontu kullanýn
    c.drawString(125, 750, page_contents[page_num])

    c.save()

    # Yeni PDF'i oluþtur
    packet.seek(0)
    new_pdf = PdfReader(packet)
    new_page = new_pdf.pages[0]
    page.merge_page(new_page)
    output_pdf.add_page(page)

# Sonuç dosyasýný kaydet
with open(output_pdf_path, "wb") as output_pdf_file:
    output_pdf.write(output_pdf_file)
