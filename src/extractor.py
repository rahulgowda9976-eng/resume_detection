import os
import PyPDF2
import docx

def validate_path(file_path: str) -> bool:
    """Check if the given file path exists."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    return True

def extract_text_from_pdf(file_path: str) -> str:
    """Extract text safely from a PDF file."""
    validate_path(file_path)
    text = ""
    try:
        with open(file_path, "rb") as pdf_file:
            reader = PyPDF2.PdfReader(pdf_file)
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:  # Avoid NoneType errors
                    text += page_text + "\n"
    except Exception as e:
        raise RuntimeError(f"Error reading PDF file: {e}")
    return text.strip()

def extract_text_from_docx(file_path: str) -> str:
    """Extract text from a DOCX file, preserving paragraphs."""
    validate_path(file_path)
    try:
        doc = docx.Document(file_path)
        text = "\n".join([para.text for para in doc.paragraphs if para.text.strip()])
    except Exception as e:
        raise RuntimeError(f"Error reading DOCX file: {e}")
    return text.strip()
