
from flask import Flask, request, send_from_directory
from random import randint
import json
import os

# set the project root directory as the static folder, you can set others.
app = Flask(__name__, static_url_path='')

dir = os.path.dirname(__file__)
filename = os.path.join(dir, 'config.json')


with open(filename) as json_data_file:
    data = json.load(json_data_file)
port = data.get("port")

@app.route("/", methods = ['GET'])
def root():
    random_panda = "panda{0}.jpg".format(randint(1, 6))
    print random_panda
    return send_from_directory('resources', random_panda)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=port)
