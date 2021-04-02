FROM python:3
ENV PYTHONUNBUFFERED=1
RUN mkdir /zadanie
WORKDIR /zadanie
COPY requirements.txt /zadanie/
ADD . /zadanie/
RUN pip install -r requirements.txt