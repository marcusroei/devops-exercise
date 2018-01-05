
from flask import Flask, request, send_from_directory
from random import randint
import json
# set the project root directory as the static folder, you can set others
smart_app = Flask(__name__, static_url_path='')

post_request_counter = 0
with open('config.json') as json_data_file:
    data = json.load(json_data_file)
port = data.get("port")



@smart_app.route("/", methods = ['POST'])
def handle_post():
    global post_request_counter
    post_request_counter+=1
    print "Counting...."
    return ""

@smart_app.route("/", methods = ['GET'])
def handle_get():
    print post_request_counter
    return str(post_request_counter)

if __name__ == "__main__":
    smart_app.run(host='0.0.0.0', port=port)
