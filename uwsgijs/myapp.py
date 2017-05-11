import redis
from flask import Flask, render_template
application = app = Flask(__name__)

@app.route('/blog_list.json')
@app.route('/fetch')
def fetch():
    # should grab paginated results from db
    return '''[
             {"url": "http://www.ucla.edu", "display": "UCLA"},
             {"url": "https://www.kernel.org", "display": "KERNEL"},
             {"url": "http://flask.pocoo.org/", "display": "FLAsk"}
            ]'''

# TODO: homework
@app.route('/post/<number:int>')
def post(number):
    return 'TODO: return the post'

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name, footer="foot")

@application.route("/")
def index():
    return render_template('index.html')

@application.route("/clear")
def blank():
    r = redis.Redis('redis')
    r.set('counter', 0)
    return "<h1>CLEARED COUNTER TO: %s</h1>" % r.get('counter')

if __name__ == "__main__":
    application.config['debug'] = True
    application.run(host='0.0.0.0')

