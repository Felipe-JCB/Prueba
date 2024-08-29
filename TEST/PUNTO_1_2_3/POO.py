from pathlib import Path
from io import open
import logging
from pydicom import dcmread 

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s -%(message)s", filename="POO.log", filemode="a")

class PatientRecord: 

    def __init__(self):

        self._nombre = None
        self._edad = None
        self._fecha_nacimiento = None   
        self._sexo = None
        self._peso = None
        self._id_paciente = None
        self._tipo_id = None

    def __str__(self):
        return f"""DATOS DEL PACIENTE:
                \nNombre: {self._nombre}
                \nEdad: {self._edad}
                \nFecha de nacimiento: {self._fecha_nacimiento}
                \nSexo: {self._sexo}
                \nPeso: {self._peso}
                \nID: {self._id_paciente}
                \nTipo ID: {self._tipo_id}"""

    def Almacenar_paciente(self):
        print(f"INGRESAR DATOS DEL PACIENTE: ")
        paciente_1._nombre = input("Nombre: ")
        paciente_1._edad = input("Edad: ")
        paciente_1._fecha_nacimiento = input("Fecha de nacimiento: ")
        paciente_1._sexo = input("Sexo: ")
        paciente_1._peso = input("Peso: ")
        paciente_1._id_paciente = input("ID: ")
        paciente_1._tipo_id = input("Tipo de ID: ")
    
    def Consultar_paciente(self):
        print(f"""DATOS DEL PACIENTE:
                \nNombre: {self._nombre}
                \nEdad: {self._edad}
                \nFecha de nacimiento: {self._fecha_nacimiento}
                \nSexo: {self._sexo}
                \nPeso: {self._peso}
                \nID: {self._id_paciente}
                \nTipo ID: {self._tipo_id}""")

class StudyRecord(PatientRecord):

    def __init__(self):

        super().__init__()
        
        self._modalidad = None
        self._fecha_estudio = None
        self._hora_estudio = None
        self._id_estudio = None
        self._numero_serie = None
        self._numero_fotogramas = None
    
    def leer_DICOM(self, dir_PATH):
        self.dir_PATH = dir_PATH
        Acceso = Path(self.dir_PATH)
        with open(Acceso,"rb") as fichero_dcm:
            self.lectura_dcm = dcmread(fichero_dcm)
            return self.lectura_dcm

    def __str__(self):
        return super().__str__() + f"""\n\nDATOS DEL ESTUDIO:
                \nModalidad: {self._modalidad}
                \nFecha del estudio: {self._fecha_estudio}
                \nHora del estudio: {self._hora_estudio}
                \nID_Study: {self._id_estudio}
                \nNúmero de serie: {self._numero_serie}
                \nNúmero de fotogramas: {self._numero_fotogramas}"""
    
    def Almacenar_estudio(self,N1,N2):
        try:
            if (N1, N2) in self.lectura_dcm:
                self.Nombre = self.lectura_dcm[N1, N2].name
                self.Dato = self.lectura_dcm[N1, N2].value
                print(f"GUARDADO ({hex(N1)},{hex(N2)}): {self.Nombre} -> {self.Dato}")
                logging.info(f"GUARDADO ({hex(N1)},{hex(N2)}): {self.Nombre} -> {self.Dato}")
                return self.Dato
            else:
                print(f"NO existe el Tag ({hex(N1)},{hex(N2)}). EL DATO NO SE GUARDA")
                logging.warning(f"NO existe el Tag ({hex(N1)},{hex(N2)}). EL DATO NO SE GUARDA")
            return None
        except Exception as e:
            print(str(e))
            logging.error(f"Error al leer el Tag ({hex(N1)},{hex(N2)}): {str(e)}")
         
    def Consultar_estudio(self):
        print(self.__str__())

    def Modificar_estudio(self):        
        print(f"INGRESAR DATOS DEL ESTUDIO: ")
        paciente_1._modalidad = input("Modalidad: ")
        paciente_1._fecha_estudio = input("Fecha de estudio: ")
        paciente_1._hora_estudio = input("Hora de estudio: ")
        paciente_1._id_estudio = input("ID: ")
        paciente_1._numero_serie = input("Numero de serie: ")
        paciente_1._numero_fotogramas = input("Numero de fotogramas: ")

paciente_1 = StudyRecord()
dcm_leido = paciente_1.leer_DICOM(r"C:\Users\Felip\OneDrive\Documentos\IMEXHS\prueba_python\sample-02-dicom.dcm")
print(dcm_leido)
print()
paciente_1.Almacenar_paciente()
print()
paciente_1._modalidad = paciente_1.Almacenar_estudio(0x0008, 0x0060)
paciente_1._fecha_estudio = paciente_1.Almacenar_estudio(0x0008, 0x0020)
paciente_1._hora_estudio = paciente_1.Almacenar_estudio(0x0008, 0x0030)
paciente_1._id_estudio = paciente_1.Almacenar_estudio(0x0020,0x0010)
paciente_1._numero_serie = paciente_1.Almacenar_estudio(0x0020, 0x0011)
paciente_1._numero_fotogramas = paciente_1.Almacenar_estudio(0x0028, 0x0008)
print()
paciente_1.Consultar_estudio()
paciente_1.Modificar_estudio()
paciente_1.Consultar_estudio()