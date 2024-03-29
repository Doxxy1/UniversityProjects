import os
import pickle
import time
import face_recognition
import cv2
import imutils
from imutils import paths
from imutils.video import VideoStream


class Recognition:
    """
    Face recognition class, contains the next 3 functions:
    face_recognition: Takes input from the input device and compares it with the stored embeddings
    face_encode: Takes the images of users and stores the embeddings in the encodings.pickle file
    new_user_reg: Takes 10 pictures for the newly created user  which then calls on the face_encode function
    """

    def __init__(self):
        pass

    def face_recongnition(self):
        # load the known faces and embeddings
        data = pickle.loads(open('encodings.pickle', "rb").read())

        # initialize the video stream and then allow the camera sensor to warm up
        vs = VideoStream(src=0).start()
        time.sleep(2.0)

        # loop over frames from the video file stream
        while True:
            # grab the frame from the threaded video stream
            frame = vs.read()

            # convert the input frame from BGR to RGB then resize it
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            rgb = imutils.resize(frame, width=240)

            # detect the (x, y)-coordinates of the bounding boxes
            # corresponding to each face in the input frame, then compute
            # the facial embeddings for each face
            boxes = face_recognition.face_locations(rgb, model='hog')
            encodings = face_recognition.face_encodings(rgb, boxes)
            names = []

            # loop over the facial embeddings
            for encoding in encodings:
                # attempt to match each face in the input image to our known
                # encodings
                matches = face_recognition.compare_faces(data["encodings"], encoding)

                # check to see if we have found a match
                if True in matches:
                    # find the indexes of all matched faces then initialize a
                    # dictionary to count the total number of times each face
                    # was matched
                    matchedIdxs = [i for (i, b) in enumerate(matches) if b]
                    counts = {}

                    # loop over the matched indexes and maintain a count for
                    # each recognized face face
                    for i in matchedIdxs:
                        name = data["names"][i]
                        counts[name] = counts.get(name, 0) + 1

                    # determine the recognized face with the largest number
                    name = max(counts, key=counts.get)

                # update the list of names
                names.append(name)

            # loop over the recognized faces
            for name in names:
                # identified person
                print("Welcome: " + name)
                # Set a flag to sleep the cam for fixed time
                time.sleep(3.0)
                # do a bit of cleanup
                vs.stop()
                return True, name
            else:
                return False, "Unknown"

    def face_encode(self):
        imagePaths = list(paths.list_images("datasets"))

        # initialize the list of known encodings and known names
        knownEncodings = []
        knownNames = []

        # loop over the image paths
        for (i, imagePath) in enumerate(imagePaths):
            name = imagePath.split(os.path.sep)[-2]

            # load the input image and convert it from RGB (OpenCV ordering)
            # to dlib ordering (RGB)
            image = cv2.imread(imagePath)
            rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            # detect the (x, y)-coordinates of the bounding boxes
            # corresponding to each face in the input image
            boxes = face_recognition.face_locations(rgb,
                                                    model='hog')

            # compute the facial embedding for the face
            encodings = face_recognition.face_encodings(rgb, boxes)

            # loop over the encodings
            for encoding in encodings:
                # add each encoding + name to our set of known names and
                # encodings
                knownEncodings.append(encoding)
                knownNames.append(name)

        # dump the facial encodings + names to disk
        data = {"encodings": knownEncodings, "names": knownNames}
        f = open("encodings.pickle", "wb")
        f.write(pickle.dumps(data))
        f.close()

    def new_user_reg(self, name):
        folder = "./datasets/{}".format(name)

        # Create a new folder for the new name
        if not os.path.exists(folder):
            os.makedirs(folder)

        # Start the camera
        cam = cv2.VideoCapture(0)
        # Set video width
        cam.set(3, 640)
        # Set video height
        cam.set(4, 480)
        # Get the pre-built classifier
        face_detector = cv2.CascadeClassifier("Fdata/haarcascade_frontalface_default.xml")
        scan_status = 0
        img_counter = 0
        while img_counter <= 10:
            key = input("...Scanning face - {} %% complete. Press ENTER to continue! ".format(scan_status))
            if key == "q":
                break

            ret, frame = cam.read()
            if not ret:
                break

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_detector.detectMultiScale(gray, 1.3, 5)

            if len(faces) == 0:
                print("No face detected, please try again")
                continue

            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
                img_name = "{}/{:04}.jpg".format(folder, img_counter)
                cv2.imwrite(img_name, frame[y: y + h, x: x + w])
                img_counter += 1
                scan_status += 10
        cam.release()
