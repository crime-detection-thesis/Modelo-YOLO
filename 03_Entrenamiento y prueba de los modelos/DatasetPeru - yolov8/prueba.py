from ultralytics import YOLO

# Cargar tu modelo entrenado
model = YOLO('runs/detect/pistola_detection_peru2/weights/best.pt')

# Hacer predicción sobre el video
model.predict(
    # Ruta a tu video
    source='Peru_Assault_001.mp4',
    show=True,           # Mostrar la ventana mientras predice
    save=False,           # Guardar el video procesado
    conf=0.5,            # Nivel de confianza (puedes ajustarlo)
)
