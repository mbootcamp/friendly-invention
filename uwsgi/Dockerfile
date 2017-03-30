FROM ubuntu
RUN apt-get update -y
RUN apt-get install -y python-pip
ADD uwsgi/requirements.txt requirements.txt
RUN pip install -r requirements.txt
ADD uwsgi/myapp.py myapp.py
ADD uwsgi/wsgi.py wsgi.py
CMD uwsgi --socket 0.0.0.0:8000 --protocol=http -w wsgi
