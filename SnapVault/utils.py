# Lets compare the faces and return the result.


import face_recognition

def compareFaces(faceEncodings, faceLocations):
    return face_recognition.compare_faces(faceEncodings, faceLocations)

