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

    def post(self):
        conn = e.connect()

        title = request.json['title']
        description = request.json['description']

        query = conn.execute("insert into tasks values ('{0}', '{1}')".format(title, description))
        return {'status':'success'}

api.add_resource(Task, '/tasks')

if __name__ == '__main__':
    app.run()