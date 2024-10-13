import cv2
import sys

def detect_faces(image_path):
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

    output_path = 'output.jpg'
    cv2.imwrite(output_path, img)
    print(f"Изображение с лицами сохранено как {output_path}")

if __name__ == "__main__":
    image_path = sys.argv[1] if len(sys.argv) > 1 else "test_image.jpg"
    detect_faces(image_path)
