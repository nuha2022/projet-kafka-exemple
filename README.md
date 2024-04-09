# Get-Started-Kafka

Install prerequisites : 
pip install flask confluent_kafka pymongo

Run Kafka Broker :
cd kafka-stack
docker-compose -f single-kafka.yml up -d


Run API REST module :
update param.py, set <ip_kafka_stack> value

cd api-rest
make compose

Run Consumer module :
update param.py, set {{ip_kafka}}, connexion url = {{user}}:{{mdp}}@{{cluster_db}} values

cd app-business
make compose

