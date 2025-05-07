import os

# Rutas de las carpetas
carpeta_jpg = 'datasetoriginal/images'
carpeta_txt = 'datasetoriginal/labels'

# Obtener los nombres base (sin extensión) de los archivos .jpg
nombres_jpg = {os.path.splitext(f)[0] for f in os.listdir(
    carpeta_jpg) if f.endswith('.jpg')}

# Recorrer los archivos .txt y eliminar los que no tienen un .jpg correspondiente
for archivo in os.listdir(carpeta_txt):
    if archivo.endswith('.txt'):
        nombre_base = os.path.splitext(archivo)[0]
        if nombre_base not in nombres_jpg:
            ruta_txt = os.path.join(carpeta_txt, archivo)
            os.remove(ruta_txt)
            print(f"Eliminado: {ruta_txt}")
