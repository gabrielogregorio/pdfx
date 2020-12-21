from pdfx import PdfExtract

# python 3
# pip install PyMuPDF==1.18.5

pdf = PdfExtract()

texto = pdf.extract_text('docs/pdf.pdf', alignment=2)
print(texto)
