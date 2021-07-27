import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
tessdata_dir_config = '--tessdata-dir "C:\\Program Files (x86)\\Tesseract-OCR\\tessdata"'

def ocr(plate):
    text = pytesseract.image_to_string(plate,config=tessdata_dir_config,lang="eng") #variabila text este 
    return text                                                                     #nr de inmatriculare extras din imagine
