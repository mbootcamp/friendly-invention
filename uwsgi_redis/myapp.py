import redis
from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    r = redis.Redis('redis')
    try:
        r.get('counter')
    except:
        r.set('counter', 0)
    r.incr('counter')
    return "<h1>This page has been visited %s times!</h1>" % r.get('counter')

@application.route("/clear")
def blank():
    r = redis.Redis('redis')
    r.set('counter', 0)
    return "<h1>CLEARED COUNTER TO: %s</h1>" % r.get('counter')

if __name__ == "__main__":
    application.run(host='0.0.0.0')

