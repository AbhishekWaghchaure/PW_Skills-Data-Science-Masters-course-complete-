import time
from flask import Flask

app =Flask(__name__)

start =time.time()

def elapsed():
    running = time.time() - start
    min,sec =divmod(running,60)
    hr,min = divmod(min, 60)
    return '%d:%02d:%02d' % (hr,min,sec)

@app.route('/')
def route():
    return f'hello every one!! App is running at {elapsed()}'

if __name__  =='__main__':
    app.run(debug=True, host = '0.0.0.0', port = 8070) 