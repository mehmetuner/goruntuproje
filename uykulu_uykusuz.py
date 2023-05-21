import cv2
import dlib
from scipy.spatial import distance as dist
import time
import pygame
import threading
from imutils import face_utils


detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
EAR_THRESHOLD = 0.25
EYE_ASPECT_RATIO_CONSEC_FRAMES = 30
COUNTER = 0
(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]

pygame.init()


def play_sound(filename):
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()


def stop_sound():
    pygame.mixer.music.stop()


def calculate_ear(eye):
    A = dist.euclidean(eye[1], eye[5])
    B = dist.euclidean(eye[2], eye[4])

    C = dist.euclidean(eye[0], eye[3])

    ear = (A + B) / (2.0 * C)
    return ear


cap = cv2.VideoCapture(0)
time.sleep(4)

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = detector(gray, 0)

    for face in faces:
        landmarks = predictor(gray, face)
        landmarks = face_utils.shape_to_np(landmarks)

        left_eye = landmarks[lStart:lEnd]

        right_eye = landmarks[rStart:rEnd]

        left_ear = calculate_ear(left_eye)
        right_ear = calculate_ear(right_eye)

        avg_ear = (left_ear + right_ear) / 2.0

        if avg_ear < EAR_THRESHOLD:
            COUNTER += 1
            if COUNTER >= EYE_ASPECT_RATIO_CONSEC_FRAMES:
                cv2.putText(
                    frame,
                    "Uykulu",
                    (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    (0, 0, 255),
                    2,
                )
                if not pygame.mixer.music.get_busy():
                    threading.Thread(
                        target=play_sound, args=("uyari_sesi.mp3",)
                    ).start()
        else:
            cv2.putText(
                frame,
                "Uykusuz",
                (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 255, 0),
                2,
            )

            if pygame.mixer.music.get_busy():
                threading.Thread(target=stop_sound).start()
            COUNTER = 0

    cv2.imshow("Uykulu/Uykusuz Tespiti", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
