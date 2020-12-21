# Vem do pymupdf

from fitz import Document as fitz_Document
from html import unescape as html_unescape

import re

class PdfExtract:
    """Extract text from a PDF from the installed pymupdf library
    and arrange the text in order as the text is viewed """
    def __init__(self):
        pass


    def extract_text(self, filename:str, alignment:int = 0) -> str:
        """It deals specifically with the extraction of texts in PDF, formatting the content
         according to the order they appear in the document and making text adjustments
         who are unaligned

         Args:
             filename (str): PDF file location
             alignment (int): Region to consider along the same lines

         Returns:
             str: text structured correctly
        """ 

        line_dictionary = {}
        with fitz_Document(filename) as doc:

            # Highest registered top (pag1, pag2)
            greater_page_point = 0

            # Increment to the top to start from
            # of a point determiner (pag1, pag2)
            minimum_point = 0

            # Scroll through the pages of the PDF
            for current_page in range(len(doc)):
                    # Page loading
                    page = doc.loadPage(current_page) 

                    # Transform PDF to HTML
                    HTML_lines = str(page.getText("html")).split('\n')

                    # Extracting data from HTML
                    regex = "<p.*top\\:(\\d{1,}).*left\\:(\\d{1,}).*><span.*>(.{1,})<\\/span\\>.*<\\/p\\>"
                    for line in HTML_lines:
                        answer = re.search(regex, line)

                        # If the line is valid
                        if answer is not None: 
                            top = int(answer.group(1)) + minimum_point
                            left = int(answer.group(2))
                            text = html_unescape(answer.group(3))
                            
                            """
                            This excerpt searches for photos that are close to group the text
                            """

                            # There is already something on that line
                            if line_dictionary.get(top): 
                                line_dictionary[top][left] = text
                            else: 




                                found_region = False

                                for i in range(alignment):
                                    # Searching near the line
                                    if top + i in line_dictionary.keys():
                                        line_dictionary[top + i][left] = text
                                        found_region = True
                                        break

                                    elif top - i in line_dictionary.keys():
                                        line_dictionary[top - i][left] = text
                                        found_region = True
                                        break

                                if not found_region:
                                    line_dictionary[top] = {left: text}

                            # Saving the biggest top
                            if top > greater_page_point:
                                greater_page_point = top

                    # Variable and reference to
                    # do not overwrite text             
                    minimum_point = greater_page_point

        return self.sort_dictionary_straction(line_dictionary)


    def sort_dictionary_straction(self, line_dictionary:dict) -> str:
        """Sort the X and Y position data of the words

         Args:
             line_dictionary (dict): Dictionary with the data in the pattern specified in the calling function

         Returns:
             str: text structured correctly
        """

        # Ordering the tops
        lista = list(line_dictionary.keys())
        lista.sort(reverse=False)

        # Scroll through the top list
        text = ""
        for top in lista:

            # Text dictionary
            # Left aligned
            dict_2 = line_dictionary[top]

            # Ordering of text placement
            lista2 = list(dict_2.keys())
            lista2.sort(reverse=False)

            # text order on line
            text_line = ""
            for num in lista2:
                text_local = line_dictionary[top][num]
                text_line = text_line + " " + text_local

            # addition in main text
            text += "\n" + text_line

        # final text
        return text.lower().strip()


