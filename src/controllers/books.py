from flask import Flask
from flask import request
from flask_restplus import Api
from src.server.instance import server
import sys
from PIL import Image
#http://127.0.0.1:5000/reducesizeimage?namefile=E:\appnotice\apiflaskreducesizeimage\marina.png&lenfile=120

app,api = server.app, server.api
@app.route('/')
def index():
    return
@app.route('/reducesizeimage')            
def reducesizeimage():
    #input parameters
    Filename=request.args.get('namefile','Need the filename.')
    Filelen=request.args.get('lenfile','Need the filename.')
    largura_desejada = int(Filelen)
    #open the image
    imagem = Image.open(Filename)
    #calculation of new dimensions of image
    largura_imagem = imagem.size[0]
    altura_imagem = imagem.size[1]
    percentual_largura = float(largura_desejada) / float(largura_imagem)
    altura_desejada = int((altura_imagem * percentual_largura))
    imagem = imagem.resize((largura_desejada, altura_desejada), Image.ANTIALIAS)
    outputFilename='imagem-{}x{}.png'.format(imagem.size[0], imagem.size[1])
    #save the new image
    imagem.save(outputFilename)
    return outputFilename