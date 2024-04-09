FROM python:3.10 

RUN mkdir -p /app
COPY ../main /app
RUN pip install flask requests confluent_kafka python-dotenv
CMD ["python", "/app/app.py"] 
