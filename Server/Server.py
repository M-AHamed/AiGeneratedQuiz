# Server main code file
# author: Mohammad Hamed
# date: 04/12/2023

# server is gonna be responsible for handling the requests from the client
# forms the queries to send to open ai api, and sends the response back to the client

import socket
import threading
import json
import requests
import os
import sys
import time
import random
import string
import re
import datetime

# import the openai api key
from env import OPENAI_API_KEY
api_key =   OPENAI_API_KEY

# things to do 
# 1. create a socket
# 2. bind the socket to an ip address and port
# 3. listen for connections
# 4. accept connections
# 5. receive data from the client
# 6. send data to the client
# 7. close the connection

# 
# create a socket
#
def create_socket():
    try:
        global host
        global port
        global s
        host = ""
        port = 9999
        s = socket.socket()
    except socket.error as msg:
        print("Socket creation error: " + str(msg))

#
# bind the socket to an ip address and port
#
def bind_socket():
    try:
        global host
        global port
        global s
        print("Binding the port: " + str(port))
        s.bind((host, port))
        s.listen(5)
    except socket.error as msg:
        print("Socket binding error: " + str(msg) + "\n" + "Retrying...")
        bind_socket()

#
# accept connections
#
def accept_connections():
    while True:
        try:
            conn, address = s.accept()
            print("Connection has been established | " + "IP " + address[0] + " | Port " + str(address[1]))
            # start the thread to handle the client
            thread = threading.Thread(target=handle_client, args=(conn,))
            thread.start()
        except socket.error as msg:
            print("Error accepting connections: " + str(msg))

#
# handle the client
# 
def handle_client(conn):
    pass

# query the openai api
def query_api(prompt, api_key):
    # set the url
    url = "https://api.openai.com/v1/engines/davinci/completions"
    # set the headers
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + api_key
    }
    # set the data
    data = {
        "prompt": prompt,
        "max_tokens": 100,
        "temperature": 0.9,
        "top_p": 1,
        "n": 1,
        "stream": False,
        "logprobs": None,
        "stop": ["\n"]
    }
    # make the request
    response = requests.post(url, headers=headers, data=json.dumps(data))
    # return the response
    return response.json()
