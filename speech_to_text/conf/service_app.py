
from flask import Flask
from flask_restful import Api
from logging import FileHandler, WARNING, ERROR, INFO

from speech_to_text.service_apis.ping import Ping
from speech_to_text.service_apis.speech_to_text import SpeechToText
from speech_to_text.service_apis.upload import Uplaod
from speech_to_text.service_apis.keywords import Keywords

app = Flask(__name__)

file_handler = FileHandler('errorlog.txt')
file_handler.setLevel(INFO)
app.logger.addHandler(file_handler)

# App Global variables
app.SEND_SMS = False

api = Api(app, prefix='/GeoVideoApplication/')

api.add_resource(Ping, 'ping/')
api.add_resource(Uplaod, 'upload')
api.add_resource(SpeechToText, 'test')
api.add_resource(Keywords, 'keywords')

if __name__ == '__main__':
    app.run(host='localhost', port=9999, debug=True)
