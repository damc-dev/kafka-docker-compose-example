from kafka import KafkaProducer
import json
from os import environ
import sys

servers =  environ.get('BOOTSTRAP_SERVERS')
if servers is None:
    sys.exit('Missing Env Variable BOOTSTRAP_SERVERS')

print("Connecting to bootstrap_servers: %s" % servers)

producer = KafkaProducer(bootstrap_servers=servers, api_version=(0,10), value_serializer=lambda v: json.dumps(v).encode('utf-8'))
futures = []
for x in range(100):
    data = {'id': x, 'foo': 'bar'}
    print(json.dumps(data))
    futures.append(producer.send('test', data))
ret = [f.get(timeout=30) for f in futures]
producer.close()