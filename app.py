

import os

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def hello():

    post_name = request.args.get('post')

    counter_file_name =  '{}_likes.txt'.format(post_name)




    index_file = open('index.html', 'r')
    my_html = index_file.read()
    index_file.close()

    # print(my_html)

    return my_html
