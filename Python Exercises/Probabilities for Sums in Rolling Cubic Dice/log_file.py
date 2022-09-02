import logging as log

log.basicConfig(level=10,#Nivel de Registro. Default: log.WARNING
                format="%(asctime)s:%(levelname)s [%(filename)s:%(lineno)s] %(message)s",
                datefmt="%A:%B:%I:%M:%S %p",
                handlers=[
                    log.FileHandler("capa_datos.log"), #Para mandar los datos a un archivo según el formato
                    log.StreamHandler() # Para mandar los datos a la consola.Opcional.
                ])