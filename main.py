import img2pdf as img2pdf
from PIL import Image
import os

#path to your image.png file
img_path = "/home/milena/Imagens/Teste/imagem.png"

#path to your path and files name destiny
pdf_path = '/home/milena/Imagens/Teste/imagem.pdf'
from PIL import Image


image1 = Image.open(r'/home/milena/Imagens/Teste/imagem.png')
im1 = image1.convert('RGB')
im1.save(r'/home/milena/Imagens/Teste/name.pdf')

#sucess
