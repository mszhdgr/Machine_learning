from quixstreams import Application

"""
app = Application(
    broker_address="localhost:9092",
    consumer_group="consumer_v1",
    auto_offset_reset="latest"
)

topic = app.topic(name="first_topic", value_deserializer="json")

sdf = app.dataframe(topic=topic)
sdf = sdf.apply(lambda row: print(f"\n__Recieved From Producer___\n{row}"))

if __name__ == "__main__":
    print("Waiting For Producer\n")
    app.run()
"""

app = Application(
    broker_address="localhost:9092",
    consumer_group="random_jokez",
    auto_offset_reset="latest"
)

topic = app.topic(name="random_jokes", value_deserializer="json")
sdf = app.dataframe(topic=topic)
sdf = sdf.apply(lambda row: print(f"\n__Setup:\n\t{row['setup']}\n__Punchline:\n\t{row['punchline']}"))

if __name__ == "__main__":
    print("Waiting for Producer\n")
    app.run()
