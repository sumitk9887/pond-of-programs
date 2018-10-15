from flask import Flask, request, make_response
from flask_restful import Resource, Api, reqparse, abort
from flask_cors import CORS

from database import program

"""
    Flask Config
"""

app = Flask(__name__)
app.config['DEBUG'] = False
app.secret_key = "@@@H4CKTOBERFEST_DSC_BVP@@@"

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
api = Api(app)

PROGRAM_FOLDER = "programs"

"""
    Resources
"""

class ProgramResource(Resource):
    post_parser = reqparse.RequestParser()
    post_parser.add_argument('input_args', type=str, action='append')

    def _getProgramInfo(self, program_name):
        return programInfo(program_name)

    def get(self, program_name):
        program_info = self._getProgramInfo(program_name)
        return program_info

    def post(self, program_name):
        args = post_parser.parse_args()
        program_info = self._getProgramInfo(program_name)

        

class ProgramsList(Resource):

    def get(self):
        program_list = getProgramList()
        response = make_response(program_list)

        return response


api.add_resource(ProgramsList, "/api/programs")
api.add_resource(ProgramResource, "/api/<string:program_name>")

if __name__ == "__main__":
    app.run(debug=True)