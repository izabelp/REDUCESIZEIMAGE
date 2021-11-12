from flask import Flask
from flask import request
from flask_restplus import Api
from src.server.instance import server
import sys
from PIL import Image
from flask import jsonify
from pathlib import Path

<<<<<<< HEAD
#http://127.0.0.1:5000/reducesizeimage?namefile=E:\appnotice\apiflaskreducesizeimage\marina.png&lenfile=120
=======
>>>>>>> d4ecd7156d48ec0e5b48b8d1df976875001f3fcc
#http://izabelpimentel.com/reducesizeimage?namefile=E:\appnotice\apiflaskreducesizeimage\marina.png&lenfile=120

app,api = server.app, server.api
@app.route('/reducesizeimage')            
def reducesizeimage():
    #parametros de entrada
    Filename=request.args.get('namefile')
    if Filename==None:
        response = {'message': 'Archivo no especificado.'}
        return jsonify(response) 
    Filelen=request.args.get('lenfile')
    if Filelen==None:
        response = {'message': 'Largura del archivo no especificado.'}
        return jsonify(response) 
    largura_desejada = int(Filelen)
    #opende la imagen
<<<<<<< HEAD
    if Path(Filename).exists():
        print(Filename,"ok",Path(Filename).exists())
        imagem = Image.open(Filename)
        #calculo dimensiones imagen
        largura_imagem = imagem.size[0]
        altura_imagem = imagem.size[1]
        percentual_largura = float(largura_desejada) / float(largura_imagem)
        altura_desejada = int((altura_imagem * percentual_largura))
        imagem = imagem.resize((largura_desejada, altura_desejada), Image.ANTIALIAS)
        outputFilename='imagem-{}x{}.png'.format(imagem.size[0], imagem.size[1])
        #save nueva imagen
        imagem.save(outputFilename)
        response= {'Archivosalida':outputFilename}
        return jsonify(response) 
    else:
        response= {'Erro':'file not exist'} 
        return jsonify(response)   
=======
    imagem = Image.open(Filename)
    print(imagem)
    #calculo dimensiones imagen
    largura_imagem = imagem.size[0]
    altura_imagem = imagem.size[1]
    percentual_largura = float(largura_desejada) / float(largura_imagem)
    altura_desejada = int((altura_imagem * percentual_largura))
    imagem = imagem.resize((largura_desejada, altura_desejada), Image.ANTIALIAS)
    outputFilename='imagem-{}x{}.png'.format(imagem.size[0], imagem.size[1])
    #save nueva imagen
    imagem.save(outputFilename)
    response= {'Archivosalida':outputFilename}
    return jsonify(response) 
>>>>>>> d4ecd7156d48ec0e5b48b8d1df976875001f3fcc
