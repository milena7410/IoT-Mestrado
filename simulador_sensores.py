import random
import time
import paho.mqtt.client as cliente_mqtt

SERVIDOR_BROKER = "broker.emqx.io"
PORTA_BROKER = 1883

cliente = cliente_mqtt.Client(
    callback_api_version=cliente_mqtt.CallbackAPIVersion.VERSION2,
    client_id="Publicador_Sensores_CentroDeDados",
)

cliente.connect(SERVIDOR_BROKER, PORTA_BROKER, 60)

print("Iniciando a publicação dos dados dos sensores do Datacenter...")

try:
    while True:
        for id_sala in range(1, 4):
            #simula leituras de temperatura e umidade
            temperatura = round(random.uniform(15.0, 32.0), 1)
            umidade = round(random.uniform(35.0, 65.0), 1)

            topico_temperatura = f"centro_de_dados/sala{id_sala}/temperatura"
            topico_umidade = f"centro_de_dados/sala{id_sala}/umidade"

            cliente.publish(topico_temperatura, temperatura)
            cliente.publish(topico_umidade, umidade)

            print(
                f"[SALA {id_sala}] Publicado -> Temperatura: {temperatura}°C | Umidade: {umidade}%"
            )

        time.sleep(5)
except KeyboardInterrupt:
    print("\nEncerrando o publicador...")
    cliente.disconnect()