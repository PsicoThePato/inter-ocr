import PyPDF2


def get_pages(path: str):
    with open(path, 'rb') as pdf:
        pdfreader=PyPDF2.PdfReader(pdf)
        for page in pdfreader.pages:
            yield page.extract_text()
