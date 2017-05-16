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

def _get_post(post_id):
    # TODO: fetch from database
    return {'content': 'content '*24, 'title': 'title '*3}

# TODO: homework
@app.route('/post/<int:post_id>')
def post(post_id):
    post = _get_post(post_id)
    return render_template('post.html', post=post)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name, footer="foot")

@application.route("/about")
def about():
    return render_template('about.html')

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

