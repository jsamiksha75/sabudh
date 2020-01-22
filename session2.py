from flask import Flask,request,jsonify
app = Flask(__name__)
tasks = [
    {
        'id' :1,
        'value' :'Samiksha',
        'description' :'student'
    },
    {

        'id': 2,
        'value': 'jain',
        'description': 'student'
    }

]
@app.route('/task',method= ['POST'])
def appnd():
    id = tasks[-1]['id'] + 1
    imp = {'id': id,
           'value' : request.json['value'],
           'description' : request.json['description'],}
            
