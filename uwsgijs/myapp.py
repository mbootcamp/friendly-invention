import redis
from flask import Flask, render_template, request, url_for, jsonify
from sqlalchemy import create_engine

application = app = Flask(__name__)
pgdb = create_engine('postgresql://ubuntu@/ubuntu')

@app.route('/blog_list.json')
@app.route('/fetch')
def fetch():
    # should grab paginated results from db
    top_posts = pgdb.execute('SELECT id,title FROM posts ORDER BY id DESC LIMIT 10')
    return jsonify([{ 'url': url_for('post', post_id=row[0]), 'display': row[1]}
        for row in top_posts ])


def _get_post(post_id):
    # TODO: fetch from database
    query = 'SELECT title,body FROM posts WHERE id=%s LIMIT 1' % post_id
    post = pgdb.execute(query).fetchone()
    return {'title': post[0], 'body': post[1]}


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


#@app.route('/login', methods=['GET', 'POST'])
#def login():
#    if request.method == 'POST':
#        do_the_login()
#    else:
#        show_the_login_form()
@application.route("/post", methods=['GET', 'POST'])
def new_post():
    if request.method == 'POST':
        # request.form['title'] to access form title
        # insert the post
        return 'implemented as homework' + request.form['title']
        # redirect to the post
    else:
        return render_template('forms.html', nav_name="post")


@application.route("/", methods=['HEAD','GET','SOMERANDOMSTUFF'])
def index():
    return render_template('index.html', nav_name="blog")


@application.route("/clear")
def blank():
    r = redis.Redis('redis')
    r.set('counter', 0)
    return "<h1>CLEARED COUNTER TO: %s</h1>" % r.get('counter')


@application.route("/postvar")
def postcars():
    return render_template('postvar.html')


if __name__ == "__main__":
    application.config['debug'] = True
    application.run(host='0.0.0.0')

