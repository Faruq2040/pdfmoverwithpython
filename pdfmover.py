import shutil, os

target = os.listdir()
os.mkdir("Automated_PDF_Books")

for pdf in target:
    if pdf.endswith('.pdf'):
        shutil.move(pdf, "AutomatedBooks")
