# FROM python:3.10
# WORKDIR /app
# COPY requirements.txt /app/
# RUN pip install --no-cache-dir -r requirements.txt
# COPY . /app
# ENV FLASK_APP=main.py
# EXPOSE 5000
# CMD ["flask", "run", "--host=0.0.0.0"]

FROM python:3.10

WORKDIR ./web-app 

#Necessary? vvv
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST==0.0.0.0

COPY  . /web-app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

COPY . .

#Necessary? vvv
ENV MONGO_URI=mongodb://mongodb:27017

CMD ["flask", "run"]