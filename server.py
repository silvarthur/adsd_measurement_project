from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
import psutil
import time

e = create_engine('sqlite:///tasks.db')

app = Flask(__name__)
api = Api(app)

class Task(Resource):
    def get(self):
        server_resp_timei = time.time()

        bd_timei = time.time()
        conn = e.connect()
        query = conn.execute('select * from tasks')
        bd_timef = time.time() - bd_timei

        cpu_usage = psutil.cpu_percent(interval=0.1)

        server_resp_timef = time.time() - server_resp_timei
        print (server_resp_timef)
        return {
            'tasks': [i for i in query.cursor.fetchall()],
            'server_resp': server_resp_timef,
            'bd_time': bd_timef,
            'cpu_usage': cpu_usage
        }

    def post(self):
        server_resp_timei = time.time()

        bd_timei = time.time()
        conn = e.connect()
        title = request.json['title']
        description = request.json['description']
        query = conn.execute("insert into tasks values ('{0}', '{1}')".format(title, description))
        bd_timef = time.time() - bd_timei

        cpu_usage = psutil.cpu_percent(interval=0.1)
        server_resp_timef = time.time() - server_resp_timei

        return {
            'status':'success',
            'server_resp': server_resp_timef,
            'bd_time': bd_timef,
            'cpu_usage': cpu_usage
        }

#class TaskObject(Resource):
#    def get(self, row_id):
#        conn = e.connect()
#        query = conn.execute('SELECT * FROM tasks WHERE rowid={0}'.format(row_id))
#        return {'tasks': [i for i in query.cursor.fetchall()]}

api.add_resource(Task, '/tasks')
#api.add_resource(TaskObject, '/task/<string:row_id>')

if __name__ == '__main__':
    app.run()