import PyPDF2
import os

merger = PyPDF2.PdfMerger()

lista_arquivos = os.listdir("arquivos")
lista_arquivos.sort()

for arquivo in lista_arquivos:
    if arquivo.endswith(".pdf"):  # melhor que ".pdf" in arquivo
        merger.append(os.path.join("arquivos", arquivo))

merger.write("PDF_Final.pdf")
merger.close()




