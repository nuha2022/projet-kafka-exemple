from flask import Flask, request, jsonify # type: ignore
import producer

app = Flask(__name__)

@app.post("/topics/<topic_name>/publish") 
def push_msg_to_topic(topic_name):
    if request.is_json:
        body = request.get_json()
        # TODO control Data Quality
        try :
            producer.publish(topic_name, body)
            print ('publish to topic {',topic_name,'} : Successeful')
            return body, 201
        except :
            return jsonify( error = "Error Internal to Server"), 500
    return jsonify( error = "Request must be JSON") , 415

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)