# 1. Install the libraries
# 2. Recognize the environment
# 3. Recognize the face.
# 4. Create the output folder and save the recognized face.

# Lets do it!!!!

import face_recognition
import os
import shutil


input_folder = 'images'
output_folder = 'output'

# Creating an array to store the faces

facesKnown = []
faceFolder = []

def imageProcessing():
    facesKnown = []
    faceFolder = []

    for img in os.listdir(input_folder):
        imagePath = os.path.join(input_folder, img)

        print("Processing Image: ", imagePath)

        # Lets Load the image!
        image = face_recognition.load_image_file(imagePath)

        faceLoacation = face_recognition.face_locations(image)
        faceEncoding = face_recognition.face_encodings(image, faceLoacation)


print("Welcome to SnapVault") 
print("Lets start recognizing the faces")
imageProcessing()