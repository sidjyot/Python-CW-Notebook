from PyPDF4 import PdfFileReader
file = open('document-2.pdf', 'rb')
document = PdfFileReader(file)

n = document.numPages
e = document.isEncrypted
c = document.documentInfo['/CreationDate']
p = document.documentInfo['/Producer']
#print(f'{n} {e} {c} {p}')
for i in range(n):
  page = document.getPage(i)
  #print("Page No.: ",i)
  text = page.extractText().split("\n")
  for line in text:
    if 'current value ' in line.lower():
      print(line)
      break
file.close()
