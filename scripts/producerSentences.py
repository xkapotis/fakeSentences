from faker import Faker
from kafka import KafkaProducer
import json
import time

fake = Faker()

def get_registered_user():
    return {
        "sentence": fake.sentence(),
        "candidate": "Baiden"
    }

def json_serializer(data):
    return json.dumps(data).encode("utf-8")

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=json_serializer
                         )

if __name__ == "__main__":
    while 1 == 1:
        registered_user = get_registered_user()
        print(registered_user)
        producer.send("baidentopic", registered_user) 
        time.sleep(1)