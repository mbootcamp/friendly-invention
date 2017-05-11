FROM ubuntu
RUN apt-get update -y
RUN apt-get install -y python-pip
ADD uwsgi_redis/requirements.txt requirements.txt
RUN pip install -r requirements.txt
ADD uwsgi_redis /app
WORKDIR /app
CMD uwsgi --socket 0.0.0.0:8000 --protocol=http -w wsgi
