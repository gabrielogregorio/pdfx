# PDFX
![image](images/pdfx.png)


![GitHub estrelas](https://img.shields.io/github/stars/gabrielogregorio/pdfx)
![GitHub last commit](https://img.shields.io/github/last-commit/gabrielogregorio/pdfx?style=flat-square)
![GitHub contributors](https://img.shields.io/github/contributors/gabrielogregorio/pdfx)
![GitHub language count](https://img.shields.io/github/languages/count/gabrielogregorio/pdfx)
![GitHub repo size](https://img.shields.io/github/repo-size/gabrielogregorio/pdfx)



Este repositório é uma extensão da biblioteca fitz do pymupdf. O objetivo dele é fornecer uma implementação de um algoritimo para alinhar dados extraidos a partir de documentos PDF.

Conforme o exemplo na imagem acima, muitos arquivos PDF podem vir com conteúdos desalinhados, fazendo algungs extratores de PDF posicionar esses dois textos em posições distintas, dificultando a análise dos dados. Atravéz dessa implementação, você consegue definir uma tolerância (alignment) para o algoritimo posicionar itens na mesma linha caso eles estejam dentro desta tolerância.

A implementação simples, se da atravéz destes passos:   

1. Instale o PyMuPDF, este  algoritimo se basea nos dados estraídos por esta biblioteca.  
```python
pip install PyMuPDF==1.18.5
```

2. Baixe esse respostório na pasta do seu projeto  
3. importe o arquivo "pdfx.py". A execução é desta forma.  


```python
from pdfx import PdfExtract

pdf = PdfExtract()

texto = pdf.extract_text('docs/pdf.pdf', alignment=2)
print(texto)
```

-------------


# Testes na pratica.
### Alinhamento = 0
![image](images/pdfx_0.png)

### Alinhamento = 2
![image](images/pdfx_2.png)

