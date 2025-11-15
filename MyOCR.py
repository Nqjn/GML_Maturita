import easyocr

def ReadData(path: str):
    print(f"Zpracovávám OCR pro soubor: {path}")
    reader = easyocr.Reader(['en', 'cs'], gpu=False)
    result = reader.readtext(path)
    
    return result
    
