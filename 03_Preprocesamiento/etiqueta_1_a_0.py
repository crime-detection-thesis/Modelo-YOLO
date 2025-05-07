import os

# Carpeta de etiquetas
label_folder = 'valid/labels/'

# Recorremos todos los archivos .txt en la carpeta
for label_file in os.listdir(label_folder):
    if label_file.endswith('.txt'):
        file_path = os.path.join(label_folder, label_file)
        with open(file_path, 'r') as f:
            lines = f.readlines()

        new_lines = []
        for line in lines:
            parts = line.strip().split()
            if parts:  # evitar líneas vacías
                if parts[0] == '1':
                    parts[0] = '0'  # cambiar clase 1 a clase 0
                new_lines.append(' '.join(parts))

        # Sobrescribir el archivo con las líneas modificadas
        with open(file_path, 'w') as f:
            f.write('\n'.join(new_lines) + '\n' if new_lines else '')
