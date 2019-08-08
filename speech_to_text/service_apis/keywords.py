from flask import request
from flask_restful import Resource
import pdb
import keyword_helper as helper

# pdb.set_trace()

class Keywords(Resource):

    def post(self):
        args = request.get_json()
        sentence = args['sentence']
        keywords = helper.filter_sentence(sentence)
        return {'keywords': keywords}
