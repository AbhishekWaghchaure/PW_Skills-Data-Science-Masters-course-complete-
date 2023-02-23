#to create api we use flask 
from flask import Flask

app = Flask(__name__)

@app.route('/')
def function():
    return 'Hello World'

@app.route('/addition')
def function1():
    a = 10 + 1
    return 'addition is : '.format(a)
    
if __name__ == '__main__':
    app.run(debug=True, port=8001)