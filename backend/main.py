from flask import Flask
from flask_restx import Api, Resource, fields

app = Flask(__name__)
api = Api(
    app,
    version="1.0",
    title="Chatbot",
    description="A Simple binary Search Api",
)

ns = api.namespace("binsearch", description="binsearch actions")


binsearch = api.model(
    "binsearch",
    {
        "curr_try": fields.Integer(required=True, description="Current try", default=1),
        "condition":fields.Boolean(required=True, description="Meets the condition?", default=False),
        "initpos": fields.Integer(required=True, description="initial position", default=0),
        "endpos": fields.Integer(required=True, description="final position"),
    },
)

getimage = api.model(
    "image",
    {
        "initpos": fields.Integer(required=True, description="initial position", default=0),
        "endpos": fields.Integer(required=True, description="final position"),
    }
)

@ns.route("/")
class BinSearchList(Resource):
    """Initial iteration entrypoint"""

    @ns.doc("Initial interaction point")
    @ns.expect(getimage)
    @ns.marshal_with(binsearch)
    def get(self):
        """Initial interaction point"""
        return ""
    
@ns.route("/interactive")
class NexIteration(Resource):
    """Get next iteration stap"""

    @ns.doc("Get data to next iteration")
    @ns.expect(binsearch)
    @ns.marshal_with(binsearch)
    def get(self):
        """next iteration data"""
        return ""


if __name__ == '__main__':
    app.run('localhost',8080)