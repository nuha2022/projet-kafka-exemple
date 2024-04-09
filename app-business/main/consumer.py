
from confluent_kafka import Consumer # type: ignore
import param
import service

def main():
    conf = {
        'bootstrap.servers' : param.kafkaBroker,
        'group.id': param.groupID
    }

    consumer = Consumer(conf)
    consumer.subscribe(param.topics)

    try:        
        while True :
            msg = consumer.poll(5.0)
            if msg is None : 
                print ("Waiting ...")
                continue
            elif msg.error():
                print("ERROR: %s".format(msg.error()))
            else : 
                service.process_msg(msg.value().decode('utf-8'))
                print("Consumed event from topic {topic}: key = {key:12} value = {value:12}".format(
                        topic=msg.topic(), key=msg.key().decode('utf-8'), value=msg.value().decode('utf-8')))
    except KeyboardInterrupt :
        pass
    finally:
        consumer.close()

if __name__ == '__main__':
    main()