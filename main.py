import cv2
import sys
import os

def detect_faces(image_path, scale_factor=0.3):
    face_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')

    img = cv2.imread(image_path)
    if img is None:
        print(f"Не удалось загрузить изображение: {image_path}")
        return

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    print(f"Найдено {len(faces)} лиц")

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    img_resized = cv2.resize(img, (0, 0), fx=scale_factor, fy=scale_factor)

    cv2.imshow('Detected Faces', img_resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.realpath(__file__))
    default_image_path = "./test_image.jpg"
    
    image_path = sys.argv[1] if len(sys.argv) > 1 else default_image_path
    detect_faces(image_path)
