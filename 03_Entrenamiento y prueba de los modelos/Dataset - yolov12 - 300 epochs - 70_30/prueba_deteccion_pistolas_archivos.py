from ultralytics import YOLO

# Cargar el modelo
model = YOLO('runs/detect/pistola_detection_peru/weights/best.pt')

# Procesar el video directamente
results = model.predict(
    source='imagenes.jpg',   # Ruta del video
    conf=0.1,              # Umbral de confianza
    show=True,             # Muestra detecciones en tiempo real (si es posible)
    save=True              # Guarda el video procesado en runs/detect/predict
)
