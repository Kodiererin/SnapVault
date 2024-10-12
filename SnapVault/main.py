import face_recognition
import os
import shutil

input_folder = 'images'
output_folder = 'output'

# Array to store known faces and folders for each face
facesKnown = []
faceFolder = []

def imageProcessing():
    global facesKnown, faceFolder

    # Iterate over each image in the folder
    for img in os.listdir(input_folder):
        imagePath = os.path.join(input_folder, img)

        print("Processing Image: ", imagePath)

        # Load the image
        image = face_recognition.load_image_file(imagePath)

        # Find all face locations and encodings in the image
        faceLocations = face_recognition.face_locations(image)
        faceEncodings = face_recognition.face_encodings(image, faceLocations)

       
# Start the process
print("Welcome to SnapVault") 
print("Let's start recognizing the faces")
imageProcessing()
