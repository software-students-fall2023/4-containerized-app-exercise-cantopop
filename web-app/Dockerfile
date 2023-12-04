# FROM python:3.10
# WORKDIR /app
# COPY requirements.txt /app/
# RUN pip install --no-cache-dir -r requirements.txt
# COPY . /app
# ENV FLASK_APP=main.py
# EXPOSE 5000
# CMD ["flask", "run", "--host=0.0.0.0"]

FROM python:3.10

WORKDIR /web-app 

#Necessary? vvv
# ENV FLASK_APP=app.py
# ENV FLASK_RUN_HOST==0.0.0.0

COPY  . /web-app

RUN pip install pipenv

RUN pipenv --clear

# RUN pip install flask

# RUN pipenv shell

RUN pipenv install

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

# COPY . .

#Necessary? vvv
#MONGO_URI or MONGODB_URI, database as well
ENV MONGODB_URI="mongodb://mongodb:27017"
ENV MONGODB_DATABASE="notes_app"

# CMD ["flask", "run"]

# CMD [ "python3", "-m" , "flask", "run"]

CMD [ "pipenv", "run", "flask", "run"]

# RUN ["flask", "run"]
# ENTRYPOINT ["flask"]
