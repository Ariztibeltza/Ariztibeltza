"""Yes

"""

#   $env:FLASK_APP = 'app.py'
#	flask run --host=0.0.0.0 --port=80
#   Ondoren, amatatzeko Ctrl+C klikatu

#   DATA -> https://flask.palletsprojects.com/en/2.0.x/quickstart/#a-minimal-application
#               Remember that for deployment we have to look here -> https://flask.palletsprojects.com/en/2.0.x/deploying/

from flask import Flask
from flask import render_template
from flask import request
from Kernel import kernel

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index_g.html')                          #Honekin html kodea renderizatuko dugu, zuzenean

@app.route("/login", methods = ['POST', 'GET'])
def login():

    if request.method == 'POST':
        username = request.form.to_dict().get('username')
        password = request.form.to_dict().get('password')
        return render_template('login_g.html.jinja', username = username, password = password)
    else:
        return render_template('login_g.html.jinja')

@app.route("/cmdprompt", methods = ['POST','GET'])           #Hau sortu dugu cmd-tik lortu ditugun datuak maneiatzeko
def data():
    #As we need to get data, we might wnt to do look at this:
    #                   https://stackoverflow.com/questions/10434599/get-the-data-received-in-a-flask-request
    #           ->      https://www.askpython.com/python-modules/flask/flask-forms
    if request.method == 'POST':
        [cmd_id,cmd_args,error,cmd_data,message] = execute_cmd(request.form.to_dict())
        return render_template('cmd_g.html.jinja', cmd_id = cmd_id, cmd_data = cmd_data, error = error, message = message)
    else:
        return render_template('cmd_g.html.jinja')  

## ~~ IMPLEMENTED FUNCTIONS ~~ #########################################################################################################################
## HORRELA LORTU DEZAKEGU ImmutableMultiDict-en barnean dauden elementu guztiak
def execute_cmd(form_dict):
    for element in form_dict:
        [cmd_id,cmd_args,error,cmd_data,message]=kernel.debug(list(form_dict.get(element)))
    return cmd_id,cmd_args,error,cmd_data,message