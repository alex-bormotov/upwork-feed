FROM python:3.8.2-slim-buster
ENV LD_LIBRARY_PATH /usr/local/lib
RUN apt-get update && apt-get install -y python3-pip
WORKDIR /upwork-feed
COPY . /upwork-feed
RUN pip3 install -r requirements.txt --no-cache-dir
CMD [ "python3", "./app.py" ]