import os
from config import inputFolder , outputFolder
from faceDetection import processImage
from fileOperations import createPersonFolder, moveImage



def imageProcess():
    facesKnown = []
    facesFolders = []

    for img in os.listdir(inputFolder):
        imagePath = os.path.join(inputFolder, img)
        print(f"Processing Image: {img}")
        faceEncodings, faceLocations = processImage(imagePath)


        if not faceEncodings:
            print(f"No faces found in {img}.")
            continue



        for faceEncoding,faceLocation in zip(faceEncodings , faceLocations):
            matchIndex , faceFolderName = createPersonFolder(facesKnown , faceEncoding , facesFolders)


            if matchIndex is None:
                facesKnown.append(faceEncoding)
            
            moveImage(imagePath , faceFolderName , img)

    print(f"Processed images from {inputFolder} and organized into {outputFolder}.")


if __name__ == "__main__":
    print("Welcome to the SnapVault")
    imageProcess()
    print("SnapVault process completed.")