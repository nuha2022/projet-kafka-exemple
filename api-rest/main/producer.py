from confluent_kafka import Producer # type: ignore
import json
from random import randrange
from param import *

import logging, sys
# logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)


producer = Producer(conf)

def delivery_callback(err, msg):
        if err:
            print('ERROR: Message failed delivery: {}'.format(err))
            raise 
        else:
            logging.debug("Produced event to topic {topic}: key = {key:12} value = {value:12}".format(
                topic=msg.topic(), key=msg.key().decode('utf-8'), value=msg.value().decode('utf-8')))

def publish (topic_name, msg):
    producer.produce(topic_name , json.dumps(msg).encode('utf-8'), str(randrange(2)) , callback=delivery_callback  )
    # Block until the messages are sent.
    producer.poll(poll_producer_time)
    producer.flush()
         
         
    
    