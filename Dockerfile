FROM python:3.8.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
RUN pip3 install --upgrade pip
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/