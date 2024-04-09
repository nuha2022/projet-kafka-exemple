import socket

conf = {
    'bootstrap.servers' : '<ip_kafka_stack>:29092',
    'client.id' : 'id-client-2'
}

poll_producer_time = 1000
