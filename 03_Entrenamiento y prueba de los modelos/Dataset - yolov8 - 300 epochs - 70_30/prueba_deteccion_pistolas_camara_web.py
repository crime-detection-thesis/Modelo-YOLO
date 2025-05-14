import cv2
from ultralytics import YOLO

# Cargar el modelo
model = YOLO('runs/detect/pistola_detection_peru/weights/best.pt')

# Abrir la cámara
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("No se pudo acceder a la cámara.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Realizar predicción sobre el frame
    results = model.predict(source=frame, conf=0.1, save=False, show=False)

    # Dibujar las cajas en el frame
    annotated_frame = results[0].plot()

    # Mostrar el resultado
    cv2.imshow("Detección con YOLO", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
