# To Create folder for new faces and keep them in separate folders.
import os
import shutil
from config import outputFolder
import face_recognition

# This function will create a folder for the person and returns the folder for the known face.
def createPersonFolder(facesKnown, faceEncoding, faceFolders):
    matches = face_recognition.compare_faces(facesKnown, faceEncoding)

    if True in matches:
        # Get the index of the known face match
        matchIndex = matches.index(True)
        faceFolderName = faceFolders[matchIndex]
    else:
        # Create a new folder for the new person (new face)
        faceFolderName = f'person_{len(facesKnown) + 1}'
        faceFolderPath = os.path.join(outputFolder, faceFolderName)

        # Create the new face folder if it doesn't exist
        os.makedirs(faceFolderPath, exist_ok=True)

        # Append the new face and folder to the lists
        faceFolders.append(faceFolderName)
        facesKnown.append(faceEncoding)

        # No match, so matchIndex is set to None
        matchIndex = None

    return matchIndex, faceFolderName

# This will move the image to the face folder.
def moveImage(imagePath, faceFolderName, imageName):
    faceFolderPath = os.path.join(outputFolder, faceFolderName, imageName)
    
    # Copy the image to the corresponding face folder
    shutil.copyfile(imagePath, faceFolderPath)
