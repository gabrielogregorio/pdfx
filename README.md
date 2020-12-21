# PDFX
![image](images/pdfx.png)

![GitHub estrelas](https://img.shields.io/github/stars/gabrielogregorio/pdfx)
![GitHub last commit](https://img.shields.io/github/last-commit/gabrielogregorio/pdfx?style=flat-square)
![GitHub contributors](https://img.shields.io/github/contributors/gabrielogregorio/pdfx)
![GitHub language count](https://img.shields.io/github/languages/count/gabrielogregorio/pdfx)
![GitHub repo size](https://img.shields.io/github/repo-size/gabrielogregorio/pdfx)


Este repositório é uma extensão da biblioteca fitz do pymupdf. O objetivo dele é fornecer uma implementação de um algoritmo para alinhar dados extraídos a partir de documentos PDF.

Conforme o exemplo na imagem acima, muitos arquivos PDF podem vir com conteúdo desalinhados, fazendo alguns extratores de PDF posicionar esses dois textos em posições distintas, dificultando a análise dos dados. Através dessa implementação, você consegue definir uma tolerância (alignment) para o algoritmo posicionar itens na mesma linha caso eles estejam dentro desta tolerância.

A implementação simples, se dá através destes passos:   

1. Instale o PyMuPDF, este algoritmo se baseia nos dados extraídos por esta biblioteca.  
```python
pip install PyMuPDF==1.18.5
```

2. Baixe esse repositório na pasta do seu projeto  
3. importe o arquivo "pdfx.py". A execução é desta forma.  


```python
from pdfx import PdfExtract

pdf = PdfExtract()

texto = pdf.extract_text('docs/pdf.pdf', alignment=2)
print(texto)
```

---------------------------------------------------------


# Testes na prática.
### Alinhamento = 0
![image](images/pdfx_0.png)

### Alinhamento = 2
![image](images/pdfx_2.png)

