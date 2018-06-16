import os
import time
import csv
import httplib, urllib
from json import dumps

class RobotOfRequisitions(object):
    def __init__(self):
        self.url_default = '127.0.0.1:5000'

    # Inits requests.
    def start(self):
        pass

    # Gets all data from the database.
    def getContentFromTheDatabase(self):
        conn = httplib.HTTPConnection(self.url_default)

        initial_time = time.time()

        conn.request("GET", "/tasks")

        final_time = time.time()

        total_time = initial_time - final_time

        print 'Response Time - GET request: {0}'.format(total_time)

        conn.close()

    # Sends a task to the dabase.
    def sendContentToTheDatabase(self):
        conn = httplib.HTTPConnection(self.url_default)

        initial_time = time.time()

        params = {"title": "testing...", "description":"testing..."}
        headers = {"Content-type": "application/json", "Accept": "text/plain"}

        conn.request("POST", "/tasks", dumps(params), headers)
        
        final_time = time.time()

        total_time = initial_time - final_time

        print 'Response Time - POST request: {0}'.format(total_time)

        conn.close()

    # Saves the data.
    def write_data(self):
        pass

if __name__ == '__main__':
    myRobot = RobotOfRequisitions()
    myRobot.getContentFromTheDatabase()
    myRobot.sendContentToTheDatabase()