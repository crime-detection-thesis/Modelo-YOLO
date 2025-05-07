import os
import shutil

# Rutas de entrada
images_folder = 'valid/images/'
labels_folder = 'valid/labels/'

# Rutas de salida
output_pistola = 'valid/pistola/'
output_no_pistola = 'valid/no_pistola/'

# Crear carpetas si no existen
os.makedirs(output_pistola + 'images/', exist_ok=True)
os.makedirs(output_pistola + 'labels/', exist_ok=True)
os.makedirs(output_no_pistola + 'images/', exist_ok=True)
os.makedirs(output_no_pistola + 'labels/', exist_ok=True)

# Procesar todos los archivos de etiquetas
for label_file in os.listdir(labels_folder):
    if label_file.endswith('.txt'):
        label_path = os.path.join(labels_folder, label_file)
        image_name = os.path.splitext(label_file)[0]

        # Soporta extensiones .jpg y .png
        image_path_jpg = os.path.join(images_folder, image_name + '.jpg')
        image_path_png = os.path.join(images_folder, image_name + '.png')

        # Leer contenido del archivo de etiquetas
        with open(label_path, 'r') as f:
            lines = f.readlines()

        has_pistola = any(line.strip().startswith('0') for line in lines)

        # Determinar destino según si contiene clase "0"
        if has_pistola:
            dest_img = output_pistola + 'images/'
            dest_lbl = output_pistola + 'labels/'
        else:
            dest_img = output_no_pistola + 'images/'
            dest_lbl = output_no_pistola + 'labels/'

        # Copiar etiqueta
        shutil.copy(label_path, os.path.join(dest_lbl, label_file))

        # Copiar imagen (verifica si es .jpg o .png)
        if os.path.exists(image_path_jpg):
            shutil.copy(image_path_jpg, os.path.join(
                dest_img, image_name + '.jpg'))
        else:
            print(f"[ADVERTENCIA] Imagen no encontrada para: {image_name}")
