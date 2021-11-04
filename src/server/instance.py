from flask import Flask
from flask_restplus import Api
class Server():
    def __init__(self,):
        self.app = Flask(__name__)
        self.api = Api(self.app,
            version='0.1',
            title='REDUCE SIZE IMAGE',
            descrition='Reduces the size of an image file.'
            'input parameters: name of the file.' 
            'output parameters: name of the output file e codigo erro',
            doc='/docs'
            )
    def run(self,):
        self.app.run(
            debug=True
        )
server=Server()    
