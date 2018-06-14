import os
import time
import csv
import requests

http_method = {
    'POST': 0,
    'GET': 1,
    'PUT' :2,
    'DELETE': 3
}

class RobotOfRequisitions(object):

    def __init__(self, number_of_requests, output, method):
        self.number_of_requests = number_of_requests
        self.output = output
        self.method = method
        self.url_default = '127.0.0.1:5000'

    '''
        init requests
    '''
    def start(self):
        pass

    '''
        saves the data
    '''
    def write_data(self):
        pass

if __name__ == '__main__':
    # robo = RobotOfRequisitions()
    pass