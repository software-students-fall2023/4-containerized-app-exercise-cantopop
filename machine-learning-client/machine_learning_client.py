"""
This is the machine learning client for our project

This is the different configrations for tesseract

#Page segmentation modes:
#0 = Orientation and script detection (OSD) only.
#1 = Automatic page segmentation with OSD.
#2 = Automatic page segmentation, but no OSD, or OCR.
#3 = Fully automatic page segmentation, but no OSD. (Default)
#4 = Assume a single column of text of variable sizes.
#5 = Assume a single uniform block of vertically aligned text.
#6 = Assume a single uniform block of text.
#7 = Treat the image as a single text line.
#8 = Treat the image as a single word.
#9 = Treat the image as a single word in a circle.
#10 = Treat the image as a single character.
#11 = Sparse text. Find as much text as possible in no particular order
#12 = Sparse text with OSD.
#13 = Raw line. Treat the image as a single text line, bypassing hacks that are Tesseract-specific.

#OCR Engine Mode
#0 = Legacy engine only.
#1 = Neural nets LSTM engine only.
#2 = Legacy + LSTM engines.
#3 = Default, based on what is available.
"""
import time
from io import BytesIO
from pymongo import MongoClient
import pytesseract
from PIL import Image


def mlc(raw_image):
    """
    This is the main application of the ML client, we applied the use of Tesseract here.
    """
    # This is the config I found most reliable, do not change!
    # myconfig = r"--psm 6 --oem 3"

    img = Image.open(BytesIO(raw_image))

    # Getting the words...
    text = pytesseract.image_to_string(img)

    # Split the text into lines
    lines = text.split("\n")

    # Separate the first line from the rest
    # title is the title (by default, the first line)
    title = lines[0]
    # content is the remaining of the paragraph
    content = "\n".join(lines[1:])
    return title, content


# Connecting to MongoDB
# pylint: disable=line-too-long
MONGO_URI = "mongodb+srv://admin:admin123@cluster0.m5t5gvu.mongodb.net/?retryWrites=true&w=majority&ssl_cert_reqs=CERT_NONE"
client = MongoClient(MONGO_URI)
# Accessing
database = client["note_app"]
# Accessing
collection = database["temp"]

while True:
    while collection.find_one() is None:
        pass
    document_to_update = collection.find_one()
    DESIRED_KEY = "raw_image"
    DESIRED_VALUE = document_to_update[DESIRED_KEY]
    new_title, new_content = mlc(DESIRED_VALUE)
    if document_to_update:
        collection.update_one(
            {
                "_id": document_to_update["_id"]
            },  # Assuming the document has an _id field
            {"$set": {"title": new_title, "main_body": new_content, "processed": True}},
        )
    # Wait for a specific interval before checking again (e.g., 1 second)
    time.sleep(1)


# Close the MongoDB connection
client.close()
