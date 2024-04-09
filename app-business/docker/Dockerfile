FROM python:3.10 

RUN mkdir -p /app

COPY ../main /app/
RUN pip install confluent_kafka pymongo python-dotenv
CMD ["python", "/app/consumer.py"] 
