import os

# Rutas
label_folder = 'valid/labels/'

# Contadores
num_pistola = 0
num_background = 0

# Iteramos por todos los archivos de etiquetas
for label_file in os.listdir(label_folder):
    if label_file.endswith('.txt'):
        with open(os.path.join(label_folder, label_file), 'r') as f:
            lines = f.readlines()
            if not lines:  # Si el archivo está vacío
                num_background += 1
            else:
                has_pistola = any(line.strip().startswith('0')
                                  for line in lines)
                if has_pistola:
                    num_pistola += 1
                else:
                    # Aquí podrías contar otras clases si las tuvieras
                    pass

# Resultados
total = num_pistola + num_background
print(f"Imágenes con pistola: {num_pistola}")
print(f"Imágenes con fondo (background): {num_background}")
print(f"Proporción pistola : background = {num_pistola} : {num_background}")
print(f"Porcentaje de imágenes con pistola: {100 * num_pistola / total:.2f}%")
print(
    f"Porcentaje de imágenes background: {100 * num_background / total:.2f}%")
