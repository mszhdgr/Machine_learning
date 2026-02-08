from quixstreams import Application
import time
import requests

app = Application(broker_address="localhost:9092")

"""topic = app.topic(name="first_topic", value_serializer="json")


with app.get_producer() as producer:
    data = {"Message": "This is Big Bluud Yeah!! Massive Ting You Get Me"}
    serializer = topic.serialize(value=data, key="key_1")
    producer.produce(
        topic=topic.name,
        value=serializer.value,
        key=serializer.key
    )
    print(f"SENT TO CONSUMER ---> {data}")"""

topic = app.topic(name="random_jokes", value_serializer="json")

URL = "https://official-joke-api.appspot.com/random_joke"

def get_and_produce_data(url):
    try:
        while True:
            req = requests.get(url=url)
            res = req.json()
            with app.get_producer() as producer:
                serializer = topic.serialize(value=res, key="joke")
                producer.produce(
                    topic=topic.name,
                    value=serializer.value,
                    key=serializer.key
                )
                print(f"SENT TO CONSUMER ---> {res}")
                time.sleep(10)

    except Exception as e:
        print(f"An Error Occured: {e}")

print("\nSending data to consumer\n")
get_and_produce_data(url=URL)