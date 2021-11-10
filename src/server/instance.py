from flask import Flask
from flask_restplus import Api
class Server():
    def __init__(self,):
        self.app = Flask(__name__)
        self.api = Api(self.app,
            version='0.1',
            title='REDUCE TAMAÑO IMAGE',
            descrition='Reduce el tamaño de un archivo imagen'
            'parametro de entrada: nombre del archivo.' 
            'parametro de salida: nombre del archivo de salida y el codigo 200 si no errores.',
            doc='/docs'
            )
    def run(self,):
        self.app.run(
            debug=True
        )
server=Server()    
