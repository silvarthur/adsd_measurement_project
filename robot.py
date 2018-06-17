import os
import time
import csv
import ast
import httplib, urllib
from json import dumps

http_method = {
    'POST': 0,
    'GET': 1,
    'PUT' :2,
    'DELETE': 3
}

class RobotOfRequisitions(object):

    def __init__(self, method, number_of_requests = 1, output = None):
        self.url_default = '127.0.0.1:5000'
        self.number_of_requests = number_of_requests
        self.method = method
        self.output = output

    # Inits requests.
    def start(self):
        if self.method == 1 and self.number_of_requests == 1:
            self.getContentFromTheDatabase()
        elif self.method == 1 and self.number_of_requests > 1:
            self.getContentFromTheDatabaseMultipleTimes(self.number_of_requests)
        elif self.method == 0 and self.number_of_requests == 1:
            self.sendContentToTheDatabase()
        elif self.method == 0 and self.number_of_requests > 1:
            self.sendContentToTheDatabaseMultipleTimes(self.number_of_requests)

    # Gets all data from the database.
    def getContentFromTheDatabase(self):
        conn = httplib.HTTPConnection(self.url_default)

        initial_time = time.time()

        conn.request("GET", "/tasks")

        # value may be incorrect
        total_time = time.time() - initial_time

        response = ast.literal_eval(conn.getresponse().read())
        server_resp = response['server_resp']
        bd_time = response['bd_time']
        cpu_usage = response['cpu_usage']

        self.write_data('GET', total_time, server_resp, bd_time, cpu_usage)
        conn.close()

    def getContentFromTheDatabaseMultipleTimes(self, times):
        initial_time = time.time()
        # time of each requisition
        wait_time = 60 / times
        for i in range(0, times):
            self.getContentFromTheDatabase()
            time.sleep(wait_time)

        total_time = time.time() - initial_time

        print ('Response Time - All GET requests: {0}'.format(total_time))

    # Sends a task to the dabase.
    def sendContentToTheDatabase(self):
        conn = httplib.HTTPConnection(self.url_default)

        initial_time = time.time()

        params = {
            "title": "testing...",
            "description":"testing..."
        }
        headers = {
            "Content-type": "application/json",
            "Accept": "text/plain"
        }

        conn.request("POST", "/tasks", dumps(params), headers)
        # value may be incorrect
        total_time = time.time() - initial_time

        response = ast.literal_eval(conn.getresponse().read())
        server_resp = response['server_resp']
        bd_time = response['bd_time']
        cpu_usage = response['cpu_usage']

        self.write_data('POST', total_time, server_resp, bd_time, cpu_usage)

        print ('Response Time - POST request: {0}'.format(total_time))

        conn.close()

    def sendContentToTheDatabaseMultipleTimes(self, times):
        initial_time = time.time()
        # time of each requisition
        wait_time = 60 / times
        for i in range(0, times):
            self.sendContentToTheDatabase()
            time.sleep(wait_time)

        total_time = time.time() - initial_time

        print ('Response Time - All POST requests: {0}'.format(total_time))

    # Saves the data.
    def write_data(self, command, total_time, server_response, bd_response, cpu_usage):
        fd = open(self.output, 'a')
        output = csv.writer(fd, delimiter=' ', lineterminator="\n")
        output.writerow([command, total_time, server_response, bd_response, cpu_usage])
        fd.close()

if __name__ == '__main__':
    # you have to rename the files you need to save
    myRobot = RobotOfRequisitions(http_method['GET'], output = 'data-set/teste.csv')
    myRobot.start()
    myRobot = RobotOfRequisitions(http_method['GET'], 10, output='data-set/teste2.csv')
    myRobot.start()
    myRobot = RobotOfRequisitions(http_method['POST'], output='data-set/teste.csv')
    myRobot.start()
    myRobot = RobotOfRequisitions(http_method['POST'], 10, output='data-set/teste2.csv')
    myRobot.start()