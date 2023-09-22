FROM python:3
ADD requirements.txt /
RUN pip install -r requirements.txt

RUN mkdir /app
# ADD iTAFM_V8_next.py /
# ADD testconnection.py /

WORKDIR /app

CMD [ "python", "./app/iTAFM_V8_next.py" ]