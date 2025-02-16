from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import datetime

def generate_pdf_with_graph(city: str, graph_path: str, output_filename: str):
    c = canvas.Canvas(output_filename, pagesize=A4)
    width, height = A4

    c.setFont("Helvetica-Bold", 16)
    titre = f"Prévisions Météo pour {city}"
    c.drawCentredString(width / 2, height - 50, titre)

    c.setFont("Helvetica", 12)
    date_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    c.drawString(50, height - 80, f"Date de génération : {date_str}")

    img_max_width  = width - 100
    img_max_height = height - 180

    x = 50
    y = height - 120 - img_max_height

    c.drawImage(graph_path, x, y, width=img_max_width, height=img_max_height, preserveAspectRatio=True, mask='auto')

    c.showPage()
    c.save()

