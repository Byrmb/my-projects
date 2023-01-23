

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World from Flask!!!"


@app.route('/second')
def second():
    return 'Bize Her Yer Dünya!!!!'









if __name__ == '__main__':
    app.run(debug=True, port=5000)













