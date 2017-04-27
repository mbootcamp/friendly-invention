import redis
from flask import Flask, render_template
application = app = Flask(__name__)

@app.route('/fetch')
def fetch():
    return '''[
             {"url": "http://www.ucla.edu", "display": "UCLA"},
             {"url": "https://www.kernel.org", "display": "KERNEL"},
             {"url": "http://flask.pocoo.org/", "display": "FLAsk"}
            ]'''

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name, footer="foot")

@application.route("/")
def index():
    r = redis.Redis('redis')
    try:
        r.get('counter')
    except:
        r.set('counter', 0)
    r.incr('counter')
    counter = r.get('counter')
    return render_template('index.html', counter=counter)
    #return "<h1>This page has been visited %s times!</h1>" % r.get('counter')

@application.route("/clear")
def blank():
    r = redis.Redis('redis')
    r.set('counter', 0)
    return "<h1>CLEARED COUNTER TO: %s</h1>" % r.get('counter')

if __name__ == "__main__":
    application.config['debug'] = True
    application.run(host='0.0.0.0')

