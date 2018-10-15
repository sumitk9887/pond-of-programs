from flask import Flask, request, make_response
from flask_restful import Resource, Api, reqparse, abort
from flask_cors import CORS
import json

from database import helper

"""
    Flask Config
"""

app = Flask(__name__)
app.config['DEBUG'] = False
app.secret_key = "@@@H4CKTOBERFEST_DSC_BVP@@@"

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
api = Api(app)

program_loader = helper.ProgramLoader()

"""
    Resources
"""

class ProgramResource(Resource):
    post_parser = reqparse.RequestParser()
    post_parser.add_argument('name', type=str, required=True)
    post_parser.add_argument('input_args', type=str, action='append')

    get_parser = reqparse.RequestParser()
    get_parser.add_argument('name', type=str, required=True)

    @staticmethod
    def _getProgramInfo(program_name):
        return program_loader.programInfoText(program_name)

    def get(self):
        args = self.get_parser.parse_args()
        program_name = args['name']

        program_info = self._getProgramInfo(program_name)
        program_info_json = json.dumps(program_info)

        response = make_response(program_info_json)

        return response

    @staticmethod
    def _runProgram(program_name, *args, **kwargs):
        program_instance, inputs, outputs = program_loader.programInfo(program_name)

        _args = list(args)

        if(len(_args) > inputs['n']):
            return 'Error, Too Many Inputs'

        for i, (input_type) in enumerate(inputs['types']):
            _args[i] = input_type(_args[i])

        program_output = program_loader.runProgram(program_name, *_args, **kwargs)

        return program_output

    def post(self):
        args = self.post_parser.parse_args()
        print(args.__dict__)
        program_name = args['name']
        input_args = args['input_args']

        output = self._runProgram(program_name, *input_args)
        
        output_json = {
            'output': output
        }
        output_json = json.dumps(output_json)

        return make_response(output_json)

class ProgramsList(Resource):

    @staticmethod
    def _getProgramsList():
        return program_loader.programsInfoList()

    def get(self):
        programs_list = self._getProgramsList()
        programs_list_json = json.dumps(programs_list)
        response = make_response(programs_list_json)

        return response


api.add_resource(ProgramsList, "/api/programs")
api.add_resource(ProgramResource, "/api/program")

if __name__ == "__main__":
    app.run(debug=True)