from kafka import KafkaConsumer
from os import environ
import sys

servers =  environ.get('BOOTSTRAP_SERVERS')
if servers is None:
    sys.exit('Missing Env Variable BOOTSTRAP_SERVERS')

print("Connecting to bootstrap_servers: %s" % servers)

consumer = KafkaConsumer('test', bootstrap_servers=servers)
for msg in consumer:
    print (msg)