import pandas as pd
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from textwrap import wrap

# Load CSV
df = pd.read_csv("news.csv")

# Keep only needed columns
df = df[['text', 'label']]

# Limit number of news for demo (change if needed)
df = df.head(50)

# Create PDF
pdf = canvas.Canvas("news_demo.pdf", pagesize=A4)
width, height = A4

x_margin = 50
y_margin = height - 50
y = y_margin

pdf.setFont("Helvetica", 11)

for idx, row in df.iterrows():
    title = f"News {idx + 1} ({row['label']})"
    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(x_margin, y, title)
    y -= 18

    pdf.setFont("Helvetica", 10)
    wrapped_text = wrap(row['text'], 90)

    for line in wrapped_text:
        if y < 60:
            pdf.showPage()
            pdf.setFont("Helvetica", 10)
            y = y_margin
        pdf.drawString(x_margin, y, line)
        y -= 14

    y -= 20  # space between news

pdf.save()
print("PDF created: news_demo.pdf")
