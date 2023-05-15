import pdf2docx

pdf_file = "sample.pdf"
docx_file = "sample.docx"

cv = pdf2docx.Converter(pdf_file)
cv.convert(docx_file)
cv.close()