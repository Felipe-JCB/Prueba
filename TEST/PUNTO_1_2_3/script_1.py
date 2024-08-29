from pathlib import Path
from io import open
import csv
import numpy as np
import logging
from pydicom import dcmread

def lista_archivos(ruta):
    carpeta = Path(ruta)
    if carpeta.is_dir():
        lista = list(carpeta.iterdir())
        print(f"La ruta: {ruta}\nContiene un total de {len(lista)} elementos.")
        for indice, contenido in enumerate(lista):
            nombre = contenido.parts
            print(f"Archivo #: {indice+1} ---> {nombre[len(nombre)-1]}")
    else:
        print("La ruta no lleva a ninguna carpeta.")

def leer_CSV(ruta_CSV,nombre_CSV):
    Acceso = Path(ruta_CSV) / f"{nombre_CSV}.csv"
    if Acceso.exists():
        with open(Acceso,"r", newline='\n') as fichero_csv:
            lectura = list(csv.reader(fichero_csv, delimiter=','))
            for N_fila, Dato_1 in enumerate(lectura):
                for N_columna, Dato_2 in enumerate(Dato_1):
                    print(f"Fila #: {N_fila+1} con Columna #: {N_columna+1}, {Dato_2} ")

            matriz = np.array(lectura) 

            try:
                C_Age = np.sum((matriz[1:,1]).astype(int))
                C_Weight = np.sum((matriz[1:,2]).astype(int))
                C_Height = np.sum((matriz[1:,3].astype(int)))
                C_Cholesterol = np.sum((matriz[1:,4].astype(int)))
                C_HeartRate = np.sum((matriz[1:,5].astype(int)))

                Media_1 = C_Age / len(matriz[1:,1])
                Media_2 = C_Weight / len(matriz[1:,2])
                Media_3 = C_Height / len(matriz[1:,3])
                Media_4 = C_Cholesterol / len(matriz[1:,4])
                Media_5 = C_HeartRate / len(matriz[1:,5])   

                sumatoria_1,sumatoria_2,sumatoria_3,sumatoria_4,sumatoria_5 = 0,0,0,0,0

                for i in matriz[1:,1].astype(int):
                    sumatoria_1 += (i-Media_1)**2
                for i in matriz[1:,2].astype(int):
                    sumatoria_2 += (i-Media_2)**2
                for i in matriz[1:,3].astype(int):
                    sumatoria_3 += (i-Media_3)**2
                for i in matriz[1:,4].astype(int):
                    sumatoria_4 += (i-Media_4)**2
                for i in matriz[1:,5].astype(int):
                    sumatoria_5 += (i-Media_5)**2     
            
                Desv_standar_1 = np.sqrt(sumatoria_1 / matriz[1:,1].size)
                Desv_standar_2 = np.sqrt(sumatoria_2 / matriz[1:,2].size)
                Desv_standar_3 = np.sqrt(sumatoria_3 / matriz[1:,3].size)
                Desv_standar_4 = np.sqrt(sumatoria_4 / matriz[1:,4].size)
                Desv_standar_5 = np.sqrt(sumatoria_5 / matriz[1:,5].size)
                print()
                print(f"Para la columna de '{matriz[0,1]}'\n La Media calculada es: {Media_1}\n La Desviación estandar calculada es: {Desv_standar_1}")
                print()
                print(f"Para la columna de '{matriz[0,2]}'\n La Media calculada es: {Media_2}\n La Desviación estandar calculada es: {Desv_standar_2}")
                print()
                print(f"Para la columna de '{matriz[0,3]}'\n La Media calculada es: {Media_3}\n La Desviación estandar calculada es: {Desv_standar_3}")
                print()
                print(f"Para la columna de '{matriz[0,4]}'\n La Media calculada es: {Media_4}\n La Desviación estandar calculada es: {Desv_standar_4}")
                print()
                print(f"Para la columna de '{matriz[0,5]}'\n La Media calculada es: {Media_5}\n La Desviación estandar calculada es: {Desv_standar_5}")     
            except TypeError:
                logging.error("Error por tipos de datos, el csv debe ser originalmente texto.")
            except Exception as e:
                print(type(e).__name__)
    else:
        logging.error("FileNotFoundError (Es posible que el directorio al archivo, o el archivo indicado no se hayan encontrado).")

def leer_dicom(ruta_dicom,nombre_dicom,Args):
    Acceso = Path(ruta_dicom) / f"{nombre_dicom}.dcm"
    if Acceso.exists():
        with open(Acceso,'rb') as fichero_dcm:
            lectura_dcm = dcmread(fichero_dcm)
            Nombre_paciente = lectura_dcm[0x0010, 0x0010].value
            Fecha_Estudio = lectura_dcm[0x0008, 0x0020].value
            Modalidad = lectura_dcm[0x0008, 0x0060].value
            print(f"Nombre del paciente: {Nombre_paciente} - Fecha de estudio: {Fecha_Estudio} - Modalidad: {Modalidad}.")

            if len(Args) % 2 == 0:
                for i in range(0,len(Args), 2):
                    print(f"El contenido de las etiquetas ingresadas  son las siguientes:{lectura_dcm[Args[i],Args[i+1]]}")
            else:
                logging.error("El número de etiquetas de los elementos debe ser par.")
    else:
        logging.error("FileNotFoundError (Es posible que el directorio al archivo, o el archivo indicado no se hayan encontrado).")

ruta = input("Ingresa una ruta de un directorio a continuación para comprobar su contenido: ")
lista_archivos(ruta)

ruta_CSV = input("Ingrese la carpeta donde esta el archivo .csv para su análisis: ")
nombre_CSV =  input("Ingrese el nombre del archivo .csv: ")
leer_CSV(ruta_CSV,nombre_CSV)

ruta_dicom = input("Ingrese la carpeta donde esta el archivo DICOM: ")
nombre_dicom =  input("Ingrese el nombre del archivo .dcm: ")
Cantidad_etiquetas = int(input('Digite cuantas etiquetas ingresará: '))
Argumentos = list(range(0,Cantidad_etiquetas))  
for i in Argumentos:
    Argumentos[i] = input(f'Ingrese etiqueta {i+1}: ')
leer_dicom(ruta_dicom,nombre_dicom,Argumentos)