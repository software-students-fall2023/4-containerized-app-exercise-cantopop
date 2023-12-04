FROM python:3.11

WORKDIR /machine_learning_client

COPY . .

RUN apt-get update && \
    apt-get install -y tesseract-ocr && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN pip install pipenv

RUN pipenv install 

EXPOSE 3001

CMD ["pipenv", "run", "python", "machine_learning_client.py"]