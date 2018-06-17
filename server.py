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

#class TaskObject(Resource):
#    def get(self, row_id):
#        conn = e.connect()
#        query = conn.execute('SELECT * FROM tasks WHERE rowid={0}'.format(row_id))
#        return {'tasks': [i for i in query.cursor.fetchall()]}

api.add_resource(Task, '/tasks')
#api.add_resource(TaskObject, '/task/<string:row_id>')

if __name__ == '__main__':
    app.run()