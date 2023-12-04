FROM python:3.11

WORKDIR /machine_learning_client

COPY . .

# RUN pip install pytesseract

# RUN pip install cv2

# RUN pip install pymongo

# RUN pip install 




RUN pip install pipenv

RUN pipenv install 


RUN pip install --no-cache-dir -r requirements.txt

# Install Tesseract OCR
RUN apt-get update && \
    apt-get install -y tesseract-ocr && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

EXPOSE 3001

#Necessary? vvv
#MONGO_URI or MONGODB_URI, database as well
ENV MONGODB_URI="mongodb://mongodb:27017"
ENV MONGODB_DATABASE="notes_app"

# CMD ["python3", "machine_learning_code.py"]

CMD ["pipenv", "run", "python", "machine_learning_client.py"]