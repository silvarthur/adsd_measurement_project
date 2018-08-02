from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from datetime import datetime
import psutil
import time
import csv
import os

e = create_engine('sqlite:///tasks.db')

app = Flask(__name__)
api = Api(app)

class Task(Resource):
    def get(self):
        log = request.args.get('log')

        server_resp_timei = time.time()
        bd_timei = time.time()
        conn = e.connect()
        query = conn.execute('select * from tasks')
        bd_timef = time.time() - bd_timei
        tasks = [i for i in query.cursor.fetchall()]

        if log == 'true':
            fd = open('log-get.csv', 'a')
            output = csv.writer(fd, delimiter=' ', lineterminator="\n")
            output.writerow([tasks, datetime.now()])
            fd.close()

        cpu_usage = psutil.cpu_percent(interval=0.1)

        pid = os.getpid()
        py = psutil.Process(pid)
        memory_usage = py.memory_info()[0] / 2. ** 30  # memoria usada em GB

        server_resp_timef = time.time() - server_resp_timei

        return {
            'tasks': tasks,
            'server_resp': server_resp_timef,
            'bd_time': bd_timef,
            'cpu_usage': cpu_usage,
            'memory_usage': memory_usage
        }

    def post(self):
        log = request.args.get('log')
        server_resp_timei = time.time()

        bd_timei = time.time()
        conn = e.connect()
        title = request.json['title']
        description = request.json['description']
        query = conn.execute("insert into tasks values ('{0}', '{1}')".format(title, description))
        bd_timef = time.time() - bd_timei

        if log == 'true':
            fd = open('log-post.csv', 'a')
            output = csv.writer(fd, delimiter=' ', lineterminator="\n")
            output.writerow([(title, description), datetime.now()])
            fd.close()

        cpu_usage = psutil.cpu_percent(interval=0.1)

        pid = os.getpid()
        py = psutil.Process(pid)
        memory_usage = py.memory_info()[0] / 2. ** 30  # memoria usada em GB

        server_resp_timef = time.time() - server_resp_timei

        return {
            'task': {'title': title, 'description': description},
            'status':'success',
            'server_resp': server_resp_timef,
            'bd_time': bd_timef,
            'cpu_usage': cpu_usage,
            'memory_usage': memory_usage
        }


api.add_resource(Task, '/tasks')
if __name__ == '__main__':
    app.run()