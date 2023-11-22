FROM python:3.8
#set work directory insideimage
WORKDIR /app
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# copy current dir contents into image dir
ADD . /app
RUN pip install --upgrade pip
RUN apt -y update
RUN pip install pymongo
ENV DATA_OP=database.py
COPY . /app

EXPOSE 4000

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]