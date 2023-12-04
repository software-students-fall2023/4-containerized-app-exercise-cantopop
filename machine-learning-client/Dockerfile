FROM python:3.10

WORKDIR ./machine_learning_client

COPY . .

# RUN pip install pytesseract

# RUN pip install cv2

# RUN pip install pymongo

# RUN pip install 




RUN pip install pipenv

RUN pipenv install 



EXPOSE 3001

#Necessary? vvv
ENV MONGO_URI=mongodb://mongodb:27017

# CMD ["python3", "machine_learning_code.py"]

CMD ["pipenv", "run", "python", "machine_learning_client.py"]]