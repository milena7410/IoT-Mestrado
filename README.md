# Automação de Refrigeração de Datacenter via MQTT

Trabalho prático da disciplina de IoT (UFMS) para simulação do controle térmico de 3 salas de datacenter utilizando o protocolo MQTT.

---

## Objetivo

Monitorar temperatura e umidade em tempo real e atuar nos aparelhos de ar-condicionado de cada sala seguindo a norma ASHRAE:
* **Temperatura ideal:** 18°C a 27°C
* **Umidade ideal:** 40% a 55%

Se qualquer valor sair da faixa recomendada, o sistema envia o comando `LIGADO` para o ar-condicionado da respectiva sala. Caso contrário, envia `DESLIGADO`.

---

## Estrutura do Sistema

* **Broker MQTT:** `broker.emqx.io` (Porta TCP: `1883` | WebSockets SSL/TLS: `8084`)
* **`publicador.py`:** Simula os sensores das salas enviando medições a cada 5 segundos.
* **`inscrito.py`:** Recebe os dados, aplica a lógica de controle e publica as ações nos atuadores.
* **MQTTX Web:** Usado para validação do tráfego das mensagens.

---

## Tópicos MQTT

| Função | Tópico | Exemplo |
| :--- | :--- | :--- |
| **Sensor de Temperatura** | `centro_de_dados/sala{1..3}/temperatura` | `24.5` |
| **Sensor de Umidade** | `centro_de_dados/sala{1..3}/umidade` | `52.0` |
| **Atuador (Ar-Condicionado)** | `centro_de_dados/sala{1..3}/ar_condicionado` | `LIGADO` / `DESLIGADO` |

---

## Como Executar

### Pré-requisitos
* Python 3.9+
* Biblioteca `paho-mqtt` (`pip install paho-mqtt`)

### Passos:

1. **Rodar o publicador (Terminal 1):**
 controlador_clima.py
 simulador_sensores.py
