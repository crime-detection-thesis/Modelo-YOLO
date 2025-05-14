import cv2
from ultralytics import YOLO

# Cargar modelo
model = YOLO('runs/detect/pistola_detection_peru/weights/best.pt')

# Leer y redimensionar la imagen a 640x640
image = cv2.imread('image1.jpg')
image_resized = cv2.resize(image, (640, 640))

# Hacer predicción
results = model.predict(
    source=image_resized,
    show=True,
    save=True,
    conf=0.5
)
