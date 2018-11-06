#-*- coding:utf-8 -*-
import pika


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
# 建立一个rabbitmq的连接
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost:5672'))

channel = connection.channel()

channel.queue_declare(queue='hello')
channel.basic_consume(callback,queue='hello',no_ack=True)
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()


