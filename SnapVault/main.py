import os

def imageProcess():
    facesKnown = []
    facesFolders = []

    for img in os.listdir(inputFolder):
        