import paho.mqtt.client as cliente_mqtt

SERVIDOR_BROKER = "broker.emqx.io"
PORTA_BROKER = 1883

estado_salas = {
    1: {"temperatura": None, "umidade": None},
    2: {"temperatura": None, "umidade": None},
    3: {"temperatura": None, "umidade": None},
}


def ao_conectar(cliente, userdata, flags, rc, propriedades=None):
    print("Conectado ao Broker MQTT com sucesso!")
    cliente.subscribe("centro_de_dados/sala/+/temperatura")
    cliente.subscribe("centro_de_dados/sala/+/umidade")
    print("Inscrito nos tópicos de sensores. Aguardando dados...\n")


def avaliar_e_controlar(cliente, sala_id):
    dados = estado_salas[sala_id]
    temp = dados["temperatura"]
    umid = dados["umidade"]

    #só toma decisão quando tiver recebido ambas as leituras da sala
    if temp is None or umid is None:
        return

    topico_atuador = f"centro_de_dados/sala{sala_id}/ar_condicionado"

    #regra de Controle ASHRAE:::
    if temp > 27.0 or umid > 55.0:
        comando = "LIGADO"
        motivo = "Fora dos limites ideais (Alta temperatura/umidade)"
    else:
        comando = "DESLIGADO"
        motivo = "Condições ideais ou abaixo do limite"

    cliente.publish(topico_atuador, comando)
    print(
        f"[CONTROLE SALA {sala_id}] Temp: {temp}°C | Umidade: {umid}% -> Ar-Condicionado: {comando} ({motivo})"
    )


def ao_receber_mensagem(cliente, userdata, msg):
    topico = msg.topic
    valor = float(msg.payload.decode())

    partes = topico.split("/")
    sala_str = partes[1] 
    sala_id = int(sala_str.replace("sala", ""))

    if "temperatura" in topico:
        estado_salas[sala_id]["temperatura"] = valor
    elif "umidade" in topico:
        estado_salas[sala_id]["umidade"] = valor

    avaliar_e_controlar(cliente, sala_id)


#configuração do Cliente MQTT
cliente = cliente_mqtt.Client(
    callback_api_version=cliente_mqtt.CallbackAPIVersion.VERSION2,
    client_id="Controlador_ArCondicionado_CentroDeDados",
)

cliente.on_connect = ao_conectar
cliente.on_message = ao_receber_mensagem

cliente.connect(SERVIDOR_BROKER, PORTA_BROKER, 60)

try:
    cliente.loop_forever()
except KeyboardInterrupt:
    print("\nEncerrando o controlador...")
    cliente.disconnect()