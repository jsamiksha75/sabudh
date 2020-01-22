from flask import Flask,jsonify

app= Flask(__name__)
@app.route("/")
def abc():
    lst = [
        { "YOU ARE BEAUTIFUL":'Mikshu'}
    ]

    return jsonify(lst)
if __name__ == '__main__':
    app.run()