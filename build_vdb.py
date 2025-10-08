import os
from pypdf import PdfReader

DOCUMENTS_DIR = './documents'
EMBEDDING_MODEL = 'all-MiniLM-L6-v2'
CHUNK_SIZE = 800
CHUNK_OVERLAP = 100

def extract_from_pdf(dir):
    '''
    Extracts text from pdf files in directory
    '''

    documents_text = []

    if not os.path.isdir(dir):
        raise ValueError(f"{dir} is not a valid directory")
    elif os.listdir(dir) == []:
        raise ValueError(f"{dir} is empty")
        
    for filename in os.listdir(dir):
        if not filename.endswith('.pdf'):
            print("Warning - skipping non-pdf file:", filename)
            
        # Extract text from each pdf
        try:
            reader = PdfReader(os.path.join(dir, filename))
            text = ""
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text
            documents_text.append(text)
        except Exception as e:
            print(f"Error reading {filename}: {e}")

