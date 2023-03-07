from nipyapi import canvas, config
import sys
#Conectar na API do Apache NiFi
config.nifi_config.host = 'http://0.0.0.0/nifi-api'

#Método para orquestrar determinado Processor via API através de seu ID.
def scheduleProcessor (idProcessor):
    processor = canvas.get_processor(idProcessor,'id')
    if sys.argv[2] == "start":
        #True = Inicia um Processor
        canvas.schedule_processor(processor, True, refresh=True)
    elif sys.argv[2] == "stop":
        #False = Para um Processor
        canvas.schedule_processor(processor, False, refresh=True)
    else:
        return print("Argumento de Start ou Stop inválido.")

scheduleProcessor(sys.argv[1])