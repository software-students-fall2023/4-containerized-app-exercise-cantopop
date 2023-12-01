FROM python:3.10

WORKDIR ./machine_learning_client

COPY . .

EXPOSE 3001

#Necessary? vvv
ENV MONGO_URI=mongodb://mongodb:27017

CMD ["pipenv", "run", "python", "machine_learning_code.py"]