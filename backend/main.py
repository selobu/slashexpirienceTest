from flask import Flask
from flask_restx import Api, Resource, fields

app = Flask(__name__)
api = Api(
    app,
    version="1.0",
    title="Chatbot",
    description="A Simple binary Search Api please visit /binsearch",
)
ns = api.namespace("binsearch", description="binsearch actions")


@app.route("/")
def hello_world():
    return "<p>Hello chatbot</p>"


todo = api.model(
    "Todo",
    {
        "id": fields.Integer(readonly=True, description="The task unique identifier"),
        "task": fields.String(required=True, description="The task details"),
    },
)


@ns.route("/")
class TodoList(Resource):
    """Shows a list of all todos, and lets you POST to add new tasks"""

    @ns.doc("list_todos")
    @ns.marshal_list_with(todo)
    def get(self):
        """List all tasks"""
        return ""

    @ns.doc("create_todo")
    @ns.expect(todo)
    @ns.marshal_with(todo, code=201)
    def post(self):
        """Create a new task"""
        return {}, 201
