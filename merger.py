from PyPDF2 import PdfWriter
import sys

merger = PdfWriter()

args = len(sys.argv) - 1
i = 1
while (args >= i):
    merger.append(sys.argv[i])
    i = i + 1

merger.write("merged.pdf")
merger.close()
