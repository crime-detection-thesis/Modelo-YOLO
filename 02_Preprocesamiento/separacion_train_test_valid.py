import os
import shutil
import random

# Carpetas de entrada
images_folder = 'images/'
labels_folder = 'labels/'

# Salida
output_base = 'dataset_split_stratified/'
splits = ['train', 'valid', 'test']
split_ratio = [0.7, 0.15, 0.15]  # 70%, 15%, 15%

# Crear carpetas de salida
for split in splits:
    os.makedirs(os.path.join(output_base, split, 'images'), exist_ok=True)
    os.makedirs(os.path.join(output_base, split, 'labels'), exist_ok=True)

# Clasificar archivos en dos listas: pistola y no_pistola
pistola_files = []
no_pistola_files = []

for label_file in os.listdir(labels_folder):
    if label_file.endswith('.txt'):
        label_path = os.path.join(labels_folder, label_file)
        image_name = os.path.splitext(label_file)[0]
        image_path_jpg = os.path.join(images_folder, image_name + '.jpg')
        image_path_png = os.path.join(images_folder, image_name + '.png')

        # Verificar que exista la imagen correspondiente
        image_path = None
        if os.path.exists(image_path_jpg):
            image_path = image_path_jpg
        elif os.path.exists(image_path_png):
            image_path = image_path_png

        if not image_path:
            continue  # saltar si no hay imagen correspondiente

        with open(label_path, 'r') as f:
            lines = f.readlines()
            has_pistola = any(line.strip().startswith('0') for line in lines)

        entry = (image_path, label_path)
        if has_pistola:
            pistola_files.append(entry)
        else:
            no_pistola_files.append(entry)

# Función para dividir estratificadamente


def stratified_split(entries):
    random.shuffle(entries)
    total = len(entries)
    train_end = int(total * split_ratio[0])
    valid_end = train_end + int(total * split_ratio[1])
    return {
        'train': entries[:train_end],
        'valid': entries[train_end:valid_end],
        'test': entries[valid_end:]
    }


# Dividir ambos grupos
split_pistola = stratified_split(pistola_files)
split_no_pistola = stratified_split(no_pistola_files)

# Función para copiar archivos a carpeta correspondiente


def copy_entries(entries, split_name):
    for img_path, label_path in entries:
        img_name = os.path.basename(img_path)
        lbl_name = os.path.basename(label_path)
        shutil.copy(img_path, os.path.join(
            output_base, split_name, 'images', img_name))
        shutil.copy(label_path, os.path.join(
            output_base, split_name, 'labels', lbl_name))


# Copiar archivos para cada conjunto
for split in splits:
    copy_entries(split_pistola[split], split)
    copy_entries(split_no_pistola[split], split)

# Reporte final
print("Distribución final:")
for split in splits:
    total_split = len(split_pistola[split]) + len(split_no_pistola[split])
    pistola_count = len(split_pistola[split])
    no_pistola_count = len(split_no_pistola[split])
    print(f"{split.upper()}: {total_split} imágenes — {pistola_count} pistola / {no_pistola_count} background")
