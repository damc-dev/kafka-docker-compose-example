from kafka import KafkaProducer
import json
producer = KafkaProducer(bootstrap_servers='localhost:9092', api_version=(0,10), value_serializer=lambda v: json.dumps(v).encode('utf-8'))
futures = []
for x in range(100):
    data = {'id': x, 'foo': 'bar'}
    print(json.dumps(data))
    futures.append(producer.send('test', data))
ret = [f.get(timeout=30) for f in futures]
producer.close()