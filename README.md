# 🌡️ Controle Térmico de Datacenter via MQTT

> **Trabalho prático da disciplina de IoT**  
> **Docente:** Dra. Hana Karina Salles Rubinsztejn  
> **Programa de Mestrado**
---
## Objetivo
Monitorar temperatura e umidade em tempo real e atuar nos aparelhos de ar-condicionado de cada sala seguindo a norma ASHRAE:
* **Temperatura ideal:** 18°C a 27°C
* **Umidade ideal:** 40% a 55%

Se qualquer valor sair da faixa recomendada, o sistema envia o comando `LIGADO` para o ar-condicionado da respectiva sala. Caso contrário, envia `DESLIGADO`.

## Estrutura do Sistema
* **Broker MQTT:** `broker.emqx.io` (Porta TCP: `1883` | WebSockets SSL/TLS: `8084`)
* **MQTTX Web:** Usado para validação do tráfego das mensagens.

## Tópicos MQTT
| Função | Tópico | Exemplo |
| :--- | :--- | :--- |
| **Sensor de Temperatura** | `centro_de_dados/sala{1..3}/temperatura` | `24.5` |
| **Sensor de Umidade** | `centro_de_dados/sala{1..3}/umidade` | `52.0` |
| **Atuador (Ar-Condicionado)** | `centro_de_dados/sala{1..3}/ar_condicionado` | `LIGADO` / `DESLIGADO` |


## Como Executar:
### Pré-requisitos
* Python 3.9+
* Biblioteca `paho-mqtt` (`pip install paho-mqtt`)

### Passos:

1. **Rodar em terminais diferentes:**
 controlador_clima.py
 simulador_sensores.py

### Imagens:
<img width="1582" height="957" alt="Captura de Tela 2026-10-05 às 20 21 37" src="https://github.com/user-attachments/assets/6af8aad4-91f1-4869-91cb-6f3adf1c9d16" />
<img width="1470" height="923" alt="Captura de Tela 2026-10-05 às 20 21 08" src="https://github.com/user-attachments/assets/5bbae974-0a41-4210-880c-13c18ad602fe" />
<img width="1470" height="923" alt="Captura de Tela 2026-10-05 às 20 20 56" src="https://github.com/user-attachments/assets/9b8823fe-9a73-4101-82e9-f7d2cb543559" />

