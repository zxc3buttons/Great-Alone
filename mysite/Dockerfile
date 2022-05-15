FROM python:3

WORKDIR /mysite

COPY manage.py /mysite/
COPY requirements.txt ./

RUN pip install -r requirements.txt

CMD ['python']