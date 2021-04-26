FROM python:3.5
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
RUN pip3 install --upgrade pip3
ADD requirements.txt /code/
RUN pip3 install -r requirements.txt
ADD . /code/