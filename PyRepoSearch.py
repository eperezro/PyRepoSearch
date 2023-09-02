import os
import time
from ftplib import FTP
import subprocess

# Pide al usuario el nombre de la carpeta a buscar
folder_name = input("Introduce el nombre de la carpeta a buscar: ")

# Especifica los repositorios de red
repo1 = r"\\ip repositorio\prueba"
repo2 = "ip ftp"
ftp_folder = "/carpeta ftp/prueba/"
repo3 = r"\\ip repositorio\prueba2"
repo4 = r"\\ip repositorio\prueba3"


# Establece el tiempo máximo de búsqueda en cada repositorio (en segundos)
max_search_time = 10

# Busca en el primer repositorio
print(f"Buscando en {repo1}...")
start_time = time.time()
for root, dirs, files in os.walk(repo1):
    for dir in dirs:
        if folder_name in dir.lower():
            print(f"Carpeta encontrada: {os.path.join(root, dir)}")
    if time.time() - start_time > max_search_time:
        print("Tiempo máximo de búsqueda alcanzado")
        break



# Busca en el segundo repositorio (FTP)
print(f"Buscando en ftp://{repo2}{ftp_folder}...")
start_time = time.time()
try:
    with FTP(repo2, encoding='latin1') as ftp:
        ftp.login()
        ftp.cwd(ftp_folder)
        for folder in ftp.nlst():
            if folder_name in folder.lower():
                print(f"Carpeta encontrada: ftp://{repo2}{os.path.join(ftp_folder, folder)}")
            if time.time() - start_time > max_search_time:
                print("Tiempo máximo de búsqueda alcanzado")
                break
except Exception as e:
    print(f"Error al buscar en el repositorio FTP: {e}")

# Busca en el tercer repositorio
print(f"Buscando en {repo3}...")
start_time = time.time()
for root, dirs, files in os.walk(repo3):
    for dir in dirs:
        if folder_name in dir.lower():
            print(f"Carpeta encontrada: {os.path.join(root, dir)}")
    if time.time() - start_time > max_search_time:
        print("Tiempo máximo de búsqueda alcanzado")
        break

# Busca en el cuarto repositorio
print(f"Buscando en {repo4}...")
start_time = time.time()
for root, dirs, files in os.walk(repo4):
    for dir in dirs:
        if folder_name in dir.lower():
            print(f"Carpeta encontrada: {os.path.join(root, dir)}")
    if time.time() - start_time > max_search_time:
        print("Tiempo máximo de búsqueda alcanzado")
        break



# Espera a que el usuario presione una tecla antes de cerrar la ventana
input("Presiona cualquier tecla para salir...")
