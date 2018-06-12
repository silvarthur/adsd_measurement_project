from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine

e = create_engine('sqlite:///tasks.db')

app = Flask(__name__)
api = Api(app)

class Task(Resource):
    def get(self):
        conn = e.connect()
        query = conn.execute('select * from tasks')
        return {'tasks': [i for i in query.cursor.fetchall()]}

api.add_resource(Task, '/tasks')

if __name__ == '__main__':
    app.run()