from pdfx import PdfExtract

pdf = PdfExtract()

texto = pdf.extract_text('docs/pdf.pdf', alignment=2)
print(texto)
