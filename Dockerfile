FROM python:3.9-bullseye

#set work directory insideimage
WORKDIR /any

# copy current dir contents into image dir
ADD . /any

RUN pip install --upgrade pip
RUN apt -y update
RUN pip install pymongo
ENV DATA_OP=database.py
COPY . .

EXPOSE 4000

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]