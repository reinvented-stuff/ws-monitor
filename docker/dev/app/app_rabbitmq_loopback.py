#!/usr/bin/env python3
# pylint: disable=line-too-long, missing-function-docstring, logging-fstring-interpolation
# pylint: disable=too-many-locals, broad-except, too-many-arguments, raise-missing-from
"""
    Dummy Message Queue client
"""
import logging
import queue
import json
import time

from py_rmq_exchange import ExchangeThread


rmq_server_address = "rabbitmq312"
rmq_exchange = "dev_loopback"

publish_queue = queue.Queue()


logging.root.handlers = []
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s function=%(name)s.%(funcName)s level=%(levelname)s %(message)s",
    handlers=[
        logging.StreamHandler()
    ]
)


def consumer_callback(event):
    logging.info(f"Received inbound event: routing_key={event['method'].routing_key} delivery_tag={event['method'].delivery_tag} event={event}")
    # event_body_json = json.loads(event['body'])

    event['channel'].basic_ack(delivery_tag=event['method'].delivery_tag)

    body = {'loop': time.time(),}
    payload = {
        'body': json.dumps(body),
        'routing_key': "route_9000",
    }
    
    # time.sleep(0.3)
    # publish_queue.put(payload)

    return True


def test_main():
    logging.info("Initialising exchange threads")

    logging.info("Setting up publisher")
    publisher = ExchangeThread(rmq_server_address=rmq_server_address)
    publisher.setup_publisher(
        exchange=rmq_exchange,
        publish_queue=publish_queue,
        auto_ack=False,
    )

    logging.info("Setting up consumer")
    consumer = ExchangeThread(rmq_server_address=rmq_server_address)
    consumer.setup_consumer(
        exchange=rmq_exchange,
        on_message_callback=consumer_callback,
        auto_ack=False,
    )

    publisher.start()
    consumer.start()

    payload = {"loop": 1}

    publish_queue.put(json.dumps(payload))

def loopback():
    logging.info("Initialising exchange threads")

    logging.info("Setting up publisher")
    publisher = ExchangeThread(rmq_server_address=rmq_server_address)
    publisher.setup_publisher(
        exchange=rmq_exchange,
        publish_queue=publish_queue
    )

    # logging.info("Setting up consumer #1")
    # consumer = ExchangeThread(rmq_server_address=rmq_server_address)
    # consumer.setup_consumer(
    #     exchange=rmq_exchange,
    #     on_message_callback=consumer_callback,
    #     queue_name=rmq_queue_1,
    #     exclusive=False,
    #     auto_ack=False,
    # )

    # logging.info("Setting up consumer #2")
    # consumer_2 = ExchangeThread(rmq_server_address=rmq_server_address)
    # consumer_2.setup_consumer(
    #     exchange=rmq_exchange,
    #     on_message_callback=consumer_callback,
    #     queue_name=rmq_queue_2,
    #     exclusive=False,
    #     auto_ack=False,
    # )

    publisher.start()
    # consumer.start()


    while True:
        body = {'timestamp': time.time(),}
        payload = {
            'body': json.dumps(body),
            'routing_key': "dev_rk_static",
        }
        
        logging.info(f"Sending message: {payload}")
        publish_queue.put(payload)

        time.sleep(1)

    # consumer_2.start()

if __name__ == '__main__':
    # test_main()
    loopback()
