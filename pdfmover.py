import shutil, os

target = os.listdir()
os.mkdir("AutomatedBooks")

for pdf in target:
    if pdf.endswith('.pdf'):
        shutil.move(pdf, "AutomatedBooks")