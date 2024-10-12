import face_recognition

# Process the image and return the faceEncoding and locations.


def processImage(imagePath):
    image = face_recognition.load_image_file(imagePath)
    faceLocations = face_recognition.face_locations(image)
    faceEncodings = face_recognition.face_encodings(image, faceLocations)
    return faceEncodings, faceLocations    