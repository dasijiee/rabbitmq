#-*- coding:utf-8 -*-
import pika

# 建立一个rabbitmq的连接
connection = pika.BlockingConnection(pika.ConnectionParameters(host='http://47.97.102.218',port=5672))
channel = connection.channel()

# 创建一个hello的队列将消息存入这个队列
channel.queue_declare(queue='hello')
# 使用默认的交换机exchange代表交换机的名字,routing_key指定队列,body表示发送的消息
channel.basic_publish(exchange='',routing_key='hello',body='Hello World!')
connection.close()
print(" [x] Sent 'Hello World!'")


print("just test!")
print("just test!")

