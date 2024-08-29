from pathlib import Path 
from io import open
import json
import logging
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s -%(message)s", filename="hilo.log", filemode="a")

def numeros_pares():
    for i in range(0,201,2):
        print(i, end=" ")
        time.sleep(0.5)
def numeros_impares():
    for i in range(1,201,2):
        print(i, end=" ")
        time.sleep(0.5)

# Función para procesar cada elemento del JSON
def procesar_elemento(elemento):
    element_id = elemento["id"]
    data = elemento["data"]
    logging.info(f"Procesando elemento ID: {element_id}")
    print(f"ID del elemento: {element_id}")

    # Convierte los datos en listas de números
    data_lista = []
    for linea in data:
        data_lista += [int(x) for x in linea.split()]

    promedio_antes = sum(data_lista) / len(data_lista)
    logging.info(f"Promedio antes de normalización para ID {element_id}: {promedio_antes}")
    print(f"Promedio antes de normalización: {promedio_antes}")

    max_valor = max(data_lista)
    data_normalizada = [x / max_valor for x in data_lista]

    promedio_despues = sum(data_normalizada) / len(data_normalizada)
    logging.info(f"Promedio después de normalización para ID {element_id}: {promedio_despues}")
    print(f"Promedio después de normalización: {promedio_despues}")

    tamaño = len(data_lista)
    logging.info(f"Tamaño de los datos para ID {element_id}: {tamaño}")
    print(f"Tamaño de los datos: {tamaño}")

def procesar_json(ruta_json, nombre_json):
    Acceso = Path(ruta_json) / f"{nombre_json}.json"
    if Acceso.exists():
        try:
            with open(Acceso, 'r') as fichero_json:
                lectura = json.load(fichero_json)
        except Exception as e:
            logging.error(f"Error al leer el archivo JSON: {e}")
    else:
        logging.error(f"El archivo {nombre_json} no existe en la ruta especificada")

    with ThreadPoolExecutor(max_workers=4) as hilos:
        futuros = []
        for key, value in lectura.items():
            futuros.append(hilos.submit(procesar_elemento, value))
        # Asegura que no se creen más de 4 hilos simultáneamente
        for futuro in as_completed(futuros):
            futuro.result()

with ThreadPoolExecutor(max_workers=2) as hilos:
    hilos.submit(numeros_pares)
    hilos.submit(numeros_impares)
print()
print()
ruta_C = input("Ingrese la carpeta donde esta el archivo .json: ")
ruta_A =  input("Ingrese el nombre del archivo .json: ")
procesar_json(ruta_C,ruta_A)