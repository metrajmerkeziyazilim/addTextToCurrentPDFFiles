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
input_pdf_path = r"C:\Users\Metraj Merkezi\Desktop\41060Diagrams.pdf"
output_pdf_path = r"C:\Users\Metraj Merkezi\Desktop\41060Diagrams_new.pdf"


page_contents = [
    "Perde Düşey M22 iç Maksimum Momenti Diyagramı",
    "Perde Düşey M22 Dış Minimum Momenti Diyagramı",
    "Perde Yatay M11 iç Maksimum Momenti Diyagramı",
    "Perde Yatay M11 Dış Minimum Momenti Diyagramı",
    "Ricat Düşey M22 iç Maksimum Momenti Diyagramı",
    "Ricat Düşey M22 Dış Minimum Momenti Diyagramı",
    "Ricat Yatay M11 iç Maksimum Momenti Diyagramı",
    "Ricat Yatay M11 Dış Minimum Momenti Diyagramı",
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
    c.drawString(125, 700, page_contents[page_num])

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
