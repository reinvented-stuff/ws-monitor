# Develompent environment

## Start

```bash
docker-compose up -d
```

## General information

### Credentials

**Admin**: 

* login: Visitor
* password: visitor

**Guest**: 

* login: guest
* password: guest

### RabbitMQ

* AMQP — localhost:5672
* Management — http://localhost:15672

### MQTT

* MQTT — localhost:1883 
* MQTT Web — localhost:15675

### STOMP

* STOMP — localhost:61613
* STOMP Web — localhost:15674


### Metrics

* Prometheus: http://localhost:15692/metrics


## STOMP via telnet

`^@` - a control character that can be reproduced on OS X by pressing control+shift+2

Install telnet on your computer (brew, port, other)

```
telnet localhost 61613
```

```
CONNECT
login:guest
passcode:guest

^@
```

```
SUBSCRIBE
destination: /exchange/dev_loopback
ack: auto

^@
```
