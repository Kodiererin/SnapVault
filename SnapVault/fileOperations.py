# To Create folder for new faces and keep them in seperate folders.
import os
import shutil
from config import outputFolder
import face_recognition
# This function will create a folder for the person and returns the folder for the known face.

def createPersonFolder(facesKnown , faceEncoding , faceFolder):
    matches = face_recognition.compare_faces(facesKnown, faceEncoding)

    if True in matches:
        matchIndex = matches.index(True)
        faceFolder = faceFolder[matchIndex]
    else :
        faceFolderName = f'person_{len(facesKnown) + 1}'
        faceFolder = os.path.join(outputFolder, faceFolderName)
        newFaceFolder = os.mkdir(faceFolder)
        os.makedirs(newFaceFolder , exist_ok=True)
        matches.index = True

    return matchIndex , faceFolderName


# This will move the image to the face folder.

def moveImage(imagePath , faceFolderName , imageName):
    faceFolderPath = os.path.join(outputFolder, faceFolderName)
    shutil.copyfile(imagePath, faceFolderPath)
